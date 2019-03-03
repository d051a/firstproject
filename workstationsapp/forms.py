from django import forms
from .models import Workstation
from mainapp.forms import TechnicModelForm


class WorkstationForm(TechnicModelForm):
    def clean(self):
        self.instance.technictype = "WORKSTATION"
        return super().clean()

    class Meta:
        model = Workstation
        fields = ('name', 'netbios_name', 'ip_address', 'mac_address', 'model_name',
                  'inventorynum1', 'inventorynum2', 'serialnum', 'employee'
                  )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'netbios_name': forms.TextInput(attrs={'class': 'form-control'}),
            'ip_address': forms.TextInput(attrs={'class': 'form-control'}),
            'mac_address': forms.TextInput(attrs={'class': 'form-control'}),
            'model_name': forms.Select(attrs={'class': 'form-control'}),
            'inventorynum1': forms.TextInput(attrs={'class': 'form-control'}),
            'inventorynum2': forms.TextInput(attrs={'class': 'form-control'}),
            'serialnum': forms.TextInput(attrs={'class': 'form-control'}),
            'technictype': forms.Select(attrs={'class': 'form-control'}),
            'employee': forms.Select(attrs={'class': 'form-control'}),
        }


class ExcelForm(forms.Form):
    file = forms.FileField(label="Выберите excel файл для загрузки")
