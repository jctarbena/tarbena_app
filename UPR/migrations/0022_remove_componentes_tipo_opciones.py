# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-20 08:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UPR', '0021_componentes_tipo_opciones'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='componentes',
            name='tipo_opciones',
        ),
    ]
