from django.db import models
from mainapp.models import Technic


class WorkstationModel(models.Model):
    computermodelname = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Модель компьютера'
        verbose_name_plural = 'Список моделей компьютеров'

    def __str__(self):
        return self.computermodelname


class Workstation(Technic):
    name = models.CharField('Имя компьютера', max_length=200)
    netbios_name = models.CharField('NETBIOS-имя', max_length=200)
    ip_address = models.GenericIPAddressField('IP-адрес')
    mac_address = models.CharField('MAC-адрес', max_length=30)
    model_name = models.ForeignKey('WorkstationModel', on_delete=models.PROTECT, verbose_name='Модель')

    class Meta:
        permissions = (
        ('can_view_workstationslist', 'Может просматривать список компьютеров'),
        ('can_add_workstations', 'Может добавлять компьютер'),
        ('can_edit_workstations', 'Может изменять карточки компьютеров'),
        ('can_delete_workstations', 'Может удалять карточки компьютеров'),
        )
        verbose_name = 'Компьютер'
        verbose_name_plural = 'Список компьютеров'


    def __str__(self):
        return self.name
