from django.db import models
from django.contrib.auth.models import User


class Almacen(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    capital = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    responsable = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

