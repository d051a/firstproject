from django import forms
from django.forms import ModelForm
from .models import Certificate, Persone


class CertificateModelForm(ModelForm):
    class Meta:
        model = Certificate
        fields = ['fullname', 'validate_start_date', 'validate_end_date', 'cert_file', 'email']
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'validate_start_date': forms.TextInput(attrs={'class': 'form-control'}),
            'validate_end_date': forms.TextInput(attrs={'class': 'form-control'}),
            'cert_file': forms.FileInput(attrs={'class': 'form-control-file'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
                    }
    def save(self):
        certificate = super(CertificateModelForm, self).save()
        certificate.fullname = self.cleaned_data['fullname']
        certificate.validate_end_date = self.cleaned_data['validate_end_date']
        certificate.cert_file = self.cleaned_data['cert_file']
        certificate.email = self.cleaned_data['email']
        certificate.save()
        return certificate


class CertificateAddModelForm(ModelForm):
    class Meta:
        model = Certificate
        fields = {'cert_file'}
        widgets = {
                    'cert_file': forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))}


class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class PersoneModelForm(ModelForm):

    class Meta:
        model = Persone
        fields = ['fullname', 'snils', 'inn']
        widgets = {
                    'fullname': forms.TextInput(attrs={'class': 'form-control'}),
                    'snils': forms.TextInput(attrs={'class': 'form-control'}),
                    'inn': forms.TextInput(attrs={'class': 'form-control'}),
                    }
        error_messages = {}

    def save(self):
        persone = super(PersoneModelForm, self).save()
        persone.fullname = self.cleaned_data['fullname']
        persone.validate_end_date = self.cleaned_data['snils']
        persone.cert_file = self.cleaned_data['inn']
        persone.save()
        return persone
