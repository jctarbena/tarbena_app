# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-06-03 11:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UPR', '0038_auto_20190531_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movimientomaquinaria',
            name='numero_inventario_mm',
        ),
        migrations.AlterField(
            model_name='maquina',
            name='poblacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nombrePoblacionMaquina', to='UPR.MovimientoMaquinaria'),
        ),
    ]