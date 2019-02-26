from django.db import models
from mainapp.models import Technic


class CMTModel(models.Model):
    computermodelname = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Модели КМТ'
        verbose_name_plural = 'Список моделей КМТ'

    def __str__(self):
        return self.computermodelname


class CMT(Technic):
    name = models.CharField('Имя', max_length=200)
    netbiosname = models.CharField('NETBIOS-имя', max_length=200)
    ip = models.GenericIPAddressField('IP-адрес')
    macaddress = models.CharField('MAC-адрес', max_length=30)
    cmtmodel = models.ForeignKey('CMTModel', on_delete=models.PROTECT, verbose_name='Модель',related_name='+')


    class Meta:
        permissions = (
        ('can_view_workstationslist', 'Может просматривать список КМТ'),
        ('can_add_workstations', 'Может добавлять КМТ'),
        ('can_edit_workstations', 'Может изменять карточки КМТ'),
        ('can_delete_workstations', 'Может удалять карточки КМТ'),
        )
        verbose_name = 'КМТ'
        verbose_name_plural = 'КМТ'


    def __str__(self):
        return self.name
