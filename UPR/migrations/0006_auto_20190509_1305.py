# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-09 11:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UPR', '0005_auto_20190509_1300'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incidencias',
            options={'verbose_name': 'Incidencia', 'verbose_name_plural': 'Incidencias'},
        ),
    ]