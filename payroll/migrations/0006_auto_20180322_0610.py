# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-22 06:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0005_auto_20180322_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payroll',
            name='year',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]