from django.contrib import admin
from .models import Technic, Department, SubDevision
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Technic)
admin.site.register(Department)
admin.site.register(SubDevision)
