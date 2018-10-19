# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-19 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketsapp', '0004_auto_20181018_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='employee_start',
            field=models.CharField(default='Иванов И.И.', max_length=300, verbose_name='Подал заявку'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='performer',
            field=models.CharField(default=None, max_length=300, verbose_name='Исполнитель'),
        ),
    ]
