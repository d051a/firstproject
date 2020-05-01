from django.db import models
from django.core.validators import MinLengthValidator


class Address(models.Model):
	LEGAL = 'LG'
	POSTAL = 'PL'
	FACT = 'FT'
	address_type = (
		(LEGAL, 'Юридический'),
		(FACT, 'Фактический'),
		(POSTAL, 'Почтовый'),
	)
	address = models.CharField('Адрес', max_length=100)
	city = models.CharField('Город', max_length=20)
	index = models.CharField('Индекс', max_length=6)
	choices = models.CharField('Тип адреса', max_length=2, choices=address_type, default=FACT)

	class Meta:
		permissions = (
			('can_view_envelop_addreses', 'Может просматривать список адресов'),
			('can_add_envelop_addreses', 'Может добавлять адресы'),
			('can_delete_envelop_addreses', 'Может удалять адресы'),
		)
		ordering = ['address']
		verbose_name = 'Адрес'
		verbose_name_plural = 'Адресы'

	def __str__(self):
		return self.city + ' ' + self.address


class Recepient(models.Model):
	title = models.CharField('Наименование адресата', max_length=100)
	pub_date = models.DateField('Дата публикации', auto_now_add=True)
	address = models.CharField('Адрес', max_length=100)
	region = models.CharField('Регион(область)', max_length=100)
	city = models.CharField('Регион(область)', max_length=100)
	postcode = models.CharField('Индекс', max_length=6, validators=[MinLengthValidator(6)], null=True)
	sender = models.BooleanField('Признак отправителя', default=False)

	class Meta:
		permissions = (
			('can_view_envelop_recepients', 'Может просматривать список адресатов'),
			('can_add_envelop_recepients', 'Может добавлять адресатов'),
			('can_delete_envelop_recepients', 'Может удалять адресатов'),
		)
		ordering = ['title']
		verbose_name = 'Получатель'
		verbose_name_plural = 'Получатели'

	def __str__(self):
		return self.title


class EnvelopFormat(models.Model):
	env_form_title = models.CharField('Формат конверта', max_length=30)

	class Meta:
		permissions = (
			('can_view_envelop_formats', 'Может просматривать список форматов конвертов'),
			('can_add_envelop_formats', 'Может добавлять форматы конвертов'),
			('can_delete_envelop_formats', 'Может удалять форматы конвертов'),
		)
		ordering = ['pk']
		verbose_name = 'Формат конверта'
		verbose_name_plural = 'Форматы конвертов'

	def __str__(self):
		return self.env_form_title


class Envelop(models.Model):
	env_title = models.CharField('Название конверта', max_length=30)
	envelop_format = models.ForeignKey(EnvelopFormat)
	envelop_template = models.FileField('Шаблон конверта')

	class Meta:
		permissions = (
			('can_view_envelop_templates', 'Может просматривать список шаблонов конвертов'),
			('can_add_envelop_templates', 'Может добавлять шаблонов конвертов'),
			('can_delete_envelop_templates', 'Может удалять шаблонов конвертов'),
		)
		ordering = ['-pk']
		verbose_name = 'Конверт'
		verbose_name_plural = 'Конверты'

	def __str__(self):
		return self.env_title


class SecretType(models.Model):
	short_name = models.CharField('Сокращенное название', max_length=15)
	name = models.CharField('Отображаемое название', max_length=30, blank=True)
	visible = models.BooleanField('Видимость', default=True)

	class Meta:
		ordering = ['short_name']
		verbose_name = 'Тип секретности'
		verbose_name_plural = 'Типы секретности'

	def __str__(self):
		return self.name


class SentEnvelop(models.Model):
	recipient = models.ForeignKey('Recepient', verbose_name='Получатель')
	date = models.DateTimeField('Дата и время создания', auto_now=True)
	username = models.CharField('Исполнитель', max_length=1, blank=True)
	rpo_type = models.ForeignKey('RPOType', null=True, verbose_name='Вид РПО')
	secret_type = models.ForeignKey('printenvelopsapp.SecretType', null=True, verbose_name='Тип секретности')
	envelop_format = models.ForeignKey('printenvelopsapp.Envelop', null=True, verbose_name='Формат конверта')
	outer_num = models.CharField('Исходящий номер', max_length=100, blank=True)
	registry_type = models.ForeignKey('printenvelopsapp.RegistryType', verbose_name='Тип реестра')
	registry = models.ForeignKey('printenvelopsapp.Registry', on_delete=models.SET_NULL, null=True, blank=True)

	class Meta:
		permissions = (
			('can_view_envelop_sent', 'Может просматривать список отправленных конвертов'),
			('can_add_envelop_sent', 'Может добавлять отправленных конвертов'),
			('can_delete_envelop_sent', 'Может удалять отправленных конвертов'),
		)
		ordering = ['-pk']
		verbose_name = 'Отправленое'
		verbose_name_plural = 'Отправленные'

	def __str__(self):
		return str(self.pk)


class RPOType(models.Model):
	name = models.CharField('Название РПО', max_length=50)
	short_name = models.CharField('Краткое название', max_length=25)

	class Meta:
		permissions = (
			('can_view_envelop_rpotype', 'Может просматривать список видов РПО'),
			('can_add_envelop_rpotype', 'Может добавлять виды РПО'),
			('can_delete_envelop_rpotype', 'Может удалять виды РПО'),
		)
		ordering = ['name']
		verbose_name = 'Вид РПО'
		verbose_name_plural = 'Виды РПО'

	def __str__(self):
		return self.name


class Registry(models.Model):
	REGISTRY_TYPE_CHOICES = (
		('1', 'МО РФ'),
		('2', 'МО РФ'),
		('3', 'ГФС иное'),
		('4', 'ГФС москва'),
		('5', 'почта ФПС'),
		('6', 'почта России'),
		('7', 'посылки'),
	)
	date = models.DateField('Дата', auto_now_add=True)
	type = models.ForeignKey('printenvelopsapp.RegistryType', verbose_name='Тип реестра')
	rpo_type = models.ForeignKey('RPOType', verbose_name='Тип РПО', null=True, blank=True)

	class Meta:
		ordering = ['-pk']
		verbose_name = 'Реестр'
		verbose_name_plural = 'Реестры'

	def __str__(self):
		return str(self.pk)


class RegistryTemplate(models.Model):
	title = models.CharField('Название шаблона', max_length=30)
	template = models.FileField('Шаблон реестра')

	class Meta:
		permissions = (
			('can_view_envelop_registry_templ', 'Может просматривать список шаблонов реестров'),
			('can_add_envelop_registry_templ', 'Может добавлять шаблоны реестров'),
			('can_delete_envelop_registry_templ', 'Может удалять шаблоны реестров'),
		)
		ordering = ['-pk']
		verbose_name = 'Шаблон реестра'
		verbose_name_plural = 'Шаблоны реестра'

	def __str__(self):
		return self.title


class RegistryType(models.Model):
	title = models.CharField('Название реестра', max_length=30)
	template = models.FileField('Шаблон реестра')

	class Meta:
		permissions = (
			('can_view_envelop_registry_type', 'Может просматривать список типов реестров'),
			('can_add_envelop_registry_type', 'Может добавлять типы реестров'),
			('can_delete_envelop_registry_type', 'Может удалять типы реестров'),
		)
		ordering = ['-pk']
		verbose_name = 'Тип реестра'
		verbose_name_plural = 'Типы реестра'

	def __str__(self):
		return self.title