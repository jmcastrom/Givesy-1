from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_lenght = 100)
    description = models.Charfield(max_lenght = 250)
    image = models.ImageField(upload_to='movie/images/')
    url = models.URLField(blank=True)