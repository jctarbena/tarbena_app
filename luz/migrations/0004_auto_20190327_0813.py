# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-27 07:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('luz', '0003_auto_20190318_1221'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='factura',
            options={'ordering': ['contador'], 'verbose_name': 'Factura', 'verbose_name_plural': 'Facturas'},
        ),
    ]