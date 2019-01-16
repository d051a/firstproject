from django.db import models


class News (models.Model):
    NEWSTYPE = (('Основные новости', 'Основные новости'),
                ('Новости портала', 'Новости портала'),
                ('Стенгазета', 'Стенгазета'))
    title = models.CharField('Заголовок', max_length=200, null=False)
    description = models.TextField('Краткое описание', max_length=10000, null=True)
    content = models.TextField('Контент', max_length=10000, null=False)
    type = models.CharField('Тип новости', max_length=50, null=False, choices=NEWSTYPE)
    datetime = models.DateTimeField('Дата и время создания', auto_now_add=True)

    class Meta:
        ordering = ['-datetime']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title
