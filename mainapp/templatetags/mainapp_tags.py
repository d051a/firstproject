import datetime
from django import template
from ticketsapp.models import Ticket

register = template.Library()

@register.simple_tag
def tickets_count(user_id, status):
    tickets_inwork_count = Ticket.objects.filter(performer_id=user_id).filter(status='INWORK').count()
    tickets_open_count = Ticket.objects.filter(performer_id=user_id).filter(status='OPEN').count()
    all_tickets_count = tickets_inwork_count + tickets_open_count
    if status == 'INWORK':
        return tickets_inwork_count
    elif status == 'OPEN':
        return tickets_open_count
    elif status == 'ALL':
        return all_tickets_count
