# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import uuid
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from stdimage import StdImageField
from django.conf import settings

from django.db import connection
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator





class User(AbstractUser):
    numero_regex = RegexValidator(
        regex=r'^\d+$', message=_('Ingrese solo números.'))

    # Create your models here.
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message=_(
    "Número de teléfono debe estar en el formato: '+999999999'. Hasta 15 dígitos permitidos."))

    ADMIN = 'Admin'
    TECNICO = 'Tecnico'
    SOPORTE = 'Soporte'
    VENTAS = 'Ventas'
    CLIENTE = 'Cliente'
    PROSPECTO = 'Prospecto'
    TYPE = (
        (ADMIN, _('Administrador')),
        (TECNICO, _('Técnico')),
        (SOPORTE, _('Soporte')),
        (VENTAS, _('Ventas')),
        (CLIENTE, _('Cliente')),
        (PROSPECTO, _('Prospecto')),
    )

    MORAL = 'Moral/Juridica'
    FISICA = 'Fisica/Natural'
    TIPO_PERSONA = (
        (FISICA, _('Fisica/Natural')),
        (MORAL, _('Moral/Juridica'))
    )

    def avatar_path(self, filename):
        extension = os.path.splitext(filename)[1][1:]
        file_name = os.path.splitext(filename)[0]
        url = "usuarios/{}/avatar/{}.{}".format(
            settings.LOTE_PRINCIPAL, slugify(str(file_name)), extension
        )
        return url

    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, db_index=True, unique=True)
    avatar = StdImageField(_('Avatar'), upload_to='usuarios/%Y/%m/', default='usuarios/avatar.png',
                           variations={
                               'perfil': {'width': 240, 'height': 240, 'crop': True},
                               'thumbnail': {'width': 45, 'height': 45, 'crop': True}
    })
    address = models.TextField(_("Dirección"), blank=True)
    phone_number = models.CharField(_("Teléfono Celular"), max_length=250, blank=True,
                                    validators=[phone_regex])
    rfc = models.CharField('RFC/RUC/NIT', max_length=30, blank=True)
    legal_name = models.CharField(
        _('Nombre facturación'), max_length=255, blank=True)
    tax_id = models.CharField('RFC/RUC', max_length=30, blank=True)
    tax_system = models.CharField(
        _('Regimen fiscal'), max_length=10, blank=True, null=True)
    postal_code = models.CharField(
        _('Código postal'), max_length=50, blank=True)
    billing_address = models.TextField(
        _('Dirección de facturación'), max_length=100, blank=True)
    billing_email = models.EmailField(_('Email de facturación'), blank=True)
    district = models.CharField(
        _('Localidad/Barrio/Departamento'), max_length=50, blank=True)
    city = models.CharField(_('Ciudad/Municipio'), max_length=50, blank=True)
    license = models.CharField(
        _('Licencia DNI/C.I./C.C.'), max_length=35, blank=True)

    # relations
    user_type = models.ForeignKey('users.TipoUsuario', verbose_name=_('Tipo de usuario'), null=True,
                                  related_name='user_type_user', on_delete=models.SET_NULL)
    
    person_type = models.ForeignKey('users.TipoPersona', verbose_name=_('Tipo de persona'), blank=True, null=True,
                                    related_name='person_type_user', on_delete=models.SET_NULL)

    status = models.ForeignKey("users.ClientStatus", related_name="client_status", verbose_name=_("Estatus"),
                               on_delete=models.SET_NULL, null=True, blank=True)

    company = models.ForeignKey('sistema.Empresa', verbose_name=_('Empresa'), null=True, related_name='company_user',
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.username + '-' + self.get_full_name()

    class Meta:
        ordering = ('-id',)

class TipoUsuario(models.Model):
    name = models.CharField(_('Nombre'), max_length=20)

    def __str__(self):
        return self.name


class TipoPersona(models.Model):
    name = models.CharField(_('Nombre'), max_length=20)

    def __str__(self):
        return self.name


class ClientStatus(models.Model):
    name = models.CharField(max_length=70, verbose_name=_('Nombre'))
    class_css = models.CharField(
        max_length=40, verbose_name=_("Class ccs color"))
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = _("Estado Clientes")
        verbose_name_plural = _("Estado Clientes")

    def __str__(self):
        return self.name


