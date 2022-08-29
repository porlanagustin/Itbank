from distutils.log import error
from email import message
from clientes.models import Cliente
from clientes.serializers import ClienteSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ClienteDetails(APIView):
    def get(self, request, pk):
        cliente = Cliente.objects.filter(pk=pk).first()

        serializer = ClienteSerializer(cliente)

        if cliente:
            return Response(serializer.data, status = status.HTTP_200_OK)

        error1 = {"message": "NO SE ENCUENTRA EL CLIENTE"}
        return Response(str(error1), status= status.HTTP_404_NOT_FOUND)   

class ClienteLists(APIView):
        def post(self, request, format=None):
            serializer = ClienteSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)