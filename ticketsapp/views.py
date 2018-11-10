from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, CreateView, UpdateView
from .forms import TicketForm, EditTicketForm, MainProblemForm, SubProblemForm
from .models import Ticket, SubProblem, MainProblem
from django.urls import reverse_lazy
from employeesapp.models import Employee

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

    def form_valid(self, form):
        try:
            form.instance.employee_start = Employee.objects.get(user__exact=self.request.user.id)
        except:
            form.instance.employee_start = None
        return super(TicketAddView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(TicketAddView, self).get_context_data(**kwargs)
        context['pagename'] = 'Новая заявка'
        return context


class MainProblemListView(ListView):
    template_name = 'ticketsapp/list_mainproblems.html'
    model = MainProblem
    context_object_name = 'mainproblemslist'

    def get_context_data(self, **kwargs):
        context = super(MainProblemListView, self).get_context_data(**kwargs)
        context['pagename'] = 'Все типовые проблемы'
        return context


class MainProblemEditView(UpdateView):
    template_name = 'ticketsapp/edit_mainproblem.html'
    model = MainProblem
    form_class = MainProblemForm
    success_url = reverse_lazy('ticketsapp:list_problems')

    def get_context_data(self, **kwargs):
        context = super(MainProblemEditView, self).get_context_data(**kwargs)
        context['pagename'] = 'Измененение типовой проблемы'
        return context


class MainProblemAddView(CreateView):
    template_name = 'ticketsapp/add_mainproblem.html'
    model = MainProblem
    form_class = MainProblemForm
    success_url = reverse_lazy('ticketsapp:list_problems')

    def get_context_data(self, **kwargs):
        context = super(MainProblemAddView, self).get_context_data(**kwargs)
        context['pagename'] = 'Новая типовая проблема'
        return context


class SubProblemListView(ListView):
    template_name = 'ticketsapp/list_subproblems.html'
    model = SubProblem
    context_object_name = 'subproblemlist'

    def get_context_data(self, **kwargs):
        context = super(SubProblemListView, self).get_context_data(**kwargs)
        context['pagename'] = 'Все'
        return context


class SubProblemEditView(UpdateView):
    template_name = 'ticketsapp/edit_subproblem.html'
    model = SubProblem
    form_class = SubProblemForm
    success_url = reverse_lazy('ticketsapp:list_subproblems')

    def get_context_data(self, **kwargs):
        context = super(SubProblemEditView, self).get_context_data(**kwargs)
        context['pagename'] = 'Измененить проблему'
        return context


class SubProblemAddView(CreateView):
    template_name = 'ticketsapp/add_subproblem.html'
    model = SubProblem
    form_class = SubProblemForm
    success_url = reverse_lazy('ticketsapp:list_subproblems')

    def get_context_data(self, **kwargs):
        context = super(SubProblemAddView, self).get_context_data(**kwargs)
        context['pagename'] = 'Новая проблема :)'
        return context
