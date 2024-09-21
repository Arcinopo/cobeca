from django.db import models
from django.contrib.auth.models import User

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    Proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    
class Cliente(models.Model):
    nombre=models.CharField(max_length=100)
    telefono=models.CharField(max_length=20)
    direccion=models.CharField(max_length=255)
    email=models.EmailField()

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10,decimal_places=2)

class Detalle_venta(models.Model):
    Venta=models.ForeignKey(Venta,on_delete=models.CASCADE)
    Producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10,decimal_places=2)
