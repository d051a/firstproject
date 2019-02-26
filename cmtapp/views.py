from django.shortcuts import render
from cmtapp.models import CMT
from cmtapp.forms import CMTForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from ACCOUNTING.generic.mixins import ContextPageMixin


def list_cmts(request):
    pagename = 'Все'
    return render(request, 'cmtapp/list_cmt.html', {'pagename': pagename})


def add_cmt(request):
    pagename = 'Новая КМТ'
    return render(request, 'cmtapp/add_cmt.html', {'pagename': pagename})


def edit_cmt(request):
    pagename = 'Изменить данные КМТ'
    return render(request, 'cmtapp/edit_cmt.html', {'pagename': pagename})

class ListCMT(ContextPageMixin, ListView):
    pagename = 'КМТ'
    model = CMT
    context_object_name = 'cmtslist'
    template_name = 'cmtapp/list_cmts.html'


class AddCMT(ContextPageMixin, CreateView):
    pagename = 'Новая КМТ'
    model = CMT
    form_class = CMTForm
    template_name = 'cmtapp/add_cmt.html'
    success_url = reverse_lazy('cmtapp:list_cmts')

class EditCMT(ContextPageMixin, UpdateView):
    pagename = 'Изменение данных'
    model = CMT
    form_class = CMTForm
    template_name = 'cmtapp/edit_cmt.html'
    success_url = reverse_lazy('cmtapp:list_cmts')


class DeleteCMT(ContextPageMixin, DeleteView):
    model = CMT
    success_url = reverse_lazy('cmtapp:list_cmts')