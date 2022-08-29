from .models import Cliente
from rest_framework import serializers 

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
    #indicamos que use todos los campos
        fields = "__all__"
    #les decimos cuales son los de solo lectura
        read_only_fields = (
            "nombre",
            "apellido",
            "edad",
            )

