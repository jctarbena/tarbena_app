# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-10 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcelas', '0005_auto_20181010_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcela',
            name='poligono',
            field=models.CharField(max_length=250),
        ),
    ]
