from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, 
    decimal_places=2)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)

    def __str__(self):
        return self.name 
