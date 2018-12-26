from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

#app_name = 'mainapp'

urlpatterns = [
    url(r'^$', views.NewsList.as_view(), name='main'),
    url(r'^ajax/load-subproblems/$', views.load_subproblems, name='ajax_load_subproblems'),
    url(r'^ajax/load-subdevisions/$', views.load_subdevisions, name='ajax_load_subdevisions'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
