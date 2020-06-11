from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'administration'

urlpatterns = [
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^access_rights/$', views.access_rights, name='access_rights'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
