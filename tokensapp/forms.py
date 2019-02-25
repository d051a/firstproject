from django import forms
from django.forms import ModelForm
from mainapp.forms import TechnicModelForm
from tokensapp.models import Token

class TokenForm(TechnicModelForm):
    def clean(self):
        self.instance.technictype = "TOKEN"
        return super().clean()
    class Meta:
        model = Token
        fields = ['name','inventorynum1', 'inventorynum2', 'serialnum', 'employee']
        widgets = {
            'inventorynum1': forms.TextInput(attrs={'class': 'form-control'}),
            'inventorynum2': forms.TextInput(attrs={'class': 'form-control'}),
            'serialnum': forms.TextInput(attrs={'class': 'form-control'}),
            'technictype': forms.Select(attrs={'class': 'form-control'}),
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),

        }

class TokenModelForm(ModelForm):
    class Meta:
        model = Token
        fields = ['name','inventorynum1', 'inventorynum2', 'serialnum', 'employee']