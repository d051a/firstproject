from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField('Имя',max_length=30, blank=True)
    lastname = models.CharField('Фамилия', max_length=30, blank=True)
    patronymic = models.CharField('Отчество',max_length=30, blank=True)
    birthdate = models.DateField('Дата рождения',null=True, blank=True)
    telephonenum = models.CharField('Телефонный номер',max_length=10, blank=True)
    telephonenum2 = models.CharField('Телефонный номер#2',max_length=10, blank=True)
    location = models.CharField('Номер кабинета',max_length=30, blank=True)
