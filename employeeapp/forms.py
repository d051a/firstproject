from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = (
            'lastname',
            'birthdate',
            'telephonenum',
            'location',
            )
        widgets = {
        'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
        'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}),
        'patronymic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Отчество'}),
        'birthdate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Дата рождения *ДД.ММ.ГГГГ*'}),
        'telephonenum': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер телефона'}),
        'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер кабинета'}),
        }
