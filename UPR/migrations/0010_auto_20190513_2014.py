# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-13 18:14
from __future__ import unicode_literals

import UPR.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UPR', '0009_auto_20190513_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipomaquina',
            name='img_maquina',
            field=models.ImageField(blank=True, null=True, upload_to=UPR.models.upload_location),
        ),
        migrations.AddField(
            model_name='tipomaquina',
            name='url_tienda_maquina',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]