from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView
from .forms import TicketForm, EditTicketForm
from .models import Ticket, SubProblem




class TicketListView(ListView):
    template_name = 'ticketsapp/list_tickets.html'
    model = Ticket
    context_object_name = 'ticketslist'
    def get_context_data(self, **kwargs):
            context = super(TicketListView, self).get_context_data(**kwargs)
            context['pagename'] = 'Все заявки'
            return context

class TicketEditView(UpdateView):
    template_name = 'ticketsapp/edit_ticket.html'
    model = Ticket
    form_class = EditTicketForm
    success_url = '/tickets'
    def get_context_data(self, **kwargs):
            context = super(TicketEditView, self).get_context_data(**kwargs)
            context['pagename'] = 'Изменение заявки'
            return context

class TicketAddView(CreateView):
    template_name = 'ticketsapp/add_ticket.html'
    model = Ticket
    form_class = TicketForm
    success_url = '/tickets'
    def get_context_data(self, **kwargs):
            context = super(TicketAddView, self).get_context_data(**kwargs)
            context['pagename'] = 'Новая заявка'
            return context


def load_subproblems(request):
    mainmproblem_id = request.GET.get('mainproblem')
    print(mainmproblem_id)
    subproblem = SubProblem.objects.filter(id=mainmproblem_id).order_by('subproblemname')
    return render(request,)
