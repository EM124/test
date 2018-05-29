# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-20 21:54
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('daycares', '0011_auto_20180520_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daycare',
            name='unique_company_taxes',
            field=jsonfield.fields.JSONField(blank=True, default={b'CSST': 0.68}, null=True),
        ),
        migrations.AlterField(
            model_name='daycare',
            name='unique_employee_taxes',
            field=jsonfield.fields.JSONField(blank=True, default={}, null=True),
        ),
    ]