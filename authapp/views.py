from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.shortcuts import render
from django.template import RequestContext, loader
from django import forms
from django.db import transaction
from .forms import UserCreateForm
from employeesapp.forms import EmployeeForm


class RegisterFormView(FormView):
    form_class = UserCreateForm
    success_url = '/auth/login/'
    template_name = 'authapp/registration.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    success_url = '/'
    template_name = 'authapp/login.html'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        print(dir(AuthenticationForm))
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/auth/login/')


class TestRegisterFormView(FormView):
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
            messages.success(request, 'Ваш профиль был успешно обновлен!')
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки.')
    else:
        user_form = UserCreateForm()
        employee_form = EmployeeForm()
    return render(request, 'authapp/registration_v2.html', {
        'form': user_form,
        'employee_form': employee_form
    })
