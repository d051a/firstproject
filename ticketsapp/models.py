from django.db import models

# Create your models here.
class Ticket(models.Model):
    STATUSES = (
        ('OPEN', 'Открыта'),
        ('INWORK', 'В работе'),
        ('CLOSED', 'Закрыта'),)
    PRIORITY = (
        ('LOW', 'Низкий'),
        ('NORMAL', 'Обычный'),
        ('HIGH', 'Высокий'),)
    status = models.CharField('Статус заявки', max_length=50,
        blank=False,
        choices=STATUSES,)
    priority = models.CharField('Приоритет', max_length=50,
            blank=False,
            choices=PRIORITY,)
    description = models.CharField('Описание проблемы', max_length=300)
    timestarted = models.DateTimeField('Дата и время подачи заявки', auto_now_add=True)
    timeclosed = models.DateTimeField('Дата и время закрытия заявки',)
    mainproblem = models.ForeignKey(
        'MainProblem', default=None)
    subproblem = models.ForeignKey(
            'SubProblem', default=None)


class MainProblem(models.Model):
    mainproblemname = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.mainproblemname


class SubProblem(models.Model):
    mainproblem = models.ForeignKey(MainProblem, on_delete=models.CASCADE, default=None)
    subproblemname = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.subproblemname
