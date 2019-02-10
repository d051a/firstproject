from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Server
from mainapp.models import Technic
from serversapp.forms import ServerModelForm
from mainapp.forms import TechnicModelForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from ACCOUNTING.generic.mixins import ContextPageMixin


def list_servers(request):
    pagename = 'Все серверы'
    allservers = Server.objects.all()
    return render(request, 'serversapp/list_servers.html', {
        'pagename': pagename,
        'serverslist': allservers})


def add_server(request):
    pagename = 'Добавить новый сервер'
    if request.method == 'POST':
        serverform = ServerModelForm(request.POST)
        technicform = TechnicModelForm(request.POST)
        if serverform.is_valid() and technicform.is_valid():
            technicform = technicform.save()
            serverform = serverform.save(commit=False)
            serverform.technic_id = technicform
            serverform.save()
            technicform.technictype = 'SERVER'
            technicform.save()
            return HttpResponseRedirect('/servers')
    else:
        serverform = ServerModelForm()
        technicform = TechnicModelForm()
    return render(request, 'serversapp/add_server.html', {
        'pagename': pagename,
        'serverform': serverform,
        'technicform': technicform})


class AddServer(ContextPageMixin, CreateView):
    pagename = 'Новая рабочая станция'
    model = Server
    form_class = ServerModelForm
    template_name = 'serversapp/add_server.html'
    success_url = reverse_lazy('serversapp:list_servers')

def post(self, request):
    pagename = 'Добавить новый сервер'
    if request.method == 'POST':
        serverform = ServerModelForm(request.POST)
        technicform = TechnicModelForm(request.POST)
        if serverform.is_valid() and technicform.is_valid():
            technicform = technicform.save()
            serverform = serverform.save(commit=False)
            serverform.technic_id = technicform
            serverform.save()
            technicform.technictype = 'SERVER'
            technicform.save()
            return HttpResponseRedirect('/servers')
    else:
        serverform = ServerModelForm()
        technicform = TechnicModelForm()
    return render(request, 'serversapp/add_server.html', {
        'pagename': pagename,
        'serverform': serverform,
        'technicform': technicform})

def edit_server(request):
    pagename = 'Изменить данные сервера'
    return render(request, 'serversapp/edit_server.html', {
        'pagename': pagename})
