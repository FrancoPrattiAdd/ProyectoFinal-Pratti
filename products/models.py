from django.db import models
from django.conf import settings
from account.models import Usuario

# Modelo del producto
class Producto(models.Model):
    nombre = models.CharField(max_length=100)  
    descripcion = models.TextField() 
    precio = models.DecimalField(max_digits=10, decimal_places=2) 
    imagen = models.ImageField(upload_to='imagenes_productos/') 
    
    def __str__(self):
        return self.nombre 

# Modelo del carrito
class Carrito(models.Model):
    usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='CarritoProducto')

    def __str__(self):
        return f"Carrito de {self.usuario}"

    def total_items(self):
        return sum(item.cantidad for item in self.carritoproducto_set.all())

    def total_price(self):
        return sum(item.producto.precio * item.cantidad for item in self.carritoproducto_set.all())

    

class CarritoProducto(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"