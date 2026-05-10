from django.db import models

from django.db import models
from users.models import Usuario
from categorias.models import Categoria

class Presupuesto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    monto_limite = models.DecimalField(max_digits=10, decimal_places=2)
    mes = models.IntegerField()
    año = models.IntegerField()

    def __str__(self):
        return f"{self.usuario} - {self.mes}/{self.año}"
