# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-04 11:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ['-timestarted'], 'permissions': (('can_view_allticketslist', 'Может просматривать все заявки'), ('can_view_myticketslist', 'Может просматривать свои заявки'), ('can_view_imperformer_ticketslist', 'Может просматривать назначенные заявки'), ('can_add_tickets', 'Может добавлять заявки'), ('can_edit_all_tickets', 'Может изменять все заявки'), ('can_edit_my_tickets', 'Может изменять свои заявки'), ('can_delete_my_tickets', 'Может удалять свои заявки')), 'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
    ]
