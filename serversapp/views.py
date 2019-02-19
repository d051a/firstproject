from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Server
from mainapp.models import Technic
from serversapp.forms import ServerModelForm
from mainapp.forms import TechnicModelForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, TemplateView
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
    technicform = TechnicModelForm
    template_name = 'serversapp/add_server.html'
    success_url = reverse_lazy('serversapp:list_servers')

    def post(self, request):
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

    def get_context_data(self, **kwargs):
        context = super(AddServer, self).get_context_data(**kwargs)
        context['technicform'] = self.technicform
        return context


class EditServer(ContextPageMixin, TemplateView):
    template_name = 'serversapp/edit_server.html'
    pagename = 'Изменить данные сервера'

    def get_context_data(self, **kwargs):
        server = Server.objects.get(pk=self.kwargs['pk'])
        technic = Technic.objects.get(pk=server.technic_id.pk)
        technicform = TechnicModelForm({'inventorynum1': technic.inventorynum1,
                                        'inventorynum2': technic.inventorynum2,
                                        'serialnum': technic.serialnum,
                                        'employee': technic.employee_id,}
                                       )
        serverform = ServerModelForm({'ip': server.ip,
                                    'name': server.name,})
        context = super(EditServer, self).get_context_data(**kwargs)
        context['technicform'] = technicform
        context['serverform'] = serverform
        return context

    def post(self, request, pk):
        serverform = ServerModelForm(request.POST)
        technicform = TechnicModelForm(request.POST)
        server = Server.objects.get(pk=pk)
        technic = Technic.objects.get(pk=server.technic_id.pk)
        if serverform.is_valid() and technicform.is_valid():
            technic_cld = technicform.cleaned_data
            serverform_cld = serverform.cleaned_data
            technic.inventorynum1 = technic_cld['inventorynum1']
            technic.inventorynum2 = technic_cld['inventorynum2']
            technic.serialnum = technic_cld['serialnum']
            technic.employee_id = technic_cld['employee']
            server.ip = serverform_cld['ip']
            server.name = serverform_cld['name']
            technic.save()
            server.save()
            return HttpResponseRedirect('/servers')