"""ACCOUNTING URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('authapp.urls', namespace='authapp')),
    url(r'^', include('newsapp.urls', namespace='newsapp')),
    url(r'^', include('mainapp.urls', namespace='mainapp')),
    url(r'^administration/', include('adminapp.urls', namespace='adminapp')),
    url(r'^cmt/', include('cmtapp.urls', namespace='cmtapp')),
    url(r'^employees/', include('employeesapp.urls', namespace='employeesapp')),
    url(r'^servers/', include('serversapp.urls', namespace='serversapp')),
    url(r'^tickets/', include('ticketsapp.urls', namespace='ticketsapp')),
    url(r'^workstations/', include('workstationsapp.urls', namespace='workstationsapp')),
    url(r'^holidays/', include('holidaysapp.urls', namespace='holidaysapp')),
    url(r'^certificates/', include('certificatesapp.urls', namespace='certificatesapp')),
    url(r'^summernote/', include('django_summernote.urls')),

]
