# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-13 02:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0007_subsystem_quick_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='subsystem',
            name='meeting_frequency',
            field=models.CharField(choices=[('weekly', 'Every week'), ('every other week', 'Every other week'), ('once a month', 'Once a month')], default='Weekly', max_length=20),
        ),
    ]
