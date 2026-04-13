
from django.db import models

class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    nivel = models.PositiveIntegerField()
    descricao = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Competências"

    def __str__(self):
        return self.nome