from django.views.generic import UpdateView
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import UserCreateForm
from employeesapp.forms import EmployeeForm
from employeesapp.models import Employee
from ACCOUNTING.generic.mixins import ContextPageMixin
from employeesapp.models import Employee


class LoginFormView(FormView):
    form_class = AuthenticationForm
    success_url = '/'
    template_name = 'authapp/login.html'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/auth/login/')


class RegisterFormView(FormView):
    template_name = 'authapp/registration_v2.html'
    def get(self, request, *args, **kwargs):
        user_form = UserCreateForm(request.POST)
        user_form.prefix = 'user_form'
        employee_form = EmployeeForm(request.POST)
        employee_form.prefix = 'employee_form'
        return self.render_to_response(self.get_context_data({
            'employee_form': employee_form,
            'user_form': user_form}))


def register_user(request):
    if request.method == 'POST':
        user_form = UserCreateForm(request.POST)
        employee_form = EmployeeForm(request.POST)
        if user_form.is_valid() and employee_form.is_valid():
            user = user_form.save()
            employee = employee_form.save(commit=False)
            employee.user_id = user.id
            employee.save()
            group = Group.objects.get(name='tickets_users')
            user.groups.add(group)
            messages.success(request, 'Ваш профиль был успешно обновлен!')
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки.')
    else:
        user_form = UserCreateForm()
        employee_form = EmployeeForm()
    return render(request, 'authapp/registration.html', {
        'form': user_form,
        'employee_form': employee_form
    })

class UserSettingsView(ContextPageMixin, UpdateView):
    template_name = 'authapp/usersettings.html'
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy('employeesapp:list_employees')
    pagename = 'Настройки'
    def get_object(self, **kwargs):
        username = self.kwargs.get("username")
        return get_object_or_404(Employee, user__exact=self.request.user.id)
