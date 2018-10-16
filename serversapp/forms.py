from django import forms
from django.forms import ModelForm
from .models import Server
from mainapp.forms import TechnicModelForm


class ServerModelForm(ModelForm):
    class Meta:
        model = Server
        fields = ['ip', 'name',]
        widgets = {
        'ip': forms.TextInput(attrs={'class': 'form-control'}),
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
