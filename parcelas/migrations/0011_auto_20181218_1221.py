# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-12-18 11:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parcelas', '0010_auto_20181217_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcela',
            name='propietario',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='propietario', to='parcelas.Propietario'),
        ),
    ]
