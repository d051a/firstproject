from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

# app_name = 'mainapp'

urlpatterns = [
    url(r'^posts/$', views.PostListView.as_view(), name='list_posts'),
    url(r'^posts/edit/(?P<pk>\d+)$', views.PostEditView.as_view(), name='edit_post'),
    url(r'^posts/add/$', views.PostAddView.as_view(), name='add_post'),
    url(r'^$', views.EmployeeListView.as_view(), name='list_employees'),
    url(r'^edit/(?P<pk>\d+)$', views.EmployeeEditView.as_view(), name='edit_employee'),
    url(r'^add/$', views.register_user, name='add_employee'),
    url(r'^telephone_book/$', views.TelephoneBookView.as_view(), name='telephone_book'),
    url(r'^birthdays/$', views.BirthdaysListView.as_view(), name='birthdays'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
