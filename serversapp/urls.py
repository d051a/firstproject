from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'servers'

urlpatterns = [
    url(r'^$', views.ListServers.as_view(), name='list_servers'),
    url(r'^edit/(?P<pk>\d+)$', views.EditServer.as_view(), name='edit_server'),
    url(r'^add/$', views.AddServer.as_view(), name='add_server'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
