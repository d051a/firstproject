from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from certticketapp.models import CertTicketModel, Template
from django.urls import reverse_lazy
from ACCOUNTING.generic.mixins import ContextPageMixin
from certticketapp.forms import CertTicketModelForm
from mailmerge import MailMerge
from django.conf import settings
import datetime



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


def file_generate(request, ticket_pk, template_type):
	template = Template.objects.all().filter(type=template_type).order_by('-date_time')[0]
	user_info = CertTicketModel.objects.get(pk=ticket_pk)
	print('+++++', datetime.datetime.today().strftime("%Y-%m-%d"))
	template = '{}/{}'.format(settings.MEDIA_ROOT, template.file)
	document = MailMerge(template)
	document.merge(
		FIO='{} {} {}'.format(user_info.surname, user_info.name, user_info.middle_name),
		ADDRESS=user_info.registration_address,
		PASSPORT_ISSUED=user_info.passport_issued_by,
		PASSPORT_SERIAL=user_info.passport_series,
		PASSPORT_NUM=user_info.passport_num,
		PASSPORT_DATE=str(get_date(user_info.passport_date)),
		PASSPORT_DCODE=user_info.passport_unit_code,
		POST=user_info.position,
		FULL_DATE=get_date(datetime.datetime.today().strftime("%Y-%m-%d"), format=1)
	)

	response = HttpResponse(content_type='text/docx')
	response['Content-Disposition'] = 'attachment; filename=download.docx'
	document.write(response)
	return response


def get_date(date, format=None):
	day_list = ['первое', 'второе', 'третье', 'четвёртое',
		'пятое', 'шестое', 'седьмое', 'восьмое',
		'девятое', 'десятое', 'одиннадцатое', 'двенадцатое',
		'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
		'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
		'двадцать первое', 'двадцать второе', 'двадцать третье',
		'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое',
		'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
		'тридцатое', 'тридцать первое']
	month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
		   'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
	years_ends_list = ['первого', 'второго', 'третьего', 'четвёртого',
		'пятого', 'шестого', 'седьмого', 'восьмого',
		'девятого', 'десятого', 'одиннадцатого', 'двенадцатого',
		'тринадцатого', 'четырнадцатого', 'пятнадцатого', 'шестнадцатого',
		'семнадцатого', 'восемнадцатого', 'девятнадцатого', 'двадцатого',
		'двадцать первого', 'двадцать второго', 'двадцать третьго',
		'двадацать четвёртого', 'двадцать пятого', 'двадцать шестого',
		'двадцать седьмого', 'двадцать восьмого', 'двадцать девятого',
		'тридцатого', 'тридцать первого']
	date_list = str(date).split('-')
	day_out = day_list[int(date_list[2]) - 1]
	month_out = month_list[int(date_list[1]) - 1]
	year_out = years_ends_list[int(str(date_list[0][2:])) - 1]
	if format == 1:
		return ('{} {} две тысячи {} года'.format(day_out, month_out, year_out))
	else:
		return ('{} {} {}'.format(date_list[2], month_out, date_list[0]))


