from django.db import models

class Projeto(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    imagem = models.ImageField(upload_to='projetos/', null=True, blank=True)
    video_demo_url = models.URLField(blank=True, null=True)
    github_url = models.URLField()
    unidade_curricular = models.ForeignKey(
        'licenciatura.UnidadeCurricular', on_delete=models.CASCADE
    )
    tecnologias = models.ManyToManyField('tecnologias.Tecnologia')
    competencias = models.ManyToManyField('competencias.Competencia')

    class Meta:
        verbose_name_plural = "Projetos"

    def __str__(self):
        return self.titulo