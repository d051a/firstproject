from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView
from .forms import TicketForm, EditTicketForm
from .models import Ticket

def list_tickets(request):
    pagename = 'Все заявки'
    ticketslist = Ticket.objects.all()
    return render(request, 'ticketsapp/list_tickets.html', {
        'pagename': pagename,
        'ticketslist': ticketslist,
        })

class TicketEditView(UpdateView):
    template_name = 'ticketsapp/edit_ticket.html'
    model = Ticket
    form_class = EditTicketForm
    success_url = '/tickets'

class TicketAddView(UpdateView):
    template_name = 'ticketsapp/add_ticket.html'
    model = Ticket
    form_class = TicketForm
    success_url = '/tickets'


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


def edit_ticket(request, ticket_id):
    pagename = 'Изменить заявку'
    ticket = Ticket.objects.get(pk=ticket_id)
    data = {'status': ticket.status,
            'priority': ticket.priority,
            'description': ticket.description,
            'mainproblem': ticket.mainproblem,
            'subproblem': ticket.subproblem,
            'performer': ticket.performer,
            }
    ticketform = EditTicketForm(data)
    return render(request, 'ticketsapp/edit_ticket.html', {
            'pagename': pagename,
            'ticketform': ticketform})


def load_subproblems(request):
    mainmproblem_id = request.GET.get('mainproblem')
    subproblem = SubProblem.objects.filter(mainmproblem_id=mainmproblem_id).order_by('subproblemname')
    return render(request,)
