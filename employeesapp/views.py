from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView
from .forms import EmployeeForm, PostForm
from .models import Employee, Post
from authapp.forms import UserCreateForm
from ACCOUNTING.generic.mixins import ContextPageMixin

class EmployeeListView(ContextPageMixin, ListView):
    template_name = 'employeesapp/list_employees.html'
    model = Employee
    context_object_name = 'employeelist'
    pagename = 'Все сотрудники'


class EmployeeEditView(ContextPageMixin, UpdateView):
    template_name = 'employeesapp/edit_employee.html'
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy('employeesapp:list_employees')
    pagename = 'Изменить данные сотрудника'


class TelephoneBookView(ContextPageMixin, ListView):
    template_name = 'employeesapp/telephone_book.html'
    model = Employee
    context_object_name = 'employeelist'
    pagename = 'Телефонный справочник'


class BirthdaysListView(ContextPageMixin, ListView):
    template_name = 'employeesapp/birthdays.html'
    model = Employee
    context_object_name = 'employeelist'
    pagename = 'Дни рождения сотрудников'


class PostListView(ContextPageMixin, ListView):
    template_name = 'employeesapp/list_posts.html'
    model = Post
    context_object_name = 'postslist'
    pagename = 'Все должности'


class PostEditView(ContextPageMixin, UpdateView):
    template_name = 'employeesapp/edit_post.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('employeesapp:list_posts')
    pagename = 'Изменение должности'


class PostAddView(ContextPageMixin, CreateView):
    template_name = 'employeesapp/add_post.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('employeesapp:list_posts')
    pagename = 'Новая должность'


def register_user(request):
    if request.method == 'POST':
        user_form = UserCreateForm(request.POST)
        employee_form = EmployeeForm(request.POST)
        if user_form.is_valid() and employee_form.is_valid():
            user = user_form.save()
            employee = employee_form.save(commit=False)
            employee.user_id = user.id
            employee.save()
            messages.success(request, 'Ваш профиль был успешно обновлен!')
            return reverse_lazy('employeesapp:add_employee')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки.')
    else:
        user_form = UserCreateForm()
        employee_form = EmployeeForm()
    return render(request, 'employeesapp/add_employee.html', {
        'form': user_form,
        'employee_form': employee_form
    })
