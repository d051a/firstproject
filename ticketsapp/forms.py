from django import forms
from django.forms import ModelForm
from .models import Ticket, SubProblem, MainProblem



class TicketForm(ModelForm):
    class Meta():
        model = Ticket
        fields = [
            'mainproblem',
            'subproblem',
            'description',]
        widgets = {
            'employee_start': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'mainproblem': forms.Select(attrs={'class': 'form-control'}),
            'subproblem': forms.Select(attrs={'class': 'form-control'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subproblem'].queryset = SubProblem.objects.none()
        if 'mainproblem' in self.data:
            try:
                mainproblem_id = int(self.data.get('mainproblem'))
                self.fields['subproblem'].queryset = SubProblem.objects.filter(
                    mainproblem_id=mainproblem_id).order_by('mainproblemname')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['subproblem'].queryset = \
                self.instance.mainproblem.subproblem_set.order_by('subproblem')


class EditTicketForm(ModelForm):
    class Meta():
        model = Ticket
        fields = [
            'status',
            'performer',
            'note']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control'}),
            'mainproblem': forms.Select(attrs={'class': 'form-control'}),
            'subproblem': forms.Select(attrs={'class': 'form-control'}),
            'employee_start': forms.TextInput(attrs={'class': 'form-control'}),
            'performer': forms.Select(attrs={'class': 'form-control'})}


class EditMyTicketForm(ModelForm):
    class Meta():
        model = Ticket
        fields = [
            'status',
            'description']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})}


class MainProblemForm(forms.ModelForm):
    class Meta:
        model = MainProblem
        fields = (
            'mainproblemname',)
        widgets = {
            'mainproblemname': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Укажите название типовой проблемы'})}


class SubProblemForm(forms.ModelForm):
    class Meta:
        model = SubProblem
        fields = (
            'mainproblem',
            'subproblemname')
        widgets = {
            'subproblemname': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Укажите название проблемы'}),
                'mainproblem': forms.Select(attrs={'class': 'form-control'})}
