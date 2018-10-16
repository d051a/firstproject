from django.db import models

class Technic (models.Model):
    TECHNICTYPES = (
        ('CMT', 'КМТ'),
        ('SERVER', 'Сервер'),
        ('WORKSTATION', 'Компьютер'),
        ('CERT', 'Сертификат'),
        ('FLASH', 'Флеш-накопитель'),
        ('TOKEN', 'Токен'),
    )
    technic_id = models.AutoField(primary_key=True,)
    inventorynum1 = models.CharField('Инвентарный номер#1',max_length=50, blank=True,)
    inventorynum2 = models.CharField('Инвентарный номер#2', max_length=50, blank=True,)
    serialnum = models.CharField('Серийный номер', max_length=50, blank=True,)
    technictype = models.CharField('Тип техники', max_length=50,
        blank=False,
        choices=TECHNICTYPES,)

    class Meta:
        ordering = ['technic_id']
        verbose_name = 'Техника'
        verbose_name_plural = 'Техника'

    def __str__(self):
        return '{} {}'.format(self.technic_id, self.technictype)
