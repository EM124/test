# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-20 06:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worklogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worklog',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
