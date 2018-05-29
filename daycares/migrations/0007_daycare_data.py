# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-19 17:31
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('daycares', '0006_remove_daycare_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='daycare',
            name='data',
            field=jsonfield.fields.JSONField(default={b'CSST': 0.68}),
        ),
    ]