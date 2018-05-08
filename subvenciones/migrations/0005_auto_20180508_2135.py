# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-08 19:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subvenciones', '0004_subvencion_responsable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subvencion',
            name='responsable',
            field=models.ManyToManyField(blank=True, related_name='responsable', to=settings.AUTH_USER_MODEL),
        ),
    ]