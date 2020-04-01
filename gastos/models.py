from django.db import models

from almacenes.models import Almacen


class Tipo_Gasto(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Gasto(models.Model):
    gasto_id = models.ForeignKey(Tipo_Gasto, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    almacen_id = models.ForeignKey(Almacen, on_delete=models.CASCADE)

    def __str__(self):
        return self.gasto_id.nombre