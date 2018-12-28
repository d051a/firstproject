from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

#app_name = 'mainapp'

urlpatterns = [
    url(r'^$', views.NewsList.as_view(), name='main'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
