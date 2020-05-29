from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Recepient, Envelop, SecretType, SentEnvelop, Registry
from ACCOUNTING import settings
from .forms import RecipientForm, EnvelopeFormatModelForm, PrintEnvelopForm, RegistryForm, RegistryTemplateForm
from docxtpl import DocxTemplate
from .main import DateToWords
from employeesapp.models import Employee
from printenvelopsapp.num2t4ru import num2text
import datetime
import zipfile
import re
import jinja2


def env_generate(request, envelop_data):
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

    response = HttpResponse(content_type='text/docx')
    response['Content-Disposition'] = 'attachment; filename=download.docx'
    output_document.save(response)
    return response


def recepients(request):
    recepients_list = Recepient.objects.order_by("-pk")
    envelop_list = Envelop.objects.all()
    secret_types_list = SecretType.objects.all()
    return render(request, 'recepients.html', {
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
            'pagename': 'Адресат'
        })


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


def add_to_sent_envelops_list(recepient_data=None, envelop_data=None, secret_data=None):
    recepient = Recepient.objects.get(pk=recepient_data)
    envelop = Envelop.objects.get(pk=envelop_data)
    secret = SecretType.objects.get(pk=secret_data)
    return None


def sent_envelops(request):
    sent_envelops_list = SentEnvelop.objects.all().order_by('-pk')
    return render(request, 'sent_envelops.html', {
        'sent_envelops_list': sent_envelops_list,
        'pagename': 'Отправленные'
    })


def print_envelop(request):
    if request.method == 'POST':
        form = PrintEnvelopForm(request.POST)
        if form.is_valid():
            cld = form.cleaned_data
            envelop = SentEnvelop()
            envelop.recipient = cld['recipient']
            envelop.rpo_type = cld['rpo_type']
            envelop.envelop_format = cld['envelop_format']
            envelop.outer_num = cld['outer_num']
            envelop.registry_type = cld['registry_type']
            envelop.save()
            return env_generate(request, cld)
    else:
        form = PrintEnvelopForm()
    return render(request, 'print_envelop.html', {
        'form': form,
        'pagename': 'Печать конверта'
    })


def registry_list(request):
    registry_objects = Registry.objects.all()
    return render(request, 'registry.html', {
        'registry_list': registry_objects,
        'pagename': 'Реестры'
    })


def registry_detail(request, registry_pk=None):
    if request.method == 'POST':
        form = RegistryForm(request.POST)
        if form.is_valid():
            cld = form.cleaned_data
            registry = Registry.objects.get(pk=registry_pk)
            registry.type = cld['type']
            registry.rpo_type = cld['rpo_type']
            registry.save()
            return redirect('printenvelopsapp:registry_list')
    else:
        registry = Registry.objects.get(pk=registry_pk)
        form = RegistryForm(instance=registry)
        registry_template_form = RegistryTemplateForm({'registry': registry_pk})
        sent_envelops_list = SentEnvelop.objects.filter(registry=registry)
        return render(request, 'registry_detail.html', {
            'form': form,
            'registry_template_form': registry_template_form,
            'registry': registry,
            'sent_envelops_list': sent_envelops_list,
            'pagename': 'Реестр №' + registry_pk
        })


def sent_envelop_del_from_registry(request, envelop_pk, registry_pk):
    envelop = SentEnvelop.objects.get(pk=envelop_pk)
    envelop.registry = None
    envelop.save()
    return redirect('printenvelopsapp:registry_detail', registry_pk=registry_pk)


def registry_delete(request, registry_pk):
    registry = Registry.objects.get(pk=registry_pk)
    registry.delete()
    return redirect('printenvelopsapp:registry_list')


def sent_envelop_add_to_registry(request, envelop_pk, registry_pk):
    envelop = SentEnvelop.objects.get(pk=envelop_pk)
    envelop.registry = None
    envelop.save()
    return redirect('printenvelopsapp:registry_detail', registry_pk=registry_pk)


def registry_print(request):
    def get_clear_address(address):
        clear_address = address.split(',')
        return str(clear_address[0])

    def add_num_before_text(text):
        text_with_num = f'№ {text}'
        return text_with_num

    jinja_env = jinja2.Environment()
    jinja_env.filters['get_clear_address'] = get_clear_address
    jinja_env.filters['add_num_before_text'] = add_num_before_text
    registry_pk = request.GET['registry']
    registry = Registry.objects.get(pk=registry_pk)
    template = '{}/{}'.format(settings.MEDIA_ROOT, registry.type.template)
    temporaty_document = DocxTemplate(template)
    output_document = DocxTemplate(template)
    envelops_list = SentEnvelop.objects.filter(registry=registry_pk)
    envelops_list_len = len(envelops_list)
    date = datetime.datetime.today().strftime("%d.%m.%Y")
    text_date = DateToWords(date)
    text_date = '« {} » {} {}'.format(text_date.get_day(), text_date.get_month_text(), text_date.get_year())
    user = Employee.objects.get(user=request.user)
    envelops_list_len_text = num2text(envelops_list_len, ((u'отправление', u'отправления', u'отправлений'), 'f'))
    envelops_list_len_pieces = num2text(envelops_list_len, ((u'штука', u'штуки', u'штук'), 'f'))
    context = {
        'tbl_contents': envelops_list,
        'registry_id': registry_pk,
        'rpo_type': registry.rpo_type,
        'envelops_list_len': envelops_list_len,
        'envelops_list_len_text': '({}) {}'.format(
            envelops_list_len_text.split()[0],
            envelops_list_len_text.split()[1]),
        'envelops_list_len_pieces': '({}) {}'.format(
            envelops_list_len_pieces.split()[0],
            envelops_list_len_pieces.split()[1]),
        'date': date,
        'text_date': text_date,
        'post': user.post,
        'fio_short': '{} {}.{}.'.format(user.fio.split()[0], user.fio.split()[1][0], user.fio.split()[1][0])
    }
    temporaty_document.render(context, jinja_env)
    response = HttpResponse(content_type='text/docx')
    response['Content-Disposition'] = 'attachment; filename=download.docx'
    temporery_template_path = '{}/{}'.format(settings.MEDIA_ROOT, 'test.docx')
    temporaty_document.save(temporery_template_path)
    zf = zipfile.ZipFile(temporery_template_path)
    docx_template_settings = str(zf.read('docProps/app.xml'))
    total_number_pages = re.findall(r'<Pages>(\d+)</Pages>', docx_template_settings)[0]
    context['pages_numbers'] = total_number_pages
    output_document.render(context, jinja_env)
    output_document.save(response)
    return response


def registry_add(request):
    if request.method == 'POST':
        form = RegistryForm(request.POST)
        if form.is_valid():
            cld = form.cleaned_data
            registry = Registry()
            registry.type = cld['type']
            registry.rpo_type = cld['rpo_type']
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
