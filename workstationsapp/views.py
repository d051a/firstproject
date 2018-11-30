import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from .models import Computer, ComputerModel
from django.urls import reverse_lazy
from .forms import ExcelForm, ComputerForm
from .excelparser import ExcelParser


class AddFromExcel(View):

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


class ListWorkstations(ListView):

    model = Computer
    template_name = 'workstationsapp/list_workstations.html'


class AddWorkstation(CreateView):
    model = Computer
    form_class = ComputerForm
    template_name = 'workstationsapp/add_workstation.html'
    success_url = reverse_lazy('workstationsapp:list_workstations')


class EditWorkstation(UpdateView):
    model = Computer
    form_class = ComputerForm
    template_name = 'workstationsapp/edit_workstation.html'
    success_url = reverse_lazy('workstationsapp:list_workstations')


class DeleteWorkstation(DeleteView):
    model = Computer
    success_url = reverse_lazy('workstationsapp:list_workstations')
