# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-16 12:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parcelas', '0015_remove_poblacionesfavoritas_favorito'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propietario',
            name='poblacion',
        ),
    ]
