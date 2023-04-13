from django.db import models


class Empleado(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    departamento = models.ForeignKey("departamentos.Departamento", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self._state.adding:
            ultimo_empleado = Empleado.objects.all().order_by("-codigo").first()
            numero = 1

            if ultimo_empleado:
                numero = int(ultimo_empleado.codigo[4:]) + 1

            self.codigo = 'EMP-{:04d}'.format(numero)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.codigo} - {self.nombres} {self.apellidos}"
