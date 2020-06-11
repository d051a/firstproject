from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'tickets'

urlpatterns = [
    url(r'^problems/$',
        views.MainProblemListView.as_view(),
        name='list_problems'),
    url(r'^problems/edit/(?P<pk>\d+)$',
        views.MainProblemEditView.as_view(),
        name='edit_problem'),
    url(r'^problems/add/$',
        views.MainProblemAddView.as_view(),
        name='add_problem'),
    url(r'^subproblems/$',
        views.SubProblemListView.as_view(),
        name='list_subproblems'),
    url(r'^subproblems/edit/(?P<pk>\d+)$',
        views.SubProblemEditView.as_view(),
        name='edit_subproblem'),
    url(r'^subproblems/add/$',
        views.SubProblemAddView.as_view(),
        name='add_subproblem'),
    url(r'^$',
        views.TicketListView.as_view(),
        name='list_tickets'),
    url(r'^my/$',
        views.UserTicketListView.as_view(),
        name='user_list_tickets'),
    url(r'^imperformer/$',
        views.UserPerformerTicketListView.as_view(),
        name='userperformer_list_tickets'),
    url(r'^imperformer/edit/(?P<pk>\d+)$',
        views.TicketEditView.as_view(),
        name='edit_ticket'),
    url(r'^my/edit/(?P<pk>\d+)$',
        views.MyTicketEditView.as_view(),
        name='edit_my_ticket'),
    url(r'^edit/(?P<pk>\d+)$',
        views.TicketEditView.as_view(),
        name='edit_ticket'),
    url(r'^add/$',
        views.TicketAddView.as_view(),
        name='add_ticket'),
    url(r'^edit/(?P<pk>\d+)/delete$',
        views.TicketDeleteView.as_view(),
        name='delete_ticket'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
