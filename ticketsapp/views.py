from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import TicketForm
from .models import Ticket

def list_tickets(request):
    pagename = 'Все заявки'
    ticketslist = Ticket.objects.all()
    return render(request, 'ticketsapp/list_tickets.html', {
        'pagename': pagename,
        'ticketslist': ticketslist,
        })


def add_ticket(request):
    pagename = 'Новая заявка'
    if request.method == 'POST':
        ticketform = TicketForm(request.POST)
        if ticketform.is_valid():
            ticketform.save()
            return HttpResponseRedirect('/tickets')
    else:
        ticketform = TicketForm()
    return render(request, 'ticketsapp/add_ticket.html', {'pagename': pagename,
                                                    'ticketform': ticketform})


def edit_ticket(request):
    pagename = 'Изменить заявку'
    return render(request, 'ticketsapp/edit_ticket.html', {'pagename': pagename})
