# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-12-17 07:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parcelas', '0008_estado_parcela_trabajo'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcela',
            name='estado_parcela_trabajo',
            field=models.ForeignKey(blank=True, default=3, null=True, on_delete=django.db.models.deletion.CASCADE, to='parcelas.Estado_Parcela_Trabajo'),
        ),
    ]
