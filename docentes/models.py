

from django.db import models

class Docente(models.Model):
    nome = models.CharField(max_length=100)
    pagina_pessoal_url = models.URLField()
    imagem = models.ImageField(upload_to='docentes/', null=True, blank=True)

    def __str__(self):
        return self.nome