from django.contrib import admin
from .models import *

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["codigo","detalle", "precio", "stock", "oferta", "categoria", "destacado"]
    list_editable = ["stock"]
    search_fields = ["detalle"]
    
class VentaAdmin(admin.ModelAdmin):
    list_display = ["id","fecha", "cliente", "total", "estado"]
    list_editable = ["estado"]
    search_fields = ["cliente"]
    
class DetalleAdmin(admin.ModelAdmin):
    list_display = ["id","cliente","venta", "producto", "cantidad", "precio"]
    search_fields = ["venta"]

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(Detalleventa,DetalleAdmin)
