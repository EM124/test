# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-21 00:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('daycares', '0012_auto_20180520_2154'),
        ('accounts', '0011_user_salary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='daycare',
        ),
        migrations.AddField(
            model_name='user',
            name='daycare',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='daycares.Daycare'),
            preserve_default=False,
        ),
    ]
