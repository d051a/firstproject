from django import forms
from .models import Computer


class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
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
                'class': 'form-control', 'placeholder': 'Инвентарный номер'}),
            'serialnum': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Серийный номер'}),
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Имя компьютера'}),
            'netbiosname': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'NETBIOS-имя'}),
            'ip': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'IP-адрес'}),
            'macaddress': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'MAC-адрес'}),
            'computermodelname': forms.Select(attrs={
                'class': 'form-control form-control', 'type': 'text'}),
        }

class ExcelForm(forms.Form):

    file = forms.FileField(label= "Выберите excel файл для загрузки")
