# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-13 02:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0008_subsystem_meeting_frequency'),
    ]

    operations = [
        migrations.AddField(
            model_name='subsystem',
            name='meeting_day',
            field=models.CharField(choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], default='Monday', max_length=20),
        ),
    ]
