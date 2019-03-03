from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import render
from .models import Certificate, Persone
from .forms import CertificateModelForm, PersoneModelForm, FileFieldForm
from django.contrib.auth.decorators import login_required
from OpenSSL import crypto


def certificate_add(request):
    pass


class MainView(TemplateView):
    template_name = 'certificatesapp/certificates.html'
    def get(self, request):
        if request.user.is_authenticated:
            certs_list = Certificate.objects.order_by("-validate_end_date")
            context = {'certs_list': certs_list}
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name, {})


class PersonesMainView(TemplateView):
    template_name = 'certificatesapp/persones.html'
    def get(self, request):
        if request.user.is_authenticated:
            persones_list = Persone.objects.order_by("fullname")
            context = {'persones_list': persones_list}
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name, {})


class CertificateEdit(TemplateView):
    template_name = 'certificatesapp/certificate_edit.html'
    def get(self, request, certificate_id):
        if request.GET == {'del': ['true']}:
            return certificate_delete(request, certificate_id)
        else:
            certificate = Certificate.objects.get(pk=certificate_id)
            data = {'fullname': certificate.fullname,
                    'validate_start_date': certificate.validate_start_date,
                    'validate_end_date': certificate.validate_end_date,
                    'cert_file': certificate.cert_file,
                    'email': certificate.email}
            form = CertificateModelForm(data)
        return render(request, 'certificatesapp/certificate_edit.html', {'form': form,
                                                                        'fullname': certificate.fullname
                                                                         })


"""@login_required
def persone_edit(request, persone_id):
    print('GET:', request.GET)
    if request.method == 'GET' and request.GET == {'del': ['true']}:
        return persone_delete(request, persone_id)
    else:
        persone = Persone.objects.get(pk = persone_id)
        certificate_list = Certificate.objects.all().filter(fullname = persone.fullname)
        data = {'fullname': persone.fullname,
                'snils': persone.snils,
                'inn': persone.inn,
                }
        form = PersoneModelForm(data)
    return render (request, 'certificatesapp/persone_edit.html', {'form': form,
                                                            'fullname': persone.fullname,
                                                            'certificate_list': certificate_list})"""

class PersoneEdit(TemplateView):
    template_name = 'certificatesapp/persone_edit.html'
    def get(self, request, persone_id):
        if request.GET == {'del': ['true']}:
            return persone_delete(request, persone_id)
        else:
            persone = Persone.objects.get(pk = persone_id)
            certificate_list = Certificate.objects.all().filter(fullname = persone.fullname)
            data = {'fullname': persone.fullname,
                    'snils': persone.snils,
                    'inn': persone.inn,
                    }
            form = PersoneModelForm(data)
        return render (request, 'certificatesapp/persone_edit.html', {'form': form,
                                                                'fullname': persone.fullname,
                                                                'certificate_list': certificate_list})


@login_required
def certificate_delete(request, certificate_id):
    if request.method == 'GET':
        certificate = Certificate.objects.get(pk = certificate_id)
        certificate.delete()
    return HttpResponseRedirect('/')


@login_required
def persone_delete(request, persone_id):
    if request.method == 'GET':
        persone = Persone.objects.get(pk = persone_id)
        persone.delete()
    return HttpResponseRedirect('/persones/')


class FileFieldView(FormView): #load certificates
    form_class = FileFieldForm
    template_name = 'certificatesapp/certificate_add.html'
    success_url = '/'
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class() #get class forms
        form = self.get_form(form_class) #get html-form
        files = request.FILES.getlist('file_field') #get list of added user files
        if form.is_valid():
            for file in files:
                x509 = crypto.load_certificate(crypto.FILETYPE_ASN1, file.read())
                list = x509.get_subject().get_components()
                cert_dict = {}
                for elem in list: cert_dict[elem[0].decode("utf-8")] = elem[1].decode("utf-8")
                cert_valid_end = x509.get_notAfter().decode("utf-8") # get date of certificate validity
                cert_valid_start = x509.get_notBefore().decode("utf-8") # get certificate expiration date
                year_s, month_s, day_s = cert_valid_start[0:4], cert_valid_start[4:6], cert_valid_start[6:8]
                year_e, month_e, day_e = cert_valid_end[0:4], cert_valid_end[4:6], cert_valid_end[6:8]
                cert_valid_start = '{}-{}-{}'.format(year_s, month_s, day_s) #format date of certificate validity
                cert_valid_end = '{}-{}-{}'.format(year_e, month_e, day_e)#format certificate expiration date
                FIO = cert_dict['CN']
                email = cert_dict['emailAddress']
                SNILS = cert_dict['SNILS']
                INN = cert_dict['INN']
                try: #try add persone
                    persone = Persone(fullname = FIO, inn = INN, snils = SNILS)
                    persone.save()
                except: #if persone exists
                    pass
                add_cert = Certificate(fullname=FIO,
                                        validate_start_date=cert_valid_start,
                                        validate_end_date = cert_valid_end,
                                        email = email,
                                        cert_file = file,
                                        persone = Persone.objects.get(fullname=FIO)
                                       )
                add_cert.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


"""@login_required
def certificate_edit(request, certificate_id):
    if request.method == 'GET' and request.GET == {'del': ['true']}:
        return certificate_delete(request, certificate_id)
    else:
        certificate = Certificate.objects.get(pk = certificate_id)
        data = {'fullname': certificate.fullname,
                'validate_start_date': certificate.validate_start_date,
                'validate_end_date': certificate.validate_end_date,
                'cert_file': certificate.cert_file,
                'email':certificate.email}
        form = CertificateModelForm(data)
    return render (request, 'certificatesapp/certificate_edit.html', {'form': form,
                                                                'fullname': certificate.fullname,})    """



"""class CertificateEdit(FormView):
    template_name = 'certificatesapp/certificate_add.html'
    form_class = CertificateModelForm
    success_url = '/'
    def form_valid(self, form):
        form.save()
        return super(CertificateEdit, self).form_valid(form)"""

"""def certificate_add(request):
    if request.method == 'POST':
        form = CertificateAddModelForm(request.POST, request.FILES)
        if form.is_valid():
            file_obj = request.FILES['cert_file']
            x509 = crypto.load_certificate(crypto.FILETYPE_ASN1, file_obj.read())
            json.dump({name.decode(): value.decode('utf-8')
            for name, value in x509.get_subject().get_components()},
            sys.stdout, indent=2, ensure_ascii=False)
        return HttpResponseRedirect ('/certificates/add_cert')
    else:
        form = CertificateAddModelForm()
    return render (request, 'certificatesapp/certificate_edit.html', {'form': form})"""