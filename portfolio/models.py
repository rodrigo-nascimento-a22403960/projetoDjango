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
    imagem = models.ImageField(upload_to='ucs/', null=True, blank=True)
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
    link_pdf = models.URLField(blank=True, null=True)  # NOVO: para guardar o link do JSON
    imagem_url = models.URLField(blank=True, null=True) # NOVO: para guardar a imagem do JSON

    class Meta:
        verbose_name_plural = "TFCs"

    def __str__(self):
        return self.titulo

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

class Projeto(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    imagem = models.ImageField(upload_to='projetos/', null=True, blank=True)
    github_url = models.URLField()
    unidade_curricular = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE)
    tecnologias = models.ManyToManyField(Tecnologia)
    competencias = models.ManyToManyField(Competencia)

    class Meta:
        verbose_name_plural = "Projetos"

    def __str__(self):
        return self.titulo

class Formacao(models.Model):
    instituicao = models.CharField(max_length=150)
    curso = models.CharField(max_length=150)
    ano_inicio = models.PositiveIntegerField()
    ano_fim = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Formações"

    def __str__(self):
        return f"{self.curso} - {self.instituicao}"

class Interesse(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='interesses/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Interesses"

    def __str__(self):
        return self.nome