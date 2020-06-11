from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'workstations'

urlpatterns = [
    url(r'^$', views.ListWorkstations.as_view(), name='list_workstations'),
    url(r'^edit/(?P<pk>\d+)/$', views.EditWorkstation.as_view(), name='edit_workstation'),
    url(r'^delete/(?P<pk>\d+)/$', views.DeleteWorkstation.as_view(), name='delete_workstation'),
    url(r'^add/$', views.AddWorkstation.as_view(), name='add_workstation'),
    url(r'^upload/$', views.AddFromExcel.as_view(), name='add_fromexcel'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
