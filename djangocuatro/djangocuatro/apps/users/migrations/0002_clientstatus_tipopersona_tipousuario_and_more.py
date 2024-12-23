# Generated by Django 4.2 on 2024-12-16 23:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Nombre')),
                ('class_css', models.CharField(max_length=40, verbose_name='Class ccs color')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Estado Clientes',
                'verbose_name_plural': 'Estado Clientes',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='TipoPersona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Nombre')),
            ],
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('-id',)},
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, verbose_name='Dirección'),
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=stdimage.models.StdImageField(default='usuarios/avatar.png', force_min_size=False, upload_to='usuarios/%Y/%m/', variations={'perfil': {'crop': True, 'height': 240, 'width': 240}, 'thumbnail': {'crop': True, 'height': 45, 'width': 45}}, verbose_name='Avatar'),
        ),
        migrations.AddField(
            model_name='user',
            name='billing_address',
            field=models.TextField(blank=True, max_length=100, verbose_name='Dirección de facturación'),
        ),
        migrations.AddField(
            model_name='user',
            name='billing_email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email de facturación'),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=50, verbose_name='Ciudad/Municipio'),
        ),
        migrations.AddField(
            model_name='user',
            name='district',
            field=models.CharField(blank=True, max_length=50, verbose_name='Localidad/Barrio/Departamento'),
        ),
        migrations.AddField(
            model_name='user',
            name='legal_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Nombre facturación'),
        ),
        migrations.AddField(
            model_name='user',
            name='license',
            field=models.CharField(blank=True, max_length=35, verbose_name='Licencia DNI/C.I./C.C.'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=250, validators=[django.core.validators.RegexValidator(message="Número de teléfono debe estar en el formato: '+999999999'. Hasta 15 dígitos permitidos.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Teléfono Celular'),
        ),
        migrations.AddField(
            model_name='user',
            name='postal_code',
            field=models.CharField(blank=True, max_length=50, verbose_name='Código postal'),
        ),
        migrations.AddField(
            model_name='user',
            name='rfc',
            field=models.CharField(blank=True, max_length=30, verbose_name='RFC/RUC/NIT'),
        ),
        migrations.AddField(
            model_name='user',
            name='tax_id',
            field=models.CharField(blank=True, max_length=30, verbose_name='RFC/RUC'),
        ),
        migrations.AddField(
            model_name='user',
            name='tax_system',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Regimen fiscal'),
        ),
        migrations.AddField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='person_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person_type_user', to='users.tipopersona', verbose_name='Tipo de persona'),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_status', to='users.clientstatus', verbose_name='Estatus'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_type_user', to='users.tipousuario', verbose_name='Tipo de usuario'),
        ),
    ]
