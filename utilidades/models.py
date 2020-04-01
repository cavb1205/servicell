from django.db import models

from almacenes.models import Almacen

class Utilidad(models.Model):
    descripcion = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    almacen_id = models.ForeignKey(Almacen, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion