
from django.db import models

class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    logo = models.ImageField(upload_to='tecnologias/', null=True, blank=True)
    website_oficial = models.URLField(blank=True)
    nivel_preferencia = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "Tecnologias"

    def __str__(self):
        return self.nome