from django.shortcuts import render
from ticketsapp.models import SubProblem
from mainapp.models import SubDevision
from django.views.generic import ListView, CreateView
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
