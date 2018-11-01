# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-30 14:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employeesapp', '0008_auto_20181030_1720'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['postname'], 'verbose_name': 'Должность', 'verbose_name_plural': 'Должности'},
        ),
        migrations.AddField(
            model_name='employee',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employeesapp.Post', verbose_name='Должность'),
        ),
    ]