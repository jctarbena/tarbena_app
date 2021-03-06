# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-04 09:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profiles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('avatar', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=profiles.models.upload_location, width_field='width_field')),
                ('height_field', models.IntegerField(blank=True, default=0, null=True)),
                ('width_field', models.IntegerField(blank=True, default=0, null=True)),
                ('telefono', models.CharField(blank=True, max_length=250, null=True)),
                ('direccion', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
