from django.contrib import admin
from .models import User, Categoria, Producto, Imagen, Orden

admin.site.register(User)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Imagen)
admin.site.register(Orden)
