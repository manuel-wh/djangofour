# Generated by Django 4.2 on 2024-12-17 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
        ('users', '0002_clientstatus_tipopersona_tipousuario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_user', to='sistema.empresa', verbose_name='Empresa'),
        ),
    ]