from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(default=datetime.now())
    cliente = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total = models.IntegerField()
    estado = models.CharField(max_length=20, default="EN PREPARACION")
    
    def __str__(self):
        return str(self.fecha)[0:20]



class Producto(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    detalle = models.CharField(max_length=200)
    precio = models.IntegerField()
    stock = models.IntegerField()
    oferta = models.BooleanField()
    imagen = models.CharField(max_length=200)
    categoria = models.CharField(max_length=20, default="semilla")
    destacado = models.BooleanField(default=False)  
    
    def tachado(self):
        if self.oferta:
            return "$"+str(round(self.precio * 1.2))
        return ""
    
    def __str__(self):
        return self.detalle+"("+self.codigo+")"
    
class Detalleventa(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    venta = models.ForeignKey(to=Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(to=Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self):
        return str(self.id)+" - "+self.producto.detalle[0:20]+" "+str(self.venta.id)