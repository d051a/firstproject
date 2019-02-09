from django.db import models

# Create your models here.
class Certificate(models.Model):
    fullname = models.CharField('ФИО:', max_length = 100, default=None)
    adddate = models.DateField('Дата добавления:', auto_now_add = True)
    validate_start_date = models.DateField('Срок начала действия сертификата:', null=True, blank=True)
    validate_end_date = models.DateField('Срок окончания действия сертификата:', null=True, blank=True)
    cert_file = models.FileField('Файл сертификата:', upload_to='certfiles', default=None, null=True, blank=True)
    email = models.EmailField('Email:', max_length = 50, default=None)
    persone = models.ForeignKey('Persone', verbose_name = 'Сертификаты:', default = None)
    class Meta:
        ordering = ['validate_end_date']
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'

    def __str__(self):
        return self.fullname + str(self.validate_end_date)

class Persone (models.Model):
    fullname = models.CharField('ФИО:', max_length = 100, unique = True)
    inn = models.CharField('ИНН:', max_length = 12)
    snils = models.CharField('СНИЛС:', max_length = 11)

    class Meta:
        ordering = ['fullname']
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'

    def __str__(self):
        return self.fullname
