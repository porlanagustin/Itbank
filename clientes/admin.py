from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    readonly_fields= ('nombre','apellido')

admin.site.register(Cliente)