# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-16 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UPR', '0010_auto_20190513_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupocomponentes',
            name='position_grupo_componentes',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]