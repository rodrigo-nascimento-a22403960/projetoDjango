from django.db import models

class MakingOf(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    decisoes = models.TextField(blank=True)
    erros_correcoes = models.TextField(blank=True)
    uso_ia = models.TextField(blank=True)
    data = models.DateField(auto_now_add=True)
    foto_papel = models.ImageField(upload_to='makingof/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Making Of"
        ordering = ['-data']

    def __str__(self):
        return self.titulo