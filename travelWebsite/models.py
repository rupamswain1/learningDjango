from django.db import models

# Create your models here.
class Destination(models.Model):
    price = models.FloatField(max_length=1000)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img')