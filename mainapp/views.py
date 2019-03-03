from django.shortcuts import render
from ticketsapp.models import SubProblem
from mainapp.models import SubDevision


def load_subproblems(request):
    mainproblem_id = request.GET.get('mainproblem')
    subproblem = SubProblem.objects.filter(
        mainproblem_id=mainproblem_id).order_by('subproblemname')
    return render(request, 'subproblems_dropdown_list_options.html', {'subproblems': subproblem})


def load_subdevisions(request):
    department_id = request.GET.get('department')
    subdevision = SubDevision.objects.filter(
        department=department_id).order_by('subdevisionname')
    return render(request, 'subdevisions_dropdown_list_options.html', {'subdevisions': subdevision})
