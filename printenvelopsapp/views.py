from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import formats
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q
from .models import Recepient, Envelop, SecretType, SentEnvelop, Registry
from ACCOUNTING import settings
from .forms import RecipientForm, EnvelopeFormatModelForm, PrintEnvelopForm, \
    RegistryForm, RegistryTemplateForm, RegistrySentEnvelopForm
from .main import DateToWords
from employeesapp.models import Employee
from printenvelopsapp.num2t4ru import num2text
from .tools import tools
from docxtpl import DocxTemplate
import datetime
import zipfile
import re
import jinja2



def print_envelop(request):
    if request.method == 'POST':
        form = PrintEnvelopForm(request.POST)
        if form.is_valid():
            cld = form.cleaned_data
            envelop = SentEnvelop()
            user = Employee.objects.get(user=request.user)
            envelop.username = user
            envelop.recipient = cld['recipient']
            envelop.rpo_type = cld['rpo_type']
            envelop.envelop_format = cld['envelop_format']
            envelop.outer_num = cld['outer_num']
            envelop.registry_type = cld['registry_type']
            envelop.save()
            return envelope_generate(request, cld)
    else:
        form = PrintEnvelopForm()
    return render(request, 'print_envelop.html', {
        'form': form,
        'pagename': 'Печать конверта'
    })


def print_envelop_backup(request, recipient_pk):
    recipient = Recepient.objects.get(pk=recipient_pk)
    if request.method == 'POST':
        form = PrintEnvelopForm(request.POST)
        if form.is_valid():
            cld = form.cleaned_data
            envelop = SentEnvelop()
            user = Employee.objects.get(user=request.user)
            envelop.username = user
            envelop.recipient = cld['recipient']
            envelop.rpo_type = cld['rpo_type']
            envelop.envelop_format = cld['envelop_format']
            envelop.outer_num = cld['outer_num']
            envelop.registry_type = cld['registry_type']
            envelop.save()
            return envelope_generate(request, cld)
    else:
        form = PrintEnvelopForm(initial={'recipient': recipient})
    return render(request, 'print_envelop.html', {
        'form': form,
        'pagename': 'Печать конверта'
    })


def envelope_generate(request, envelop_data):
    recipient = envelop_data['recipient']
    envelop = envelop_data['envelop_format']
    outer_num = envelop_data['outer_num']
    template = '{}/{}'.format(settings.MEDIA_ROOT, envelop.envelop_template)
    output_document = DocxTemplate(template)
    address = (recipient.region, recipient.city, recipient.address)
    address_old_format = ', '.join(filter(None, address))
    address_new_format = ', '.join(filter(None, address[::-1]))
    context = {
        'title': recipient.title,
        'address': address_old_format,
        'address_new_format': address_new_format,
        'region': recipient.region,
        'city': recipient.city,
        'postcode': recipient.postcode,
        'outer_num': outer_num,
    }
    output_document.render(context)
    datetime_now = datetime.datetime.now()
    response = HttpResponse(content_type='text/docx')
    response['Content-Disposition'] = 'attachment; filename={}_konvert.docx'.format(datetime_now.strftime("%Y.%m.%d_%H-%M"))
    output_document.save(response)
    return response


def recepients(request):
    recepients_list = Recepient.objects.order_by("-pk")
    if request.method == 'POST':
        form = PrintEnvelopForm(request.POST)
        if form.is_valid():
            cld = form.cleaned_data
            envelop = SentEnvelop()
            user = Employee.objects.get(user=request.user)
            envelop.username = user
            envelop.recipient = cld['recipient']
            envelop.rpo_type = cld['rpo_type']
            envelop.envelop_format = cld['envelop_format']
            envelop.outer_num = cld['outer_num']
            envelop.registry_type = cld['registry_type']
            envelop.save()
            return envelope_generate(request, cld)
    else:
        form = PrintEnvelopForm()
        return render(request, 'recepients_printform.html', {
            'form': form,
            'recepients_list': recepients_list,
            'pagename': 'Адресаты'
        })


def recepients_backup(request):
    recepients_list = Recepient.objects.order_by("-pk")
    envelop_list = Envelop.objects.all()
    secret_types_list = SecretType.objects.all()
    return render(request, 'recepients_printform.html', {
        'recepients_list': recepients_list,
        'envelop_list': envelop_list,
        'secret_types_list': secret_types_list,
        'pagename': 'Адресаты'
    })


def recepient_add(request):
    if request.method == 'POST':
        form = RecipientForm(request.POST)
        if form.is_valid():
            cld = form.cleaned_data
            recipient = Recepient()
            recipient.title = cld['title']
            recipient.address = cld['address']
            recipient.postcode = cld['postcode']
            recipient.region = cld['region']
            recipient.city = cld['city']
            recipient.save()
            return redirect('printenvelopsapp:recepients')
    else:
        form = RecipientForm()

    return render(request, 'recepient_add.html', {'form': form,
                                                  'pagename': 'Новый адресат'})


def recepient_detail(request, rec_id):
    if request.method == 'POST':
        form = RecipientForm(request.POST)
        if form.is_valid():
            cld = form.cleaned_data
            recipient = Recepient.objects.get(pk=rec_id)
            recipient.title = cld['title']
            recipient.address = cld['address']
            recipient.postcode = cld['postcode']
            recipient.region = cld['region']
            recipient.city = cld['city']
            recipient.save()
            return redirect('printenvelopsapp:recepients')
    else:
        recipient_detail = Recepient.objects.get(pk=rec_id)
        form = RecipientForm({
            'title': recipient_detail.title,
            'address': recipient_detail.address,
            'postcode': recipient_detail.postcode,
            'region': recipient_detail.region,
            'city': recipient_detail.city
        })
        return render(request, 'recepient_detail.html', {
            'form': form,
            'recepient': recipient_detail,
            'pagename': 'Адресат',
        })


def recepient_delete(request, recepient_pk):
    recepient = Recepient.objects.get(pk=recepient_pk)
    recepient.delete()
    return redirect('printenvelopsapp:recepients')


def envelops(request):
    envelops_list = Envelop.objects.all()
    return render(request, 'envelops.html', {
        'envelops_list': envelops_list,
        'pagename': 'Конверты'
    })


def envelop_template_add(request):
    if request.method == 'POST':
        form = EnvelopeFormatModelForm(request.POST, request.FILES)
        if form.is_valid():
            cld = form.cleaned_data
            envelop = Envelop()
            envelop.env_title = cld['env_title']
            envelop.EnvelopFormat = cld['envelop_format']
            envelop.envelop_template = cld['envelop_template']
            envelop.save()
            return redirect('printenvelopsapp:envelops_list')
    else:
        form = EnvelopeFormatModelForm()
    return render(request, 'envelop_add.html', {
        'form': form,
        'pagename': 'Новый конверт'
    })


def envelop_template_detail(request, envelop_pk):
    envelop = Envelop.objects.get(pk=envelop_pk)
    if request.method == 'POST':
        form = EnvelopeFormatModelForm(request.POST)
        if form.is_valid():
            cld = form.cleaned_data
            envelop = Envelop()
            envelop.env_title = cld['env_title']
            envelop.EnvelopFormat = cld['envelop_format']
            envelop.envelop_template = cld['envelop_template']
            envelop.save()
            return redirect('printenvelopsapp:envelops_list')
    else:
        form = EnvelopeFormatModelForm(instance=envelop)
    return render(request, 'envelops_detail.html', {
        'form': form,
        'pagename': 'Конверт'
    })


def registry_list(request):
    registry_objects = Registry.objects.all()
    return render(request, 'registry_json.html', {
        'registry_list': registry_objects,
        'pagename': 'Реестры'
    })


def registry_detail(request, registry_pk=None):
    if request.method == 'POST':
        form = RegistrySentEnvelopForm(request.POST)
        if form.is_valid():
            registry = Registry.objects.get(pk=registry_pk)
            sent_envelop = SentEnvelop()
            user = Employee.objects.get(user=request.user)
            cld = form.cleaned_data
            sent_envelop.username = user
            sent_envelop.recipient = cld['recipient']
            sent_envelop.outer_num = cld['outer_num']
            sent_envelop.envelop_format = cld['envelop_format']
            sent_envelop.registry_type = registry.type
            sent_envelop.rpo_type = registry.rpo_type
            sent_envelop.registry = registry
            sent_envelop.save()
            return redirect('printenvelopsapp:registry_detail', registry_pk=registry_pk)
    else:
        registry = Registry.objects.get(pk=registry_pk)
        form = RegistrySentEnvelopForm(instance=registry)
        registry_template_form = RegistryTemplateForm({'registry': registry_pk})
        sent_envelops_list = SentEnvelop.objects.filter(registry=registry).order_by('pk')
        return render(request, 'registry_detail.html', {
            'form': form,
            'registry_template_form': registry_template_form,
            'registry': registry,
            'sent_envelops_list': sent_envelops_list,
            'pagename': f"Реестр № {registry.num if registry.num is not None else 'б/н'}"
        })


def registry_add(request):
    if request.method == 'POST':
        form = RegistryForm(request.POST)
        if form.is_valid():
            user = Employee.objects.get(user=request.user)
            cld = form.cleaned_data
            registry = Registry()
            registry.username = user
            registry.type = cld['type']
            registry.rpo_type = cld['rpo_type']
            registry.num = cld['num']
            # registry.current_cost = cld['current_cost']
            registry.save()
            envelops = SentEnvelop.objects.filter(registry=None).filter(rpo_type=cld['rpo_type']).filter(
                registry_type=cld['type'])
            envelops.update(registry=registry)
            return redirect('printenvelopsapp:registry_list')
    else:
        pagename = 'Новый реестр'
        form = RegistryForm()
        sent_envelops_list = SentEnvelop.objects.all().order_by('-pk')
        return render(request, 'registry_add.html', {
            'form': form,
            'pagename': pagename,
            'sent_envelops_list': sent_envelops_list
        })


def registry_delete(request, registry_pk):
    registry = Registry.objects.get(pk=registry_pk)
    registry.delete()
    return redirect('printenvelopsapp:registry_list')


def registry_print(request, registry_pk):
    jinja_env = jinja2.Environment()
    jinja_env.filters['get_clear_address'] = tools.get_clear_address
    jinja_env.filters['add_num_before_text'] = tools.add_num_before_text
    jinja_env.filters['without_commas'] = tools.without_commas
    registry = Registry.objects.get(pk=registry_pk)
    template = '{}/{}'.format(settings.MEDIA_ROOT, registry.type.template)
    temporaty_document = DocxTemplate(template)
    output_document = DocxTemplate(template)
    sent_list = SentEnvelop.objects.filter(registry=registry_pk)
    envelops_list_len = len(sent_list)
    date = datetime.datetime.today().strftime("%d.%m.%Y")
    text_date = DateToWords(date)
    text_date = '« {} » {} {}'.format(text_date.get_day(), text_date.get_month_text(), text_date.get_year())
    user = Employee.objects.get(user=request.user)
    envelops_list_len_text = tools.change_neuter_gender_text(
        num2text(envelops_list_len, ((u'отправление', u'отправления', u'отправлений'), 'm')))
    envelops_list_len_pieces = num2text(envelops_list_len, ((u'штука', u'штуки', u'штук'), 'f'))
    envelops_list_len_short = f"{envelops_list_len} " \
        f"({envelops_list_len_pieces.split(' ')[0]}) " \
        f"{envelops_list_len_pieces.split(' ')[1][:2]}."
    current_weight_cost = registry.current_cost
    # for sent in sent_list:
    #     tools.set_sent_cost(current_weight_cost, sent)
    envelops_cost_sum = tools.sum_envelops_cost(sent_list)
    context = {
        'tbl_contents': sent_list,
        'registry_num': registry.num,
        'rpo_type': registry.rpo_type,
        'envelops_list_len': envelops_list_len,
        'envelops_list_len_text': '({}) {}'.format(
            envelops_list_len_text.split()[0],
            envelops_list_len_text.split()[1]),
        'envelops_list_len_pieces': '({}) {}'.format(
            envelops_list_len_pieces.split()[0],
            envelops_list_len_pieces.split()[1]),
        'envelops_cost_sum': envelops_cost_sum,
        'envelops_list_len_short': envelops_list_len_short,
        'date': date,
        'text_date': text_date,
        'post': user.post,
        'fio_short': '{} {}.{}.'.format(user.fio.split()[0], user.fio.split()[1][0], user.fio.split()[1][0])
    }
    datetime_now = datetime.datetime.now()
    temporaty_document.render(context, jinja_env)
    response = HttpResponse(content_type='text/docx')
    response['Content-Disposition'] = 'attachment; filename={}_registry.docx'.format(datetime_now.strftime("%Y.%m.%d_%H-%M"))
    temporery_template_path = '{}/{}'.format(settings.MEDIA_ROOT, 'test.docx')
    temporaty_document.save(temporery_template_path)
    zf = zipfile.ZipFile(temporery_template_path)
    docx_template_settings = str(zf.read('docProps/app.xml'))
    total_number_pages = re.findall(r'<Pages>(\d+)</Pages>', docx_template_settings)[0]
    context['pages_numbers'] = total_number_pages
    output_document.render(context, jinja_env)
    output_document.save(response)
    return response


def sent_envelop_del_from_registry(request, envelop_pk, registry_pk):
    envelop = SentEnvelop.objects.get(pk=envelop_pk)
    envelop.registry = None
    envelop.save()
    return redirect('printenvelopsapp:registry_detail', registry_pk=registry_pk)


def sent_envelop_add_to_registry(request, envelop_pk, registry_pk):
    envelop = SentEnvelop.objects.get(pk=envelop_pk)
    envelop.registry = None
    envelop.save()
    return redirect('printenvelopsapp:registry_detail', registry_pk=registry_pk)


def sent_envelops(request):
    sent_envelops_list = SentEnvelop.objects.all().order_by('-pk')
    return render(request, 'sent_envelops_json.html', {
        'sent_envelops_list': sent_envelops_list,
        'pagename': 'Отправленные'
    })


def sent_delete(request, envelop_pk):
    envelop = SentEnvelop.objects.get(pk=envelop_pk)
    envelop.delete()
    return redirect('printenvelopsapp:sent_envelops')


def sent_detail(request, envelop_id):
    if request.method == 'POST':
        form = PrintEnvelopForm(request.POST)
        if form.is_valid():
            cld = form.cleaned_data
            sent_envelop = SentEnvelop.objects.get(pk=envelop_id)
            sent_envelop.recipient = cld['recipient']
            sent_envelop.registry_type = cld['registry_type']
            sent_envelop.rpo_type = cld['rpo_type']
            sent_envelop.envelop_format = cld['envelop_format']
            sent_envelop.outer_num = cld['outer_num']
            sent_envelop.save()
            return redirect('printenvelopsapp:sent_envelops')
    else:
        envelop_detail = SentEnvelop.objects.get(pk=envelop_id)
        form = PrintEnvelopForm(instance=envelop_detail)
        return render(request, 'sent_detail.html', {
            'form': form,
            'sent_envelop': envelop_detail,
            'pagename': 'Отправление',
        })


class RecepientModelListJson(BaseDatatableView):
    model = Recepient
    columns = ['title', 'address', 'region', 'city', 'postcode', 'sender']

    def render_column(self, row, column):
        if column == 'title':
            return f'<a href="recepient/{row.id}">{row.title}</a>'
        if column == 'sender':
            return f"""<input type="image" form="print_form" onclick="myFunction('{row.id}')" src="/static/base_svg/print.svg" width=20" alt="Submit" />"""
        else:
            return super(RecepientModelListJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(Q(title__icontains=search)|Q(address__icontains=search)|Q(city__icontains=search))


        return qs


class SentModelListJson(BaseDatatableView):
    model = SentEnvelop
    columns = ['recepient', 'date', 'username', 'envelop_format',
               'outer_num', 'rpo_type', 'registry_type', 'registry']

    def render_column(self, row, column):
        if column == 'recepient':
            return f'<a href="sent_detail/{row.id}">{row.recipient}</a>'
        if column == 'date':
            return formats.date_format(row.date, "SHORT_DATETIME_FORMAT")
        if column == 'registry':
            if row.registry:
                return f'<a href="/envelops/registry/{row.registry}">{row.registry}</a>'
            else:
                return ''
        else:
            return super(SentModelListJson, self).render_column(row, column)


class RegistryModelListJson(BaseDatatableView):
    model = Registry
    columns = ['id', 'username', 'date', 'type', 'rpo_type', 'print']

    def render_column(self, row, column):
        if column == 'id':
            return f'<a href="registry/{row.id}">Реестр #{row.num if row.num else " б/н"}</a>'
        if column == 'print':
            return f"""<a href="registry/{row.id}/print"><img src="/static/base_svg/print.svg" width=20"></a>"""
        else:
            return super(RegistryModelListJson, self).render_column(row, column)