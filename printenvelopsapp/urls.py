from django.conf.urls import url
from . import views

app_name = 'printenvelopsapp'

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.recepients, name='recepients'),
    url(r'sentenvelops/$', views.sent_envelops, name='sent_envelops'),
    url(r'recepient/(\d+)/$', views.recepient_detail, name='recepient_detail'),
    url(r'recepient_add/$', views.recepient_add, name='recepient_add'),
    url(r'envelops/$', views.envelops, name='envelops'),
    url(r'envelops_detail/(\d+)/$', views.envelop_template_detail, name='envelops_detail'),
    url(r'gen_env/', views.env_generate, name='env_gen'),
    url(r'envelop_gen/(\d+)/(\d+)/$', views.env_generate, name='envelop_gen'),
    url(r'envelop_add/$', views.envelop_template_add, name='envelop_template_add'),
    url(r'printenvelop/$', views.print_envelop, name='envelop_print'),
    url(r'registry/$', views.registry_list, name='registry_list'),
    url(r'registry_add/$', views.registry_add, name='registry_add'),
    url(r'registry/(?P<registry_pk>\d+)/$', views.registry_detail, name='registry_detail'),
    url(r'registry_delete/(\d+)/$', views.registry_delete, name='registry_delete'),
    url(r'registry/del_envelop/(\d+)/(\d+)', views.sent_envelop_del_from_registry, name='drop_registry_envelop'),
    url(r'registry_print/', views.registry_print, name='registry_print'),
    # url(r'registry_add2/', views.registry_add2, name='registry_print'),
    # url(r'registry2/(?P<pk>\d+)/$', views.RegistryDetail.as_view(), name='registry_detail'),
]
