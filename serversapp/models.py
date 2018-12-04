import uuid
from django.db import models
from mainapp.models import Technic

# Create your models here.
class Server (models.Model):
    technic_id = models.OneToOneField(
        Technic,
        on_delete=models.CASCADE,)
    ip = models.CharField('Ip-адрес', max_length=50,)
    name = models.CharField('Имя', max_length=50,)

    class Meta:
        ordering = ['name']
        verbose_name = 'Сервер'
        verbose_name_plural = 'Серверы'

    def __str__(self):
        return self.name
