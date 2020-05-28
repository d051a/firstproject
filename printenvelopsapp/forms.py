from django import forms
from django.db import models
from .models import Envelop, SentEnvelop, Registry, RegistryTemplate, Recepient
from django.forms import ModelForm


class RecipientForm(ModelForm):
    class Meta:
        model = Recepient
        fields = [
            'title',
            'address',
            'city',
            'region',
            'postcode'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'region': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'postcode': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PrintEnvelopForm(ModelForm):
    class Meta:
        model = SentEnvelop
        fields = [
            'recipient',
            'registry_type',
            'rpo_type',
            'envelop_format',
            'outer_num',
        ]
        widgets = {
            'recipient': forms.Select(attrs={'class': 'js-example-placeholder-single js-states form-control', 'height': '75%'}),
            'rpo_type': forms.Select(attrs={'class': 'form-control'}),
            'envelop_format': forms.Select(attrs={'class': 'form-control'}),
            'registry_type': forms.Select(attrs={'class': 'form-control'}),
            'outer_num': forms.TextInput(attrs={'class': 'form-control'}),
            'address_format': forms.Select(attrs={'class': 'form-control'}),

        }


class EnvelopeFormatModelForm(ModelForm):
    class Meta:
        model = Envelop
        fields = ['env_title', 'envelop_format', 'secret_type', 'envelop_template']
        widgets = {
            'env_title': forms.TextInput(attrs={'class': 'form-control'}),
            'envelop_format': forms.Select(attrs={'class': 'form-control'}),

        }



class RegistryForm(ModelForm):
    class Meta:
        model = Registry
        fields = ['rpo_type', 'type']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'}),
            'rpo_type': forms.Select(attrs={'class': 'form-control'}),
        }

class RegistryTemplateForm(forms.Form):
    registry = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'special', 'hidden': 'true'}), label='', required=False)


