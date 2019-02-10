from django.db import models


class CMTModel(models.Model):
    computermodelname = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Модели КМТ'
        verbose_name_plural = 'Список моделей КМТ'

    def __str__(self):
        return self.computermodelname


class CMT (models.Model):
    inventorynum = models.CharField(verbose_name='Инвентарный номер', max_length=12)
    serialnum = models.CharField(verbose_name='Серийный номер', max_length=20)
    name = models.CharField(verbose_name='Имя компьютера', max_length=200)
    netbiosname = models.CharField(verbose_name='NETBIOS-имя', max_length=200)
    ip = models.GenericIPAddressField(verbose_name='IP-адрес')
    macaddress = models.CharField(verbose_name='MAC-адрес', max_length=30)
    cmtmodel = models.ForeignKey('CMTModel', on_delete=models.PROTECT, related_name='+')
    created_at = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True)
    modified = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

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
