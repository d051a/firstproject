# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-03 11:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serversapp', '0003_auto_20181203_1249'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='server',
            options={'default_permissions': ('add', 'change', 'delete', 'view'), 'ordering': ['name'], 'verbose_name': 'Сервер', 'verbose_name_plural': 'Серверы'},
        ),
    ]
