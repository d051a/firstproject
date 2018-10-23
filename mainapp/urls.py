from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

#app_name = 'mainapp'

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^ajax/load-subproblems/$', views.load_subproblems, name='ajax_load_subproblems'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
