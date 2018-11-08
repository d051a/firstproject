from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView
from .forms import EmployeeForm, PostForm
from .models import Employee, Post
from authapp.forms import UserCreateForm


class EmployeeListView(ListView):
    template_name = 'employeesapp/list_employees.html'
    model = Employee
    context_object_name = 'employeelist'
    def get_context_data(self, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        context['pagename'] = 'Все сотрудники'
        return context

class EmployeeEditView(UpdateView):
    template_name = 'employeesapp/edit_employee.html'
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy('employeesapp:list_employees')


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


class BirthdaysListView(ListView):
    template_name = 'employeesapp/birthdays.html'
    model = Employee
    context_object_name = 'employeelist'

    def get_context_data(self, **kwargs):
        context = super(BirthdaysListView, self).get_context_data(**kwargs)
        context['pagename'] = 'Дни рождения сотрудников'
        return context


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
