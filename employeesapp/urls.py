from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

# app_name = 'mainapp'

urlpatterns = [
    url(r'^$', views.EmployeeListView.as_view(), name='list_employees'),
    url(r'^$', views.list_employees, name='list_employees'),
    url(r'^edit/$', views.edit_employee, name='edit_employee'),
    url(r'^add/$', views.add_employee, name='add_employee'),
    url(r'^telephone_book/$', views.TelephoneBookView.as_view(), name='telephone_book'),
    url(r'^telephone_book/$', views.telephone_book, name='telephone_book'),
    url(r'^birthdays/$', views.BirthdaysListView.as_view(), name='birthdays'),
    url(r'^birthdays/$', views.birthdays, name='birthdays'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
