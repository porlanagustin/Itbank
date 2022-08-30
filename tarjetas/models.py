from django.db import models
from clientes.models import Cliente 

class Tarjeta(models.Model):
    nombre = models.CharField(max_length=20)
    numero = models.IntegerField()
    cvv = models.IntegerField()
    vto = models.DateTimeField()
    tipo = models.TextField(max_length=20)
    customer_id= models.ForeignKey(Cliente,null=True, blank=True, on_delete=models.CASCADE) 

    class Meta:
        verbose_name = "Tarjeta"
        verbose_name_plural = "Tarjetas"

    def __str__(self):
        return self.nombre