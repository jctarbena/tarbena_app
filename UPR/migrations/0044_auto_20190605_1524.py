# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-06-05 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UPR', '0043_remove_maquina_obra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movimientomaquinaria',
            name='numero_inventario_mm',
        ),
        migrations.AddField(
            model_name='maquina',
            name='maquina_poblacion',
            field=models.ManyToManyField(blank=True, related_name='nombre_poblacion', to='UPR.MovimientoMaquinaria'),
        ),
        migrations.AddField(
            model_name='movimientomaquinaria',
            name='comentario',
            field=models.TextField(blank=True, null=True),
        ),
    ]