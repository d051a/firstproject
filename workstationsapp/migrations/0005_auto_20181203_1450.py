# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-03 11:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workstationsapp', '0004_auto_20181203_1443'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='computer',
            options={'default_permissions': ('add', 'change', 'delete', 'view'), 'verbose_name': 'Компьютер', 'verbose_name_plural': 'Компьютеры'},
        ),
        migrations.AlterModelOptions(
            name='computermodel',
            options={'default_permissions': ('add', 'change', 'delete', 'view'), 'verbose_name': 'Модель компьютера', 'verbose_name_plural': 'Модели компьютера'},
        ),
    ]
