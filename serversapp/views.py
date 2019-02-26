from .models import Server
from serversapp.forms import ServerModelForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, TemplateView
from django.urls import reverse_lazy
from ACCOUNTING.generic.mixins import ContextPageMixin


class ListServers(ContextPageMixin, ListView):
    pagename = 'Серверы'
    model = Server
    context_object_name = 'list_servers'
    template_name = 'serversapp/list_servers.html'


class AddServer(ContextPageMixin, CreateView):
    pagename = 'Новая сервер'
    model = Server
    form_class = ServerModelForm
    template_name = 'serversapp/add_server.html'
    success_url = reverse_lazy('serversapp:list_servers')


class EditServer(ContextPageMixin, UpdateView):
    pagename = 'Изменить данные сервера'
    model = Server
    form_class = ServerModelForm
    template_name = 'serversapp/edit_server.html'
    success_url = reverse_lazy('serversapp:list_servers')
