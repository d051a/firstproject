from django.db import models
from serversapp.models import Server

class Tehnic (models.Model):
    TECHNICTYPES = (
        ('CMT', 'КМТ'),
        ('SERVER', 'Сервер'),
        ('WORKSTATION', 'Компьютер'),
        ('CERT', 'Сертификат'),
        ('FLASH', 'Флеш-накопитель'),
        ('TOKEN', 'Токен'),
    )

    inventorynum1 = models.CharField(max_length=50,
        help_text = 'Инвентарный номер#1',)
    inventorynum2 = models.CharField(max_length=50,
        help_text = 'Инвентарный номер#2',)
    serialnum = models.CharField(max_length=50,
        help_text = 'Серийный номер',)
    tecnic = models.OneToOneField(
        Server,
        on_delete=models.CASCADE,)
    technictype = models.CharField(max_length=50,
        default = 'CMT',
        help_text = 'Тип техники',
        choices=TECHNICTYPES,)

    class Meta:
        ordering = ['id']
        verbose_name = 'Техника'
        verbose_name_plural = 'Техника'

    def __str__(self):
        return str(self.id) + str(Server.name)
