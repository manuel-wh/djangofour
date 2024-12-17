from django.db import models

import os
import uuid
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from stdimage import StdImageField

from django_countries.fields import CountryField
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class Empresa(models.Model):
    
    # Create your models here.
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message=_(
    "Número de teléfono debe estar en el formato: '+999999999'. Hasta 15 dígitos permitidos."))
    
    def logo_path(self, filename):
        extension = os.path.splitext(filename)[1][1:]
        file_name = os.path.splitext(filename)[0]
        url = "empresas/{}/logo/{}.{}".format(
            self.schema_name, slugify(str(file_name)), extension
        )
        return url

    ACTIVO = 1
    SUSPENDIDO = 2
    CANCELADO = 3
    ESTADO_EMPRESA = (
        (ACTIVO, 'Activo'),
        (SUSPENDIDO, 'Suspendido'),
        (CANCELADO, 'Cancelado'),
    )
    uuid = models.UUIDField(verbose_name=_('Identificador de empresa'), editable=False, default=uuid.uuid4,
                            db_index=True, unique=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Registro')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Última Actualización')

    nombre = models.CharField(max_length=80, unique=True)
    email = models.EmailField(blank=True)
    direccion = models.TextField(max_length=100, blank=True)
    telefono = models.CharField(
        validators=[phone_regex], max_length=15, blank=True)
    pais = CountryField()
    detalles = models.TextField(verbose_name="Detalles", blank=True)
    logo = StdImageField(upload_to=logo_path, default="empresas/logo-blanco.png",
                         variations={'thumbnail': {"width": 180, "height": 50, "crop": False}})
    estado = models.PositiveSmallIntegerField(
        choices=ESTADO_EMPRESA, default=ACTIVO, blank=True)
    is_active = models.BooleanField(default=True)

    fecha_contratacion = models.DateTimeField(blank=True, null=True)
    fecha_suspension = models.DateTimeField(
        blank=True, null=True, verbose_name="Fecha de Suspension")

    nombre_facturacion = models.CharField(max_length=255, blank=True)
    rfc = models.CharField(max_length=30, blank=True, verbose_name="RFC/RUC")
    regimen_fiscal = models.CharField(max_length=10, blank=True, null=True)
    codigo_postal = models.CharField(max_length=50, blank=True)
    direccion_facturacion = models.TextField(max_length=100, blank=True)
    email_facturacion = models.EmailField(blank=True)

    timezone = models.CharField(
        max_length=190, blank=False, null=False, default="Etc/UTC")
    # Grupos de Servidores y Subdominios
    external_id = models.PositiveIntegerField(_('Id externo del lote al que pertenece'), db_index=True, blank=True,
                                              null=True)
    lote = models.CharField(_('Lote al que pertenece'),
                            max_length=50, default=settings.LOTE_PRINCIPAL)

    plan = models.ForeignKey('sistema.PlanEmpresa', related_name="empresa_plan_empresa", on_delete=models.SET_NULL,
                             null=True, blank=True,)

    class Meta:
        verbose_name = _("Empresa")
        verbose_name_plural = _("Empresas")
        permissions = {
            ('lista_empresas', _('Lista de empresas')),
            ('acciones_lista_empresas', _('Acciones lista de empresas')),
            ('crear_superusuarios', _('Crear super usuarios')),
            ('eliminar_superusuarios', _('Eliminar super usuarios')),
            ('ver_perfil_financiero', _('Ver perfil financiero')),
        }

    def __str__(self):
        return f"{self.nombre}"

    def save(self, verbosity=1, *args, **kwargs):
        super().save()


class PlanEmpresa(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    precio_sin_iva = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    mostrar = models.BooleanField(default=False)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Última Actualización')

    class Meta:
        ordering = ('-created',)
        verbose_name = "Plan"
        verbose_name_plural = "Planes"

    def __str__(self):
        return '{}'.format(self.nombre)


# Modelos Giro

class Categoria(models.Model):
    nombre = models.CharField(_('Nombre'), max_length=100)
    descripcion = models.TextField(_('Descripción'), blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = _('Categoría')
        verbose_name_plural = _('Categorías')


class Proveedor(models.Model):
    nombre = models.CharField(_('Nombre'), max_length=100)
    direccion = models.TextField(_('Dirección'), blank=True)
    telefono = models.CharField(_('Teléfono'), max_length=15, blank=True)
    email = models.EmailField(_('Email'), blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = _('Proveedor')
        verbose_name_plural = _('Proveedores')


class Producto(models.Model):
    nombre = models.CharField(_('Nombre'), max_length=100)
    descripcion = models.TextField(_('Descripción'), blank=True)
    precio = models.DecimalField(_('Precio'), max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(_('Stock'))
    categoria = models.ForeignKey(Categoria, verbose_name=_(
        'Categoría'), on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, verbose_name=_(
        'Proveedor'), on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = _('Producto')
        verbose_name_plural = _('Productos')


class Cliente(models.Model):
    nombre = models.CharField(_('Nombre'), max_length=100)
    direccion = models.TextField(_('Dirección'), blank=True)
    telefono = models.CharField(_('Teléfono'), max_length=15, blank=True)
    email = models.EmailField(_('Email'), blank=True)
    fecha_registro = models.DateTimeField(
        _('Fecha de Registro'), auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = _('Cliente')
        verbose_name_plural = _('Clientes')
