# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-13 03:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0014_timeline_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]