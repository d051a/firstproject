from django.db import models
from mainapp.models import Technic
from django.contrib.auth.models import Group

class Token(Technic):
    name = models.CharField('Имя токена', max_length=20)

    class Meta:
        permissions = (
            ('can_view_tokens', 'Может просматривать список токенов'),
            ('can_add_tokens', 'Может добавлять токенов'),
            ('can_delete_tokens', 'Может удалять токенов'),
            ('can_somethings_tokens', 'Может еще что-то'),
        )
        ordering = ['name']
        verbose_name = 'Токен'
        verbose_name_plural = 'Токены'

    def __str__(self):
        return self.name
