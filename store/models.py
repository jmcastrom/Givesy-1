from django.db import models
from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField

class User(AbstractUser):
    class Roles(models.TextChoices):
        vendedor = "Vendedor" 
        comprador = "Comprador"

    rol = models.CharField(choices=Roles.choices, default=Roles.vendedor, max_length=20)
    
    def __str__(self):
        return f"User: {self.first_name} {self.last_name}"

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    slug = models.SlugField() # new
    
    def __str__(self):
        return f"Categoria: {self.nombre}"

class Producto(models.Model):
    class Estados(models.TextChoices):
        activo = "activo" 
        vendido = "vendido"
        desactivado = "desactivado"
    
    titulo = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from='titulo')
    descripcion = models.TextField(blank=False, null = False)
    categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE)
    vendedor = models.ForeignKey("User", on_delete=models.CASCADE)
    destacado = models.BooleanField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    estado = models.CharField(choices=Estados.choices, default=Estados.activo, max_length=20)
    
    def __str__(self):
        return f"Producto: {self.titulo}"

class Imagen(models.Model):
    imagen = models.ImageField()
    producto = models.ForeignKey("Producto", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"image for product: {self.producto.titulo}"

class Orden(models.Model):
    class Estados(models.TextChoices):
        reservado = "reservado" 
        comprado = "comprado"
        entregado = "entregado"
    
    producto = models.ForeignKey("Producto", on_delete=models.CASCADE)
    comprador = models.ForeignKey("User", on_delete=models.CASCADE)
    estado = models.CharField(choices=Estados.choices, default=Estados.reservado, max_length=20)
    def __str__(self):
        return f"Producto: {self.producto.titulo} del User: {self.producto.vendedor.first_name}, para el User: {self.comprador.first_name}"