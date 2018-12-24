from django import forms
from .models import Employee, Post
from mainapp.models import SubDevision


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
            'post',
            'img',)
        widgets = {
            'firstname': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Имя'}),
            'fio': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия Имя Отчество'}),
            'patronymic': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Отчество'}),
            'birthdate': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата рождения *ДД.ММ.ГГГГ*'}),
            'telephonenum': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Телефон'}),
            'location': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Кабинет'}),
            'department': forms.Select(attrs={
                'class': 'form-control form-control', 'type': 'text'}),
            'subdevision': forms.Select(attrs={'class': 'form-control'}),
            'post': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subdevision'].queryset = SubDevision.objects.none()
        if 'subdevision' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['subdevision'].queryset = SubDevision.objects.filter(department_id=department_id).order_by('department')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['subdevision'].queryset = self.instance.department.subdevision_set.order_by('subdevisionname')
            print(self.fields['subdevision'].queryset)



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'postname',
                )
        widgets = {
            'postname': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Название должности'})}


class EmployeeDisabledForm(forms.ModelForm):
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
                'class': 'form-control form-control', 'type': 'text'}),
            'subdevision': forms.Select(attrs={'class': 'form-control'}),
            'post': forms.Select(attrs={'class': 'form-control'}),}
