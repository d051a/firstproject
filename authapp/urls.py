from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [

    url(r'^registration/$', views.register_user, name='registration'),
    #url(r'^registration/$', views.RegisterFormView.as_view(), name='registration'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^settings/$', views.UserSettingsView.as_view(), name='settings'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
