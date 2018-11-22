from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, CreateView, UpdateView
from .forms import TicketForm, EditTicketForm, MainProblemForm, SubProblemForm
from .models import Ticket, SubProblem, MainProblem
from django.urls import reverse_lazy
from employeesapp.models import Employee
from ACCOUNTING.generic.mixins import ContextPageMixin

class TicketListView(ContextPageMixin, ListView):
    template_name = 'ticketsapp/list_tickets.html'
    model = Ticket
    context_object_name = 'ticketslist'
    pagename = 'Все заявки'


class UserTicketListView(ContextPageMixin, ListView):
    template_name = 'ticketsapp/list_tickets.html'
    model = Ticket
    context_object_name = 'ticketslist'
    pagename = 'Мои заявки'

    def get_queryset(self):
        user = Employee.objects.get(user__exact=self.request.user.id)
        object_list = super(UserTicketListView, self).get_queryset()
        object_list = Ticket.objects.filter(performer__exact=user)
        return object_list


class TicketEditView(ContextPageMixin, UpdateView):
    template_name = 'ticketsapp/edit_ticket.html'
    model = Ticket
    form_class = EditTicketForm
    success_url = '/tickets'
    pagename = 'Изменение заявки'


class TicketAddView(ContextPageMixin, CreateView):
    template_name = 'ticketsapp/add_ticket.html'
    model = Ticket
    form_class = TicketForm
    success_url = '/tickets'
    pagename = 'Новая заявка'

    def form_valid(self, form):
        form.instance.userhostname = self.request.META['REMOTE_ADDR']
        try:
            form.instance.employee_start = Employee.objects.get(user__exact=self.request.user.id)
        except:
            form.instance.employee_start = None
        return super(TicketAddView, self).form_valid(form)


class MainProblemListView(ContextPageMixin, ListView):
    template_name = 'ticketsapp/list_mainproblems.html'
    model = MainProblem
    context_object_name = 'mainproblemslist'
    pagename = 'Все типовые проблемы'


class MainProblemEditView(ContextPageMixin, UpdateView):
    template_name = 'ticketsapp/edit_mainproblem.html'
    model = MainProblem
    form_class = MainProblemForm
    success_url = reverse_lazy('ticketsapp:list_problems')
    pagename = 'Измененение типовой проблемы'


class MainProblemAddView(ContextPageMixin, CreateView):
    template_name = 'ticketsapp/add_mainproblem.html'
    model = MainProblem
    form_class = MainProblemForm
    success_url = reverse_lazy('ticketsapp:list_problems')
    pagename = 'Новая типовая проблема'


class SubProblemListView(ContextPageMixin, ListView):
    template_name = 'ticketsapp/list_subproblems.html'
    model = SubProblem
    context_object_name = 'subproblemlist'
    pagename = 'Все'


class SubProblemEditView(ContextPageMixin, UpdateView):
    template_name = 'ticketsapp/edit_subproblem.html'
    model = SubProblem
    form_class = SubProblemForm
    success_url = reverse_lazy('ticketsapp:list_subproblems')
    pagename = 'Измененить проблему'


class SubProblemAddView(ContextPageMixin, CreateView):
    template_name = 'ticketsapp/add_subproblem.html'
    model = SubProblem
    form_class = SubProblemForm
    success_url = reverse_lazy('ticketsapp:list_subproblems')
    pagename = 'Новая проблема :)'
