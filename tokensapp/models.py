from django.db import models
from mainapp.models import Technic
# Create your models here.

class Token(Technic):
    name = models.CharField('Имя токена', max_length=20)

    def __str__(self):
        return self.name

    class Meta():
        ordering = ['name']
        verbose_name = 'Токен'
        verbose_name_plural = 'Токены'
