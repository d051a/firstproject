from django import forms
from django.forms import ModelForm
from .models import Ticket


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
