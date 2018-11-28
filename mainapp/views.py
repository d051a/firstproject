from django.shortcuts import render
from ticketsapp.models import SubProblem
from django.views.generic import ListView
from .models import News
# сreate your views here.


def main(request):
    pagename = 'Главная'
    return render(request, 'main.html', {'pagename': pagename})

def load_subproblems(request):
    mainproblem_id = request.GET.get('mainproblem')
    subproblem = SubProblem.objects.filter(
        mainproblem_id=mainproblem_id).order_by('subproblemname')
    return render(request, 'subproblems_dropdown_list_options.html',
        {'subproblems': subproblem})

class NewsList(ListView):
    template_name = 'main.html'
    model = News
    context_object_name = 'newslist'
    pagename = 'Новости Департамента'
