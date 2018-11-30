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
    technic_id = models.AutoField(
        primary_key=True,)
    inventorynum1 = models.CharField(
        'Инвентарный номер#1',
        max_length=50,
        blank=True,)
    inventorynum2 = models.CharField(
        'Инвентарный номер#2',
        max_length=50,
        blank=True,)
    serialnum = models.CharField(
        'Серийный номер',
        max_length=50,
        blank=True,)
    technictype = models.CharField(
        'Тип техники',
        max_length=50,
        blank=False,
        choices=TECHNICTYPES,)

    class Meta:
        ordering = ['technic_id']
        verbose_name = 'Техника'
        verbose_name_plural = 'Техника'

    def __str__(self):
        return '{} {}'.format(self.technic_id, self.technictype)


class Department(models.Model):
    departmentmname = models.CharField(
        'Департамент',
        max_length=100,
        null=True)

    class Meta:
        ordering = ['departmentmname']
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'

    def __str__(self):
        return self.departmentmname


class SubDevision(models.Model):
    department = models.ForeignKey(
        Department,
        verbose_name='Департамент',
        on_delete=models.CASCADE,
        default=None)
    subdevisionname = models.CharField(
        'Отдел',
        max_length=100,
        null=True)

    class Meta:
        ordering = ['subdevisionname']
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.subdevisionname


class News (models.Model):
    NEWSTYPE = (('Главные', 'MAIN'),
                ('Побочные', 'SECOND'))
    title = models.CharField('Заголовок', max_length=50, null=False)
    content = models.CharField('Контент', max_length=1000, null=False)
    type = models.CharField('Тип новости', max_length=50, null=False, choices=NEWSTYPE)
    datetime = models.DateTimeField('Дата и время создания', auto_now_add=True)
    class Meta:
        ordering = ['title']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title
