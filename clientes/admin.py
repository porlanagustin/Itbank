from django.contrib import admin
from .models import Cliente, Cuenta, TipoCliente

admin.site.register(Cuenta)
admin.site.register(Cliente)
admin.site.register(TipoCliente)
