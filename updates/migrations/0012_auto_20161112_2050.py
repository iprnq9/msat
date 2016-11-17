# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-13 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0011_subsystem_meeting_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsystem',
            name='meeting_frequency',
            field=models.CharField(choices=[('Weekly', 'Every week'), ('Biweekly', 'Every other week'), ('Monthly', 'Once a month')], default='Weekly', max_length=20),
        ),
    ]
