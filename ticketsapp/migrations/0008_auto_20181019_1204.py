# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-19 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketsapp', '0007_auto_20181019_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='performer',
            field=models.CharField(default=None, max_length=30, null=True, verbose_name='Исполнитель'),
        ),
    ]
