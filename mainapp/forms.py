from django import forms
from django.forms import ModelForm
from .models import Technic


class TechnicModelForm(ModelForm):
    class Meta:
        model = Technic
        fields = ['inventorynum1', 'inventorynum2', 'serialnum', 'employee']
        widgets = {
            'inventorynum1': forms.TextInput(attrs={'class': 'form-control'}),
            'inventorynum2': forms.TextInput(attrs={'class': 'form-control'}),
            'serialnum': forms.TextInput(attrs={'class': 'form-control'}),
            'technictype': forms.Select(attrs={'class': 'form-control'}),
            'employee': forms.Select(attrs={'class': 'form-control'}),
        }
