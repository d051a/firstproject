from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .forms import EmployeeForm, PostForm
from .models import Employee, Post



class EmployeeListView(ListView):
    template_name = 'employeesapp/list_employees.html'
    model = Employee
    context_object_name = 'employeelist'

def list_employees(request):
    pagename = 'Все'
    return render(request, 'employeesapp/list_employees.html', {
        'pagename': pagename})


def add_employee(request):
    pagename = 'Новый сотрудник'
    return render(request, 'employeesapp/add_employee.html', {
        'pagename': pagename})


def edit_employee(request):
    pagename = 'Изменить данные сотрудника'
    return render(request, 'employeesapp/edit_employee.html', {
        'pagename': pagename})

class TelephoneBookView(ListView):
    template_name = 'employeesapp/telephone_book.html'
    model = Employee
    context_object_name = 'employeelist'
    def get_context_data(self, **kwargs):
        context = super(TelephoneBookView, self).get_context_data(**kwargs)
        context['pagename'] = 'Телефонный справочник'
        return context

def telephone_book(request):
    pagename = 'Телефонный справочник'
    return render(request, 'employeesapp/telephone_book.html', {
        'pagename': pagename})


class BirthdaysListView(ListView):
    template_name = 'employeesapp/birthdays.html'
    model = Employee
    context_object_name = 'employeelist'

    def get_context_data(self, **kwargs):
        context = super(BirthdaysListView, self).get_context_data(**kwargs)
        context['pagename'] = 'Дни рождения сотрудников'
        return context


def birthdays(request):
    pagename = 'Дни рождения сотрудников'
    return render(request, 'employeesapp/birthdays.html', {
        'pagename': pagename})


class PostListView(ListView):
    template_name = 'employeesapp/list_posts.html'
    model = Post
    context_object_name = 'postslist'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['pagename'] = 'Все должности'
        return context


class PostEditView(UpdateView):
    template_name = 'employeesapp/edit_post.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('employeesapp:list_posts')

    def get_context_data(self, **kwargs):
        context = super(PostEditView, self).get_context_data(**kwargs)
        context['pagename'] = 'Изменение должности'
        return context


class PostAddView(CreateView):
    template_name = 'employeesapp/add_post.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('employeesapp:list_posts')

    def get_context_data(self, **kwargs):
        context = super(PostAddView, self).get_context_data(**kwargs)
        context['pagename'] = 'Новая должность'
        return context
