# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-02-08 11:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parcelas', '0026_poblacionesfavoritas_superfavorita'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parcela',
            options={'ordering': ['propietario', 'poligono'], 'permissions': (('acceder_parcelas', 'Puede acceder a la app de parcelas'),), 'verbose_name': 'Parcela', 'verbose_name_plural': 'Parcelas'},
        ),
    ]