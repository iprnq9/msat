# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-13 02:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0004_project_quick_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='full_description',
            field=models.TextField(default='Full description'),
            preserve_default=False,
        ),
    ]
