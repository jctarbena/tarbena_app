# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-08 06:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contract',
            options={'ordering': ['type'], 'verbose_name': 'Contratos', 'verbose_name_plural': 'Contratos'},
        ),
    ]
