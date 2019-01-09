# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-12-18 11:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parcelas', '0011_auto_20181218_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcela',
            name='estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='estado', to='parcelas.Estado'),
        ),
    ]