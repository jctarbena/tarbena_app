# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-24 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20181024_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='apellidos2',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
