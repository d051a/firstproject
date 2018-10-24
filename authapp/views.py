from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserCreateForm
from django.shortcuts import render
from django.template import RequestContext, loader
from django import forms

# Create your views here.

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
