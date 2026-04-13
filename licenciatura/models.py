from django.db import models

class Licenciatura(models.Model):
    nome = models.CharField(max_length=150)
    sigla = models.CharField(max_length=10)
    descricao = models.TextField()
    duracao_anos = models.PositiveIntegerField()
    ects_total = models.PositiveIntegerField()

    def __str__(self):
        return self.nome


class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=150)
    codigo = models.CharField(max_length=50, blank=True)
    ano_curricular = models.PositiveIntegerField()
    semestre = models.PositiveIntegerField(default=1)
    ects = models.PositiveIntegerField()
    natureza = models.CharField(max_length=50, blank=True)
    objetivos = models.TextField(blank=True)
    apresentacao = models.TextField(blank=True)
    metodologia = models.TextField(blank=True)
    programa = models.TextField(blank=True)
    bibliografia = models.TextField(blank=True)
    avaliacao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='ucs/', blank=True, null=True)
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE)
    docentes = models.ManyToManyField('docentes.Docente', blank=True)

    class Meta:
        verbose_name_plural = "Unidades Curriculares"

    def __str__(self):
        return self.nome