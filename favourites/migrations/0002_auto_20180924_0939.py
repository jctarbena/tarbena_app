# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-24 07:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('favourites', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favourite',
            name='user',
        ),
        migrations.AddField(
            model_name='favourite',
            name='user',
            field=models.ManyToManyField(blank=True, related_name='favourite_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
