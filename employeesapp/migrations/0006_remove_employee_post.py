# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-30 14:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeesapp', '0005_auto_20181030_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='post',
        ),
    ]
