# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-16 00:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0022_generalsubsystem_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generalsubsystem',
            name='image',
        ),
    ]
