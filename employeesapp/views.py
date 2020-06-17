from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView
from .forms import EmployeeForm, PostForm, EmployeeDisabledForm
from .models import Employee, Post
from mainapp.models import Technic
from authapp.forms import UserCreateForm
from ACCOUNTING.generic.mixins import ContextPageMixin
from django.db.models.functions import Extract


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
    pagename = 'Карточка сотрудника'

    def get_context_data(self, **kwargs):
        context = super(EmployeeEditView, self).get_context_data(**kwargs)
        usertechniclist = Technic.objects.filter(employee=self.kwargs['pk'])
        user_data = Employee.objects.get(pk=self.kwargs['pk'])
        print(user_data)
        context['usertechniclist'] = usertechniclist
        context['employee'] = user_data
        return context


class TelephoneBookView(ContextPageMixin, ListView):
    template_name = 'employeesapp/telephone_book.html'
    model = Employee
    context_object_name = 'employeelist'
    pagename = 'Телефонный справочник'


class TelephoneBookEmployee(ContextPageMixin, UpdateView):
    template_name = 'employeesapp/telephone_employee.html'
    model = Employee
    form_class = EmployeeDisabledForm
    pagename = 'Карточка сотрудника'
    success_url = reverse_lazy('employeesapp:telephone_book')


class BirthdaysListView(ContextPageMixin, ListView):
    template_name = 'employeesapp/birthdays.html'
    model = Employee
    context_object_name = 'employeelist'
    pagename = 'Дни рождения сотрудников'

    def get_queryset(self):
        object_list = super(BirthdaysListView, self).get_queryset()
        object_list = Employee.objects.annotate(
            month=Extract('birthdate', 'month'),
            day=Extract('birthdate', 'day')).order_by('month', 'day')
        return object_list


class BirthdaysEmployee(ContextPageMixin, UpdateView):
    template_name = 'employeesapp/birthdays_employee.html'
    model = Employee
    form_class = EmployeeDisabledForm
    pagename = 'Карточка сотрудника'
    success_url = reverse_lazy('employeesapp:telephone_book')


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
