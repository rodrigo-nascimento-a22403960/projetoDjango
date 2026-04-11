from django.db import models

class Licenciatura(models.Model):
    nome = models.CharField(max_length=150)
    sigla = models.CharField(max_length=10)
    descricao = models.TextField()
    duracao_anos = models.PositiveIntegerField()
    ects_total = models.PositiveIntegerField()

    def __str__(self):
        return self.nome

class Docente(models.Model):
    nome = models.CharField(max_length=100)
    pagina_pessoal_url = models.URLField()
    imagem = models.ImageField(upload_to='docentes/', null=True, blank=True)

    def __str__(self):
        return self.nome