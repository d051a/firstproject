from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'holidays'

urlpatterns = [
    url(r'^$', views.HolidaysListView.as_view(), name='list_holidays'),
    url(r'^(?P<pk>\d+)$', views.HolidayPageView.as_view(), name='view_holiday')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
