from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=500)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

