from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

# app_name = 'mainapp'

urlpatterns = [
    url(r'^$', views.TicketListView.as_view(), name='list_tickets'),
    url(r'^$', views.list_tickets, name='list_tickets'),
    url(r'^edit/(?P<pk>\d+)$', views.TicketEditView.as_view(), name='edit_ticket'),
    #url(r'^edit/(\d+)$', views.edit_ticket, name='edit_ticket'),
    url(r'^add/$', views.TicketAddView.as_view(), name='add_ticket'),
    #url(r'^add/$', views.add_ticket, name='add_ticket'),
    url(r'^ajax/load-subproblems/$', views.load_subproblems, name='ajax_load_subproblems'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
