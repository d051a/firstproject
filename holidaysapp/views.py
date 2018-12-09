from django.shortcuts import render
from .models import Holiday
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from ACCOUNTING.generic.mixins import ContextPageMixin
from django.views.generic.base import TemplateView


class HolidaysListView(ContextPageMixin, ListView):
    template_name = 'holidaysapp/list_holidays.html'
    model = Holiday
    context_object_name = 'holidayslist'
    pagename = 'Праздники России'


class HolidayPageView(ContextPageMixin, DetailView):
    pagename = 'Праздники России'
    template_name = 'holidaysapp/view_holiday.html'
    model = Holiday
    context_object_name = 'holiday'
