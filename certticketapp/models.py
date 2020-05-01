from django.db import models
from django.core.validators import RegexValidator


class CertTicketModel(models.Model):
    created_time = models.DateField('Дата добавления', auto_now_add=True)
    surname = models.CharField('Фамилия', max_length=50)
    name = models.CharField('Имя', max_length=50)
    middle_name = models.CharField('Отчество', max_length=50)
    birthday = models.DateField('Дата рождения')
    place_of_birth = models.CharField('Место рождения', max_length=50)
    INN = models.CharField('ИНН',
            validators=[RegexValidator(regex='^.{12}$', message='Длина ИНН должна быть 12 знаков', code='nomatch')],
            max_length=12)
    SNILS = models.CharField('СНИЛС',
            validators=[RegexValidator(regex='^.{11}$', message='Длина СНИЛС должна быть 11 знаков', code='nomatch')],
            max_length=11)
    email = models.EmailField('E-mail')
    region = models.CharField('Регион', max_length=50)
    passport_series = models.CharField('Серия паспорта',
            validators=[RegexValidator(regex='^.{4}$', message='Серия паспорта должна быть 4 знака', code='nomatch')],
            max_length=4)
    passport_num = models.CharField('Номер паспорта',
            validators=[RegexValidator(regex='^.{6}$', message='Номер паспорта должен быть 6 знаков', code='nomatch')],
            max_length=6)
    passport_date = models.DateField('Дата выдачи')
    passport_unit_code = models.CharField('Код подразделения',
            validators=[RegexValidator(regex='^.{7}$', message='Код подразделения(ХХХ-ХХХ) должен быть 7 знаков', code='nomatch')],
            max_length=7)
    passport_issued_by = models.CharField('Кем выдан', max_length=150)
    registration_address = models.CharField('Адрес регистрации', max_length=250)
    position = models.CharField('Должность', max_length=100)
    code_word = models.CharField('Произвольное кодовое слово', max_length=20)

    class Meta:
        permissions = (
            ('can_view_certticketslist', 'Может просматривать все заявки на сертификаты'),
            ('can_view_mycertticketslist', 'Может просматривать свои заявки'),
            ('can_add_certtickets', 'Может добавлять заявки'),
            ('can_edit_all_certtickets', 'Может изменять все заявки'),
            ('can_edit_my_certtickets', 'Может изменять свои заявки'),
            ('can_delete_my_certtickets', 'Может удалять свои заявки'),
        )
        ordering = ['created_time']
        verbose_name = 'Заявка на выдачу сертификата'
        verbose_name_plural = 'Заявки на выдачу сертификатов'

    def __str__(self):
        return '{} {} {} {}'.format(self.created_time, self.name, self.name, self.middle_name)

class Template(models.Model):
    TEMPLATE_TYPE_CHOICES = (
        ('1', 'Доверенность'),
        ('2', 'Согласие'),
    )
    type = models.CharField('Тип шаблона',
                            max_length=2,
                            choices=TEMPLATE_TYPE_CHOICES,
                            default='2')
    name = models.CharField('Название шаблона', max_length=100)
    date_time = models.DateTimeField('Дата добавления', auto_now_add=True)
    file = models.FileField('Файл шаблона')

    class Meta:
        permissions = (
            ('can_add_certtickets_temlates', 'Может добавлять шаблоны'),
            ('can_delete_certtickets_temlates', 'Может удалять шаблоны'),
        )
        verbose_name = 'Шаблон документа'
        verbose_name_plural = 'Шаблоны документов'


    def __str__(self):
        return self.name


