from django.db import models


class Ticket(models.Model):
    STATUSES = (
        ('OPEN', 'Открыта'),
        ('INWORK', 'В работе'),
        ('CLOSED', 'Выполнено'),)
    PRIORITY = (
        ('LOW', 'Низкий'),
        ('NORMAL', 'Обычный'),
        ('HIGH', 'Высокий'),)
    status = models.CharField(
        'Статус заявки',
        max_length=50,
        blank=False,
        choices=STATUSES,
        default='OPEN')
    priority = models.CharField(
        'Приоритет',
        max_length=50,
        blank=False,
        choices=PRIORITY,
        default='NORMAL')
    description = models.CharField(
        'Описание проблемы',
        max_length=300)
    note = models.CharField(
        'Примечание',
        max_length=300,
        null=True,
        blank=True,
        default='-')
    timestarted = models.DateTimeField(
        'Дата и время подачи заявки',
        auto_now_add=True)
    timeclosed = models.DateTimeField(
        'Дата и время закрытия заявки',
        null=True,)
    mainproblem = models.ForeignKey(
        'MainProblem',
        verbose_name='Типовая проблема',
        default=None)
    subproblem = models.ForeignKey(
        'SubProblem',
        verbose_name='Проблема',
        default=None)
    employee_start = models.ForeignKey(
        'employeesapp.Employee', null=True, related_name='employee_start', verbose_name='Отправитель',)
    performer = models.ForeignKey(
        'employeesapp.Employee', null=True, verbose_name='Исполнитель',)

    class Meta:
        ordering = ['-timestarted']
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.description


class MainProblem(models.Model):
    mainproblemname = models.CharField(
        'Типовая проблема',
        max_length=50,
        null=True)

    def __str__(self):
        return self.mainproblemname


class SubProblem(models.Model):
    mainproblem = models.ForeignKey(
        MainProblem,
        verbose_name='Типовая проблема',
        on_delete=models.CASCADE,
        default=None)
    subproblemname = models.CharField('Проблема', max_length=50, null=True)

    def __str__(self):
        return self.subproblemname
