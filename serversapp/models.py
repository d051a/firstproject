import uuid
from django.db import models
from mainapp.models import Technic
from employeesapp.models import Employee
from mainapp.models import Technic

# Create your models here.
class Server (Technic):
    name = models.CharField('Имя', max_length=50)
    ip = models.CharField('Ip-адрес', max_length=50)

    class Meta:
        permissions = (
        ('can_view_serverslist', 'Может просматривать список серверов'),
        ('can_add_servers', 'Может добавлять серверы'),
        ('can_edit_servers', 'Может изменять карточки серверов'),
        ('can_delete_servers', 'Может удалять карточки серверов'),
        )
        ordering = ['name']
        verbose_name = 'Сервер'
        verbose_name_plural = 'Серверы'

    def __str__(self):
        return self.name
