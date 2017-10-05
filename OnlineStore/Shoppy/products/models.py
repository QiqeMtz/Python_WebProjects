from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    # Funcion para nombrar al objeto con el valor que se le defina en el modelo
    def __str__(self):
        return self.name