from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.conf.urls.static import static

#app_name = 'recepientsapp'

urlpatterns = [
    url(r'^$', login_required(views.MainView.as_view()), name='certificates'), #login_required для доступа только аутентифицированных пользователей.
    url(r'^(\d+)$', login_required(views.CertificateEdit.as_view()), name='certificate_edit'),
    url(r'^add_cert$', login_required(views.FileFieldView.as_view()), name='certificate_add'),
    url(r'^persones/$', login_required(views.PersonesMainView.as_view()), name='persones'),
    url(r'^persones/(\d+)$', login_required(views.PersoneEdit.as_view()), name='persone_edit'),

    #url(r'^persones/(\d+)$', views.persone_edit, name='persone_edit'),
    #url(r'^certificates/(\d+)$', views.certificate_edit, name='certificate_edit'),
    #url(r'^certificates/add_cert$', views.certificate_add, name='certificate_edit'),
    #url(r'^certificates/(\d+)$', login_required(views.CertificateEdit.as_view()), name='certificate_edit'),
    #url(r'^certificates/(\d+)/del', views.certificate_delete, name='certificate_del'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
