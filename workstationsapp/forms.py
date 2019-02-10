from django import forms
from .models import Workstation


class WorkstationForm(forms.ModelForm):
    class Meta:
        model = Workstation
        fields = (
            'inventorynum',
            'serialnum',
            'name',
            'netbiosname',
            'ip',
            'macaddress',
            'computermodelname',
        )
        widgets = {
            'inventorynum': forms.TextInput(attrs={
                'class': 'form-control'}),
            'serialnum': forms.TextInput(attrs={
                'class': 'form-control'}),
            'name': forms.TextInput(attrs={
                'class': 'form-control'}),
            'netbiosname': forms.TextInput(attrs={
                'class': 'form-control'}),
            'ip': forms.TextInput(attrs={
                'class': 'form-control'}),
            'macaddress': forms.TextInput(attrs={
                'class': 'form-control'}),
            'computermodelname': forms.Select(attrs={
                'class': 'form-control form-control', 'type': 'text'}),
        }

class ExcelForm(forms.Form):

    file = forms.FileField(label= "Выберите excel файл для загрузки")
