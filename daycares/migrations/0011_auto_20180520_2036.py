# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-20 20:36
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('daycares', '0010_auto_20180520_1744'),
    ]

    operations = [
        migrations.RenameField(
            model_name='daycare',
            old_name='unique_taxes',
            new_name='unique_company_taxes',
        ),
        migrations.AddField(
            model_name='daycare',
            name='unique_employee_taxes',
            field=jsonfield.fields.JSONField(default={}),
        ),
    ]
