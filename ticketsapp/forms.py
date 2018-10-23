from django import forms
from django.forms import ModelForm
from .models import Ticket, SubProblem


class TicketForm(ModelForm):
    class Meta():
        model = Ticket
        fields = ['priority',
                'mainproblem',
                'subproblem',
                'description',
                ]
        widgets = {
        'priority': forms.Select(attrs={'class': 'form-control'}),
        'description': forms.Textarea(attrs={'class': 'form-control'}),
        'mainproblem': forms.Select(attrs={'class': 'form-control'}),
        'subproblem': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subproblem'].queryset = SubProblem.objects.none()
        print(self.fields['subproblem'])

        if 'mainmproblem' in self.data:
            try:
                mainmproblem_id = int(self.data.get('mainmproblem'))
                self.fields['subproblem'].queryset = SubProblem.objects.filter(mainmproblem_id=mainmproblem_id).order_by('mainproblemname')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty subproblem queryset
        elif self.instance.pk:
            self.fields['subproblem'].queryset = self.instance.mainmproblem.subproblem_set.order_by('subproblem')

class EditTicketForm(ModelForm):
    class Meta():
        model = Ticket
        fields = [
                'status',
                'mainproblem',
                'subproblem',
                'performer',
                'note'
                ]
        widgets = {
        'status': forms.Select(attrs={'class': 'form-control'}),
        'priority': forms.Select(attrs={'class': 'form-control'}),
        'description': forms.Textarea(attrs={'class': 'form-control'}),
        'note': forms.Textarea(attrs={'class': 'form-control'}),
        'mainproblem': forms.Select(attrs={'class': 'form-control'}),
        'subproblem': forms.Select(attrs={'class': 'form-control'}),
        'employee_start': forms.TextInput(attrs={'class': 'form-control'}),
        'performer': forms.TextInput(attrs={'class': 'form-control'}),
        }
