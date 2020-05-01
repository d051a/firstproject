from django.contrib import admin
from .models import Recepient, EnvelopFormat, Envelop, SecretType, RPOType, SentEnvelop, Registry, RegistryTemplate, RegistryType


admin.site.register(Recepient)
admin.site.register(EnvelopFormat)
admin.site.register(Envelop)
admin.site.register(SecretType)
admin.site.register(RPOType)
admin.site.register(SentEnvelop)
admin.site.register(Registry)
admin.site.register(RegistryTemplate)
admin.site.register(RegistryType)


class SecretType(admin.ModelAdmin):
    fields = ('short_name', 'name')

