from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

# app_name = 'mainapp'

urlpatterns = [
    url(r'^problems/$', views.MainProblemListView.as_view(), name='list_problems'),
    url(r'^problems/edit/(?P<pk>\d+)$', views.MainProblemEditView.as_view(),
        name='edit_problem'),
    url(r'^problems/add/$', views.MainProblemAddView.as_view(), name='add_problem'),
    url(r'^subproblems/$', views.SubProblemListView.as_view(), name='list_subproblems'),
    url(r'^subproblems/edit/(?P<pk>\d+)$', views.SubProblemEditView.as_view(),
        name='edit_subproblem'),
    url(r'^subproblems/add/$', views.SubProblemAddView.as_view(), name='add_subproblem'),
    url(r'^$', views.TicketListView.as_view(), name='list_tickets'),
    url(r'^edit/(?P<pk>\d+)$', views.TicketEditView.as_view(),
        name='edit_ticket'),
    url(r'^add/$', views.TicketAddView.as_view(), name='add_ticket'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
