# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-27 16:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxes', '0008_auto_20180520_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tax',
            name='CNT_Employer',
        ),
        migrations.RemoveField(
            model_name='tax',
            name='EI_Employee',
        ),
        migrations.RemoveField(
            model_name='tax',
            name='EI_Employer',
        ),
        migrations.RemoveField(
            model_name='tax',
            name='Federal_Income_Tax',
        ),
        migrations.RemoveField(
            model_name='tax',
            name='QHSF_Employer',
        ),
        migrations.RemoveField(
            model_name='tax',
            name='QPIP_Employee',
        ),
        migrations.RemoveField(
            model_name='tax',
            name='QPIP_Employer',
        ),
        migrations.RemoveField(
            model_name='tax',
            name='QPP_Employee',
        ),
        migrations.RemoveField(
            model_name='tax',
            name='QPP_Employer',
        ),
        migrations.RemoveField(
            model_name='tax',
            name='Quebec_Income_Tax',
        ),
        migrations.RemoveField(
            model_name='tax',
            name='Vacation_Pay',
        ),
    ]