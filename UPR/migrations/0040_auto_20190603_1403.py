# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-06-03 12:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UPR', '0039_auto_20190603_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maquina',
            name='poblacion',
        ),
        migrations.AddField(
            model_name='movimientomaquinaria',
            name='numero_inventario_mm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='numeroInventario', to='UPR.Maquina'),
        ),
    ]