# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-21 19:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0012_payroll_taxes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payroll',
            old_name='taxes',
            new_name='payroll_taxes',
        ),
    ]
