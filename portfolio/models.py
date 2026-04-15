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
    docentes = models.ManyToManyField(Docente, blank=True)

    class Meta:
        verbose_name_plural = "Unidades Curriculares"

    def __str__(self):
        return self.nome


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


class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    nivel = models.PositiveIntegerField()
    descricao = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Competências"

    def __str__(self):
        return self.nome


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


class Projeto(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    imagem = models.ImageField(upload_to='projetos/', null=True, blank=True)
    video_demo_url = models.URLField(blank=True, null=True)
    github_url = models.URLField()
    unidade_curricular = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE)
    tecnologias = models.ManyToManyField(Tecnologia)
    competencias = models.ManyToManyField(Competencia)

    class Meta:
        verbose_name_plural = "Projetos"

    def __str__(self):
        return self.titulo


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