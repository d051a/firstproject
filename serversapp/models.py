import uuid
from django.db import models

# Create your models here.
class Server (models.Model):
    technic_id = models.AutoField(primary_key=True,)
    ip = models.CharField(max_length=50,
            help_text = 'Ip-адрес',)
    name = models.CharField(max_length=50,
                help_text = 'Имя',)
    class Meta: #настройка вывода данных
        ordering = ['name'] #сортировка записей по полю. "-" - сортировка с конца
        verbose_name = 'Сервер' #вывод названия модели в единственном числе
        verbose_name_plural = 'Серверы' #вывод названия модели в единственном числе

    def __str__(self):
        return self.name
