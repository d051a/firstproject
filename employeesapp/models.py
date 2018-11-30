from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from mainapp.models import Department, SubDevision
from ACCOUNTING.settings import MEDIA_ROOT

class Employee(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE)
    fio = models.CharField(
        'Фамилия Имя Отчество',
        max_length=30,
        blank=True)
    birthdate = models.DateField(
        'Дата рождения',
        null=True,
        blank=True)
    telephonenum = models.CharField(
        'Телефонный номер',
        max_length=10,
        blank=True)
    telephonenum2 = models.CharField(
        'Телефонный номер#2',
        max_length=10,
        blank=True)
    location = models.CharField(
        'Номер кабинета',
        max_length=30,
        blank=True)
    department = models.ForeignKey(
        'mainapp.Department',
        verbose_name='Управление',
        default=None)
    subdevision = models.ForeignKey(
        'mainapp.SubDevision',
        verbose_name='Отдел',
        default=None)
    post = models.ForeignKey(
        'Post',
        null=True,
        verbose_name='Должность')
    img = models.ImageField(upload_to=MEDIA_ROOT,
        null=True,
        blank=True)

    class Meta:
        ordering = ['fio']
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.fio


class Post(models.Model):
    postname = models.CharField(
        'Должность',
        max_length=75,)
    class Meta:
        ordering = ['postname']
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.postname
