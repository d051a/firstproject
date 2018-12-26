from django.shortcuts import render
from ticketsapp.models import SubProblem
from mainapp.models import SubDevision
from django.views.generic import ListView
from .models import News
from holidaysapp.models import Holiday
from employeesapp.models import Employee
from ACCOUNTING.generic.mixins import ContextPageMixin
from datetime import datetime
from itertools import chain

def load_subproblems(request):
    mainproblem_id = request.GET.get('mainproblem')
    subproblem = SubProblem.objects.filter(
        mainproblem_id=mainproblem_id).order_by('subproblemname')
    return render(request, 'subproblems_dropdown_list_options.html',
        {'subproblems': subproblem})

def load_subdevisions(request):
    department_id = request.GET.get('department')
    subdevision = SubDevision.objects.filter(
        department=department_id).order_by('subdevisionname')
    return render(request, 'subdevisions_dropdown_list_options.html',
        {'subdevisions': subdevision})

class NewsList(ContextPageMixin, ListView):
    template_name = 'main.html'
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
