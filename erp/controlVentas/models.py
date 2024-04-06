from django.db import models

class resumenVenta(models.Model):

    nombreTienda = models.CharField(max_length=120)
    barrioTienda = models.CharField(max_length=120)
    numLocalidad = models.IntegerField()
    total = models.IntegerField()
    recibido = models.IntegerField()
    cambio = models.IntegerField()
    articulosVendidos = models.IntegerField()
    fechaVenta = models.DateTimeField(auto_now_add=False)
    nombreVendedor = models.CharField(max_length=120)
