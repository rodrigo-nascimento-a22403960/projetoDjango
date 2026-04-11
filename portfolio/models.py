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

class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=150)
    ano_curricular = models.PositiveIntegerField()
    semestre = models.PositiveIntegerField()
    ects = models.PositiveIntegerField()
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='ucs/')
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE)
    docentes = models.ManyToManyField(Docente)

    class Meta:
        verbose_name_plural = "Unidades Curriculares"

    def __str__(self):
        return self.nome

class TFC(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    resumo = models.TextField()
    ano = models.PositiveIntegerField()
    destaque = models.BooleanField(default=False)
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Trabalhos Finais de Curso (TFCs)"

    def __str__(self):
        return self.titulo