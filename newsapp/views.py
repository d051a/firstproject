from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import News
from holidaysapp.models import Holiday
from employeesapp.models import Employee
from ACCOUNTING.generic.mixins import ContextPageMixin
from datetime import datetime


class NewsList(ContextPageMixin, ListView):
    template_name = 'newsapp/main_news.html'
    model = News
    context_object_name = 'newslist'
    pagename = 'Новости Департамента'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.now().date()
        holiday_list_gte = Holiday.objects.filter(date__day__gte=today.day,
            date__month__gte=today.month)
        birthdays_list_gte = Employee.objects.filter(birthdate__day__gte=today.day,
            birthdate__month__gte=today.month)
        context['holidays_list'] = holiday_list_gte[:5]
        context['birthdays_list'] = birthdays_list_gte[:5]
        return context


'''class NewsAdd (ContextPageMixin, CreateView):
    template_name'''


class NewsPageView(ContextPageMixin, UpdateView):
    template_name = 'newsapp/edit_news.html'
    model = News
    context_object_name = 'news'
    pagename = 'Новости Департамента'
    fields = 'title', 'content'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.now().date()
        holiday_list_gte = Holiday.objects.filter(date__day__gte=today.day,
            date__month__gte=today.month)
        birthdays_list_gte = Employee.objects.filter(birthdate__day__gte=today.day,
            birthdate__month__gte=today.month)
        context['holidays_list'] = holiday_list_gte[:5]
        context['birthdays_list'] = birthdays_list_gte[:5]
        return context
