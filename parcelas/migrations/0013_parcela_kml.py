# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-09 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcelas', '0012_auto_20181218_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcela',
            name='kml',
            field=models.TextField(blank=True, null=True),
        ),
    ]