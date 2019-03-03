from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from certticketapp.models import CertTicketModel, Template
from django.urls import reverse_lazy
from ACCOUNTING.generic.mixins import ContextPageMixin
from certticketapp.forms import CertTicketModelForm
from mailmerge import MailMerge
from django.conf import settings
import zipfile

    
class CertTicketList(ContextPageMixin, ListView):
    pagename = 'Заявки на сертификаты'
    model = CertTicketModel
    context_object_name = 'cert_ticket_list'
    template_name = 'certticketapp/list_certtickets.html'


class AddCertTicket(ContextPageMixin, CreateView):
    pagename = 'Новая заявка на сертификат'
    model = CertTicketModel
    form_class = CertTicketModelForm
    template_name = 'certticketapp/add_certticket.html'
    success_url = reverse_lazy('certticketapp:list_cert_tickets')


class EditCertTicket(ContextPageMixin, UpdateView):
    pagename = 'Изменение заявки'
    model = CertTicketModel
    form_class = CertTicketModelForm
    template_name = 'certticketapp/edit_certticket.html'
    success_url = reverse_lazy('certticketapp:list_cert_tickets')


class DeleteCertTicket(ContextPageMixin, DeleteView):
    model = CertTicketModel
    success_url = reverse_lazy('certticketapp:list_cert_tickets')


def file_generate(request, ticket_pk):
    templates = Template.objects.all()
    cert_ticket = CertTicketModel.objects.filter(pk=ticket_pk)
    cert_ticket_values_dict = cert_ticket.values()[0]
    model_fields_list = cert_ticket_values_dict.keys()
    docs_paths = []
    zip_file_name = '{}/{}_docs.zip'.format(settings.MEDIA_ROOT, ticket_pk)
    for template in templates:
        with MailMerge(template.file.path) as document:
            document_tags = document.get_merge_fields()
            merge_tags = {}
            for tag in document_tags:
                if tag in model_fields_list:
                    merge_tags[tag] = cert_ticket_values_dict[tag]
            document.merge(**merge_tags)
            document_path = '{}/{}_{}.docx'.format(settings.MEDIA_ROOT, cert_ticket_values_dict['id'], template.name)
            docs_paths.append(document_path)
            document.write(document_path)
            document.close()
    with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
        for document_patch in docs_paths:
            filename = document_patch.split('/')[-1]
            zip_file.write(document_patch, filename)
        zip_file.close()
