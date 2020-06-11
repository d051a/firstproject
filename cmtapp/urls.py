from django.conf.urls import url
from . import views


app_name = 'cmt'

urlpatterns = [
    url(r'^$', views.ListCMT.as_view(), name='list_cmts'),
    url(r'edit/(?P<pk>\d+)$', views.EditCMT.as_view(), name='edit_cmt'),
    url(r'add/$', views.AddCMT.as_view(), name='add_cmt')
]