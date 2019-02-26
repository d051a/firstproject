import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from .models import Workstation, WorkstationModel
from django.urls import reverse_lazy
from .forms import ExcelForm, WorkstationForm
from .excelparser import ExcelParser
from ACCOUNTING.generic.mixins import ContextPageMixin


class AddFromExcel(LoginRequiredMixin, View):

    def get(self, request):
        form = ExcelForm()
        context = {'form': form}
        return render(request, 'workstationsapp/excel_parser.html', context)

    def post(self, request):
        form = ExcelForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            path = default_storage.save('tmp/temp.xlsx', ContentFile(file.read()))
            tmp_file = os.path.join(settings.MEDIA_ROOT, path)
            parser = ExcelParser()
            exceldata = parser.parse(tmp_file)
            default_storage.delete(path)
            for key, value in exceldata.items():
                obj, created = WorkstationModel.objects.get_or_create(model=value)
                if created:
                    get = Workstation.objects.create(title=key, model=obj)
                    get.save()
                else:
                    comp = Workstation.objects.create(title=key, model=obj)
                    comp.save()

            url = reverse_lazy('workstationsapp:list_workstations')
            return redirect(url)

        return render(request, 'workstationsapp/excel_parser.html')


class ListWorkstations(ContextPageMixin, LoginRequiredMixin, ListView):
    pagename = 'Рабочие станции'
    model = Workstation
    template_name = 'workstationsapp/list_workstations.html'
    context_object_name = 'workstations_list'

class AddWorkstation(ContextPageMixin, LoginRequiredMixin, CreateView):
    pagename = 'Новая рабочая станция'
    model = Workstation
    form_class = WorkstationForm
    template_name = 'workstationsapp/add_workstation.html'
    success_url = reverse_lazy('workstationsapp:list_workstations')


class EditWorkstation(ContextPageMixin, LoginRequiredMixin, UpdateView):
    pagename = 'Изменение данных'
    model = Workstation
    form_class = WorkstationForm
    template_name = 'workstationsapp/edit_workstation.html'
    success_url = reverse_lazy('workstationsapp:list_workstations')


class DeleteWorkstation(LoginRequiredMixin, DeleteView):
    model = Workstation
    success_url = reverse_lazy('workstationsapp:list_workstations')
