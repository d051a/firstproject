# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-25 18:59
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
                ('technic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mainapp.Technic')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('ip', models.CharField(max_length=50, verbose_name='Ip-адрес')),
            ],
            options={
                'verbose_name': 'Сервер',
                'verbose_name_plural': 'Серверы',
                'ordering': ['name'],
                'permissions': (('can_view_serverslist', 'Может просматривать список серверов'), ('can_add_servers', 'Может добавлять серверы'), ('can_edit_servers', 'Может изменять карточки серверов'), ('can_delete_servers', 'Может удалять карточки серверов')),
            },
            bases=('mainapp.technic',),
        ),
    ]
