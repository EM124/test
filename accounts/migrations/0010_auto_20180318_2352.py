# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-18 23:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20180318_0603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='full_name',
            new_name='adult_first_name',
        ),
        migrations.AddField(
            model_name='user',
            name='adult_last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
