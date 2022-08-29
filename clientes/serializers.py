from .models import Cliente, Cuenta
from rest_framework import serializers 

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
    
        fields = "__all__"
    
        read_only_fields = (
            "nombre",
            "apellido",
            "edad",
            )

class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
    
        fields = "__all__"
    
        read_only_fields = (
            "account_id",
            "customer_id",
            "balance",
            )
