from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import News
from holidaysapp.models import Holiday
from employeesapp.models import Employee
from ACCOUNTING.generic.mixins import ContextPageMixin
from datetime import datetime
from django.views import View
from django.shortcuts  import render
from django.db.models import Q


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


class SearchView(ContextPageMixin, View):
    template_name = 'newsapp/main_news.html'
    pagename = 'Новости Департамента'
    
    def get(self, request):
        search_query = self.request.GET.get('search')
        founded_news = News.objects.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query))
        today = datetime.now().date()
        holiday_list_gte = Holiday.objects.filter(
            date__day__gte=today.day,
            date__month__gte=today.month
        )
        birthdays_list_gte = Employee.objects.filter(
            birthdate__day__gte=today.day,
            birthdate__month__gte=today.month
        )
        context = {
            'newslist': founded_news,
            'holidays_list': holiday_list_gte[:5],
            'birthdays_list': birthdays_list_gte[:5],
            'pagename': self.pagename,
        }
        return render(self.request, self.template_name, context)
