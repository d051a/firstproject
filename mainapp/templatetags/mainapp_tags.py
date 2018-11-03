import datetime
from django import template
from ticketsapp.models import Ticket
from employeesapp.models import Employee

register = template.Library()


@register.simple_tag
def tickets_all_count(user_id):
    user = Employee.objects.get(user__exact=user_id).id
    tickets_inwork_count = Ticket.objects.filter(performer__exact=user).filter(status__exact='INWORK').count()
    tickets_open_count = Ticket.objects.filter(performer__exact=user).filter(status__exact='OPEN').count()
    #print('profile={}, user ={}, all_tickets_count ={}, tickets_inwork_count ={},tickets_open_count ={}'.format(profile, user, all_tickets_count, tickets_inwork_count,tickets_open_count))
    return tickets_inwork_count + tickets_open_count

@register.simple_tag
def tickets_inwork_count(user_id):
    user = Employee.objects.get(user__exact=user_id).id
    tickets_inwork_count = Ticket.objects.filter(performer__exact=user).filter(status__exact='INWORK').count()
    #print('profile={}, user ={}, all_tickets_count ={}, tickets_inwork_count ={},tickets_open_count ={}'.format(profile, user, all_tickets_count, tickets_inwork_count,tickets_open_count))
    return tickets_inwork_count


@register.simple_tag
def tickets_open_count(user_id):
    user = Employee.objects.get(user__exact=user_id).id
    tickets_open_count = Ticket.objects.filter(performer__exact=user).filter(status__exact='OPEN').count()
    #print('profile={}, user ={}, all_tickets_count ={}, tickets_inwork_count ={},tickets_open_count ={}'.format(profile, user, all_tickets_count, tickets_inwork_count,tickets_open_count))
    return tickets_open_count
