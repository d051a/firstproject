from django import forms
from django.forms import ModelForm
from .models import News
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'type']
        widgets = {
            'title': SummernoteWidget(),
            'content': SummernoteInplaceWidget(),
            'type': forms.Select(attrs={'class': 'form-control'}),
        }
