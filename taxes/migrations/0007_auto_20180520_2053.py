# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-20 20:53
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taxes', '0006_auto_20180519_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tax',
            name='taxes',
        ),
        migrations.AddField(
            model_name='tax',
            name='global_company_taxes',
            field=jsonfield.fields.JSONField(default={b'CNT_Employer': 0.0007, b'EI_Employer': 0.0182, b'QHSF_Employer': 0.023, b'QPIP_Employer': 0.00767, b'QPP_Employer': 0.04564, b'Vacation_Pay': 0.04}),
        ),
        migrations.AddField(
            model_name='tax',
            name='global_employee_taxes',
            field=jsonfield.fields.JSONField(default={b'EI_Employee': 0.013, b'Federal_Income_Tax': 0.04522, b'QPIP_Employee': 0.00548, b'QPP_Employee': 0.04564, b'Quebec_Income_Tax': 0.04283}),
        ),
    ]
