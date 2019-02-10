from django.db import models


class WorkstationModel(models.Model):
    computermodelname = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Модель компьютера'
        verbose_name_plural = 'Список моделей компьютеров'

    def __str__(self):
        return self.computermodelname


class Workstation(models.Model):
    inventorynum = models.CharField(verbose_name='Инвентарный номер', max_length=12)
    serialnum = models.CharField(verbose_name='Серийный номер', max_length=20)
    name = models.CharField(verbose_name='Имя компьютера', max_length=200)
    netbiosname = models.CharField(verbose_name='NETBIOS-имя', max_length=200)
    ip = models.GenericIPAddressField(verbose_name='IP-адрес')
    macaddress = models.CharField(verbose_name='MAC-адрес', max_length=30)
    computermodelname = models.ForeignKey('WorkstationModel', on_delete=models.PROTECT, related_name='+')
    created_at = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True)
    modified = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

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
