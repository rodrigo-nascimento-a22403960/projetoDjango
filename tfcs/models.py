from django.db import models

class TFC(models.Model):
    titulo = models.CharField(max_length=200)
    autores = models.CharField(max_length=300, blank=True)
    orientadores = models.CharField(max_length=300, blank=True)
    licenciaturas = models.CharField(max_length=200, blank=True)
    sumario = models.TextField(blank=True)
    link_pdf = models.URLField(blank=True)
    imagem = models.URLField(blank=True)
    palavras_chave = models.TextField(blank=True)
    areas = models.TextField(blank=True)
    tecnologias_usadas = models.TextField(blank=True)
    rating = models.PositiveIntegerField(default=0)
    destaque = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "TFCs"

    def __str__(self):
        return self.titulo