from django.shortcuts import render


def list_workstations(request):
    pagename = 'Все'
    return render(request, 'workstationsapp/list_workstations.html', {
        'pagename': pagename})


def add_workstation(request):
    pagename = 'Новая рабочая станция'
    return render(request, 'workstationsapp/add_workstation.html', {
        'pagename': pagename})


def edit_workstation(request):
    pagename = 'Изменить данные рабочей станции'
    return render(request, 'workstationsapp/edit_workstation.html', {
        'pagename': pagename})
