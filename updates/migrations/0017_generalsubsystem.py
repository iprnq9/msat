# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-15 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0016_auto_20161112_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralSubsystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('short_description', models.CharField(max_length=150)),
                ('full_description', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
