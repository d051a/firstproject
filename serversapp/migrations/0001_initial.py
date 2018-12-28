# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-26 14:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=50, verbose_name='Ip-адрес')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('technic_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Technic')),
            ],
            options={
                'verbose_name': 'Сервер',
                'verbose_name_plural': 'Серверы',
                'ordering': ['name'],
                'permissions': (('can_view_serverslist', 'Может просматривать список серверов'), ('can_add_servers', 'Может добавлять серверы'), ('can_edit_servers', 'Может изменять карточки серверов'), ('can_delete_servers', 'Может удалять карточки серверов')),
            },
        ),
    ]
