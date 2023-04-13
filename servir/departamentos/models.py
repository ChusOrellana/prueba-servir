from django.db import models

class Departamento(models.Model):
    codigo = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"