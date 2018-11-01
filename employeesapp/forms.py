from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = (
            'fio',
            'birthdate',
            'telephonenum',
            'location',
            'department',
            'subdevision',
            'post',)
        widgets = {
            'firstname': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Имя'}),
            'fio': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия Имя Отчество'}),
            'patronymic': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Отчество'}),
            'birthdate': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата рождения *ДД.ММ.ГГГГ*'}),
            'telephonenum': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Номер телефона'}),
            'location': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Номер кабинета'}),
            'department': forms.Select(attrs={
                'class': 'form-control form-control-lg', 'type': 'text'}),
            'subdevision': forms.Select(attrs={'class': 'form-control'}),
            'post': forms.Select(attrs={'class': 'form-control'})}
