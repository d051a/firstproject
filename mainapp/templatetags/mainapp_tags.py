import datetime
from django import template
from ticketsapp.models import Ticket
from employeesapp.models import Employee

register = template.Library()


@register.simple_tag
def all_tickets_count(user_id):
    try:
        user = Employee.objects.get(user__exact=user_id).id
        tickets_inwork_count = Ticket.objects.filter(
            performer__exact=user).filter(status__exact='INWORK').count()
        tickets_open_count = Ticket.objects.filter(
            performer__exact=user).filter(status__exact='OPEN').count()
        return tickets_inwork_count + tickets_open_count
    except:
        print('У этого пользователя нет записи в Employee. Заявок - 0')
        return 0


@register.simple_tag
def inwork_tickets_count(user_id):
    try:
        user = Employee.objects.get(user__exact=user_id).id
        tickets_inwork_count = Ticket.objects.filter(
            performer__exact=user).filter(status__exact='INWORK').count()
        return tickets_inwork_count
    except:
        print('У этого пользователя нет записи в Employee. Заявок - 0')
        return 0



@register.simple_tag
def open_tickets_count(user_id):
    try:
        user = Employee.objects.get(user__exact=user_id).id
        tickets_open_count = Ticket.objects.filter(
            performer__exact=user).filter(status__exact='OPEN').count()
        return tickets_open_count
    except:
        print('У этого пользователя нет записи в Employee. Заявок - 0')
        return 0
