from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.TokensList.as_view(), name='list_tokens'),
    url(r'edit/(?P<pk>\d+)$', views.EditToken.as_view(), name='edit_token'),
    url(r'add/$', views.AddToken.as_view(), name='add_token')
]
