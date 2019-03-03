from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import TicketForm, EditTicketForm, EditMyTicketForm, MainProblemForm, SubProblemForm
from .models import Ticket, SubProblem, MainProblem
from django.urls import reverse_lazy
from employeesapp.models import Employee
from ACCOUNTING.generic.mixins import ContextPageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class TicketListView(
        PermissionRequiredMixin,
        LoginRequiredMixin,
        ContextPageMixin,
        ListView):
    permission_required = 'ticketsapp.can_view_allticketslist'
    template_name = 'ticketsapp/list_tickets.html'
    model = Ticket
    context_object_name = 'ticketslist'
    pagename = 'Все заявки'


class UserPerformerTicketListView(
        PermissionRequiredMixin,
        LoginRequiredMixin,
        ContextPageMixin,
        ListView):
    permission_required = 'ticketsapp.can_view_imperformer_ticketslist'
    template_name = 'ticketsapp/list_tickets.html'
    model = Ticket
    context_object_name = 'ticketslist'
    pagename = 'Назначенные мне заявки'

    def get_queryset(self):
        user = Employee.objects.get(user__exact=self.request.user.id)
        # object_list = super(UserPerformerTicketListView, self).get_queryset()
        object_list = Ticket.objects.filter(performer__exact=user)
        return object_list


class UserTicketListView(
        PermissionRequiredMixin,
        LoginRequiredMixin,
        ContextPageMixin,
        ListView):
    permission_required = 'ticketsapp.can_view_myticketslist'
    template_name = 'ticketsapp/list_tickets.html'
    model = Ticket
    context_object_name = 'ticketslist'
    pagename = 'Мои заявки'

    def get_queryset(self):
        user = Employee.objects.get(user__exact=self.request.user.id)
        # object_list = super(UserTicketListView, self).get_queryset()
        object_list = Ticket.objects.filter(employee_start__exact=user)
        return object_list


class TicketEditView(LoginRequiredMixin, ContextPageMixin, UpdateView):
    template_name = 'ticketsapp/edit_ticket.html'
    model = Ticket
    form_class = EditTicketForm
    success_url = '/tickets'
    pagename = 'Изменение заявки'


class MyTicketEditView(LoginRequiredMixin, ContextPageMixin, UpdateView):
    template_name = 'ticketsapp/edit_ticket.html'
    model = Ticket
    form_class = EditMyTicketForm
    success_url = '/tickets/my/'
    pagename = 'Изменение заявки'


class TicketAddView(LoginRequiredMixin, ContextPageMixin, CreateView):
    template_name = 'ticketsapp/add_ticket.html'
    model = Ticket
    form_class = TicketForm
    success_url = '/tickets/my/'
    pagename = 'Новая заявка'

    def form_valid(self, form):
        form.instance.userhostname = self.request.META['REMOTE_ADDR']
        try:
            form.instance.employee_start = Employee.objects.get(
                user__exact=self.request.user.id)
        except:
            form.instance.employee_start = None
        return super(TicketAddView, self).form_valid(form)


class TicketDeleteView(LoginRequiredMixin, DeleteView):
    model = Ticket
    success_url = reverse_lazy('ticketsapp:list_tickets')


class MainProblemListView(LoginRequiredMixin, ContextPageMixin, ListView):
    template_name = 'ticketsapp/list_mainproblems.html'
    model = MainProblem
    context_object_name = 'mainproblemslist'
    pagename = 'Все типовые проблемы'


class MainProblemEditView(LoginRequiredMixin, ContextPageMixin, UpdateView):
    template_name = 'ticketsapp/edit_mainproblem.html'
    model = MainProblem
    form_class = MainProblemForm
    success_url = reverse_lazy('ticketsapp:list_problems')
    pagename = 'Измененение типовой проблемы'


class MainProblemAddView(LoginRequiredMixin, ContextPageMixin, CreateView):
    template_name = 'ticketsapp/add_mainproblem.html'
    model = MainProblem
    form_class = MainProblemForm
    success_url = reverse_lazy('ticketsapp:list_problems')
    pagename = 'Новая типовая проблема'


class SubProblemListView(LoginRequiredMixin, ContextPageMixin, ListView):
    template_name = 'ticketsapp/list_subproblems.html'
    model = SubProblem
    context_object_name = 'subproblemlist'
    pagename = 'Все'


class SubProblemEditView(LoginRequiredMixin, ContextPageMixin, UpdateView):
    template_name = 'ticketsapp/edit_subproblem.html'
    model = SubProblem
    form_class = SubProblemForm
    success_url = reverse_lazy('ticketsapp:list_subproblems')
    pagename = 'Измененить проблему'


class SubProblemAddView(LoginRequiredMixin, ContextPageMixin, CreateView):
    template_name = 'ticketsapp/add_subproblem.html'
    model = SubProblem
    form_class = SubProblemForm
    success_url = reverse_lazy('ticketsapp:list_subproblems')
    pagename = 'Новая проблема :)'
