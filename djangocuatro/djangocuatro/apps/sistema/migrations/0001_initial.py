# Generated by Django 4.2 on 2024-12-17 14:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import djangocuatro.apps.sistema.models
import stdimage.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlanEmpresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio_sin_iva', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('mostrar', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Última Actualización')),
            ],
            options={
                'verbose_name': 'Plan',
                'verbose_name_plural': 'Planes',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True, verbose_name='Identificador de empresa')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Última Actualización')),
                ('nombre', models.CharField(max_length=80, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('direccion', models.TextField(blank=True, max_length=100)),
                ('telefono', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Número de teléfono debe estar en el formato: '+999999999'. Hasta 15 dígitos permitidos.", regex='^\\+?1?\\d{9,15}$')])),
                ('pais', django_countries.fields.CountryField(max_length=2)),
                ('detalles', models.TextField(blank=True, verbose_name='Detalles')),
                ('logo', stdimage.models.StdImageField(default='empresas/logo-blanco.png', force_min_size=False, upload_to=djangocuatro.apps.sistema.models.Empresa.logo_path, variations={'thumbnail': {'crop': False, 'height': 50, 'width': 180}})),
                ('estado', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Activo'), (2, 'Suspendido'), (3, 'Cancelado')], default=1)),
                ('is_active', models.BooleanField(default=True)),
                ('fecha_contratacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_suspension', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Suspension')),
                ('nombre_facturacion', models.CharField(blank=True, max_length=255)),
                ('rfc', models.CharField(blank=True, max_length=30, verbose_name='RFC/RUC')),
                ('regimen_fiscal', models.CharField(blank=True, max_length=10, null=True)),
                ('codigo_postal', models.CharField(blank=True, max_length=50)),
                ('direccion_facturacion', models.TextField(blank=True, max_length=100)),
                ('email_facturacion', models.EmailField(blank=True, max_length=254)),
                ('timezone', models.CharField(default='Etc/UTC', max_length=190)),
                ('external_id', models.PositiveIntegerField(blank=True, db_index=True, null=True, verbose_name='Id externo del lote al que pertenece')),
                ('lote', models.CharField(default='A', max_length=50, verbose_name='Lote al que pertenece')),
                ('plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='empresa_plan_empresa', to='sistema.planempresa')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
                'permissions': {('lista_empresas', 'Lista de empresas'), ('crear_superusuarios', 'Crear super usuarios'), ('ver_perfil_financiero', 'Ver perfil financiero'), ('acciones_lista_empresas', 'Acciones lista de empresas'), ('eliminar_superusuarios', 'Eliminar super usuarios')},
            },
        ),
    ]