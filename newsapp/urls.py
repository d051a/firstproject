from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

#app_name = 'mainapp'

urlpatterns = [
    url(r'^$', views.NewsList.as_view(), name='main'),
    url(r'^search/', views.SearchView.as_view(), name='search_page'),
    url(r'^(?P<pk>\d+)$', views.NewsPageView.as_view(), name='newspage')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
