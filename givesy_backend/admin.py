from django.contrib import admin
from .models import User, Product, Image
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass