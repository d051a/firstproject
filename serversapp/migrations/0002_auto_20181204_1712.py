# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-04 14:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serversapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='server',
            options={'ordering': ['name'], 'permissions': (('can_view_serverslist', 'Может просматривать список серверов'), ('can_add_servers', 'Может добавлять серверы'), ('can_edit_servers', 'Может изменять карточки серверов'), ('can_delete_servers', 'Может удалять карточки серверов')), 'verbose_name': 'Сервер', 'verbose_name_plural': 'Серверы'},
        ),
    ]
