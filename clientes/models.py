from django.db import models

class Cliente(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_DNI = models.CharField(max_length=10,null=True)
    customer_name = models.CharField(max_length=50,null=True)
    customer_surname = models.CharField(max_length=50,null=True)
    branch_id = models.CharField(max_length=50)
    

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.customer_name