from django.contrib import admin
from .models import Cliente, Cuenta

class ClienteAdmin(admin.ModelAdmin):
    readonly_fields= ('nombre','apellido')

admin.site.register(Cliente)
admin.site.register(Cuenta)