from django import forms
from django.forms import ModelForm
from .models import Ticket, SubProblem


class TicketForm(ModelForm):
    class Meta():
        model = Ticket
        fields = [
            'priority',
            'mainproblem',
            'subproblem',
            'description',
            'employee_start']
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
            'mainproblem',
            'subproblem',
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
