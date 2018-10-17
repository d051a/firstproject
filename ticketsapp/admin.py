from django.contrib import admin
from .models import MainProblem, SubProblem, Ticket

# Register your models here.
admin.site.register(MainProblem)
admin.site.register(SubProblem)
admin.site.register(Ticket)
