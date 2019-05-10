# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-09 09:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UPR', '0003_auto_20190509_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='componentes',
            name='tipo_maquina',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tipo_maquina_componente', to='UPR.TipoMaquina'),
        ),
    ]
