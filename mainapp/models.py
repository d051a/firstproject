from django.db import models
from serversapp.models import Server

class Technic (models.Model):
    TECHNICTYPES = (
        ('CMT', 'КМТ'),
        ('SERVER', 'Сервер'),
        ('WORKSTATION', 'Компьютер'),
        ('CERT', 'Сертификат'),
        ('FLASH', 'Флеш-накопитель'),
        ('TOKEN', 'Токен'),
    )

    inventorynum1 = models.CharField('Инвентарный номер#1',max_length=50, blank=True,)
    inventorynum2 = models.CharField('Инвентарный номер#2', max_length=50, blank=True,)
    serialnum = models.CharField('Серийный номер', max_length=50, blank=True,)
    technic = models.OneToOneField(
        Server,
        on_delete=models.CASCADE,)
    technictype = models.CharField('Тип техники', max_length=50,
        blank=False,
        choices=TECHNICTYPES,)

    class Meta:
        ordering = ['id']
        verbose_name = 'Техника'
        verbose_name_plural = 'Техника'

    def __str__(self):
        return '{} {} {}'.format(self.id, self.technictype, self.technic.name)
