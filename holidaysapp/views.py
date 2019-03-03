from .models import Holiday
from django.views.generic import ListView, DetailView
from ACCOUNTING.generic.mixins import ContextPageMixin
from datetime import datetime
from itertools import chain


class HolidaysListView(ContextPageMixin, ListView):
    template_name = 'holidaysapp/list_holidays.html'
    model = Holiday
    context_object_name = 'holidayslist'
    pagename = 'Праздники России'

    def get_queryset(self):
        object_list = super(HolidaysListView, self).get_queryset()
        today = datetime.now().date()
        object_list_gte = Holiday.objects.filter(date__day__gte=today.day,
                                                 date__month__gte=today.month)
        object_list_lte = Holiday.objects.filter(date__day__lte=today.day,
                                                 date__month__lte=today.month)
        object_list = chain(object_list_gte, object_list_lte)
        return object_list


class HolidayPageView(ContextPageMixin, DetailView):
    pagename = 'Праздники России'
    template_name = 'holidaysapp/view_holiday.html'
    model = Holiday
    context_object_name = 'holiday'
