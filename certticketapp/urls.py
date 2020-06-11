from django.conf.urls import url
from . import views

app_name = 'certtickets'

urlpatterns = [
    url(r'^$', views.CertTicketList.as_view(), name='list_cert_tickets'),
    url(r'edit/(?P<pk>\d+)$', views.EditCertTicket.as_view(), name='edit_cert_ticket'),
    url(r'add/$', views.AddCertTicket.as_view(), name='add_cert_ticket'),
    url(r'filegen/(?P<ticket_pk>\d+)/(?P<template_type>\d+)$', views.file_generate, name='file_generate')
]