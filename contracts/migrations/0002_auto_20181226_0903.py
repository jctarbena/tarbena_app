# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-12-26 08:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contract',
            options={'ordering': ['contractor', 'contractor__dni', 'date_contract'], 'verbose_name': 'Contratos', 'verbose_name_plural': 'Contratos'},
        ),
    ]