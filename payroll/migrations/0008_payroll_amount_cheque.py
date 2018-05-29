# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-22 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0007_payroll_amount_ytd'),
    ]

    operations = [
        migrations.AddField(
            model_name='payroll',
            name='amount_cheque',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
    ]