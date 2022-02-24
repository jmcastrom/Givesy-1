from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # Django already has name, password, email, etc
    class UserRoles(models.TextChoices):
        Seller = "Seller" 
        Buyer = "Buyer"

    role = models.CharField(choices=UserRoles.choices, default=UserRoles.Seller, max_length=20)
    
    def create_user(self):
        super().save()
    
    def edit_user(self):
        super().save()
    
    def delete_user(self):
        super().delete()
    
    def get_user(self):
        self.objects.get(self)
    
    def __str__(self):
        return f"User: {self.first_name} {self.last_name}"

class Product(models.Model):
    title = models.CharField(max_length=30)
    decription = models.TextField(blank=False, null = False)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    def __str__(self):
        return f"Product: {self.title}"

class Image(models.Model):
    image = models.ImageField()
    product = models.ForeignKey("Product", on_delete=models.CASCADE)

    def __str__(self):
        return f"image for product: {self.product.title}"