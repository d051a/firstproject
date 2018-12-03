from django.db import models


class ComputerModel(models.Model):

    computermodel_id = models.AutoField(primary_key=True)
    computermodelname = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Модель компьютера'
        verbose_name_plural = 'Модели компьютера'
        default_permissions = ('add', 'change', 'delete', 'view')

    def __str__(self):
        return self.computermodelname


class Computer(models.Model):
    inventorynum = models.CharField(max_length=12)
    serialnum = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    netbiosname = models.CharField(max_length=200)
    ip = models.GenericIPAddressField()
    macaddress = models.CharField(max_length=30)
    computermodelname = models.ForeignKey(ComputerModel, on_delete=models.PROTECT, related_name='+')
    computermodel_id = models.ForeignKey(ComputerModel, on_delete=models.PROTECT, related_name='+')
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Компьютер'
        verbose_name_plural = 'Компьютеры'
        default_permissions = ('add', 'change', 'delete', 'view')

    def __str__(self):
        return self.name
