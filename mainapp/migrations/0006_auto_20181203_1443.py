# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-03 11:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20181130_1438'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'default_permissions': ('add', 'change', 'delete', 'view'), 'ordering': ['departmentmname'], 'verbose_name': 'Департамент', 'verbose_name_plural': 'Департаменты'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'default_permissions': ('add', 'change', 'delete', 'view'), 'ordering': ['title'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterModelOptions(
            name='subdevision',
            options={'default_permissions': ('add', 'change', 'delete', 'view'), 'ordering': ['subdevisionname'], 'verbose_name': 'Отдел', 'verbose_name_plural': 'Отделы'},
        ),
        migrations.AlterModelOptions(
            name='technic',
            options={'default_permissions': ('add', 'change', 'delete', 'view'), 'ordering': ['technic_id'], 'verbose_name': 'Техника', 'verbose_name_plural': 'Техника'},
        ),
    ]
