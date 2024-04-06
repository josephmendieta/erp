from django.contrib import admin
from controlVentas.models import resumenVenta

class ControlVentasAdmin(admin.ModelAdmin):
    list_display = ["nombreTienda", "barrioTienda", "total", "articulosVendidos", "fechaVenta", "nombreVendedor"]

admin.site.register(resumenVenta, ControlVentasAdmin)
