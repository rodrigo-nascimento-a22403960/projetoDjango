


from django.db import models

class Formacao(models.Model):
    nome = models.CharField(max_length=150)
    instituicao = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    certificado_url = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = "Formações"
        ordering = ['-data_inicio']

    def __str__(self):
        return self.nome