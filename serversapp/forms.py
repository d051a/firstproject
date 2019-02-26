from django import forms
from django.forms import ModelForm
from .models import Server
from mainapp.forms import TechnicModelForm


class ServerModelForm(ModelForm):
    def clean(self):
        self.instance.technictype = "SERVER"
        return super().clean()
    class Meta:
        model = Server
        fields = ['ip', 'name', 'inventorynum1', 'inventorynum2', 'serialnum', 'employee']
        widgets = {
        'ip': forms.TextInput(attrs={'class': 'form-control'}),
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'inventorynum1': forms.TextInput(attrs={'class': 'form-control'}),
        'inventorynum2': forms.TextInput(attrs={'class': 'form-control'}),
        'serialnum': forms.TextInput(attrs={'class': 'form-control'}),
        'employee': forms.Select(attrs={'class': 'form-control'}),
        }
