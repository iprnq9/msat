# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-15 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0020_remove_subsystem_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalsubsystem',
            name='nickname',
            field=models.CharField(default='COMM', max_length=8),
            preserve_default=False,
        ),
    ]
