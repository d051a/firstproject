# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-30 08:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_department_subdevision'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['departmentmname'], 'verbose_name': 'Департамент', 'verbose_name_plural': 'Департаменты'},
        ),
        migrations.AlterModelOptions(
            name='subdevision',
            options={'ordering': ['subdevisionname'], 'verbose_name': 'Отдел', 'verbose_name_plural': 'Отделы'},
        ),
    ]