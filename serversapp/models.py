import uuid
from django.db import models
from mainapp.models import Technic
from employeesapp.models import Employee

# Create your models here.
class Server (models.Model):
    technic_id = models.OneToOneField(
        Technic,
        on_delete=models.CASCADE,)
    ip = models.CharField('Ip-адрес', max_length=50,)
    name = models.CharField('Имя', max_length=50,)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, verbose_name='Ответственный', blank=True, null=True)

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
