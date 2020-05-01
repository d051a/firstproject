from django import forms
from django.forms import ModelForm
from certticketapp.models import CertTicketModel

class CertTicketModelForm(ModelForm):
    class Meta:
        model = CertTicketModel
        fields = ['surname',
                  'name',
                  'middle_name',
                  'birthday',
                  'place_of_birth',
                  'INN',
                  'SNILS',
                  'email',
                  'region',
                  'passport_series',
                  'passport_num',
                  'passport_date',
                  'passport_unit_code',
                  'passport_issued_by',
                  'registration_address',
                  'position',
                  'code_word',
                  ]

        widgets = {
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control'}, format='%d.%m.%Y'),
            'place_of_birth': forms.TextInput(attrs={'class': 'form-control'}),
            'INN': forms.TextInput(attrs={'class': 'form-control'}),
            'SNILS': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'region': forms.TextInput(attrs={'class': 'form-control'}),
            'passport_series': forms.TextInput(attrs={'class': 'form-control'}),
            'passport_num': forms.TextInput(attrs={'class': 'form-control'}),
            'passport_date': forms.DateInput(attrs={'class': 'form-control'}, format='%d.%m.%Y'),
            'passport_unit_code': forms.TextInput(attrs={'class': 'form-control'}),
            'passport_issued_by': forms.TextInput(attrs={'class': 'form-control'}),
            'registration_address': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'code_word': forms.TextInput(attrs={'class': 'form-control'}),
        }
