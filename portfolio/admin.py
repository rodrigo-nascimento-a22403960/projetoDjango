from django.contrib import admin
from .models import Licenciatura, Docente, UnidadeCurricular, Tecnologia, Competencia, Formacao, Projeto, TFC, MakingOf

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'duracao_anos', 'ects_total')
    search_fields = ('nome', 'sigla')

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pagina_pessoal_url')
    search_fields = ('nome',)

@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano_curricular', 'semestre', 'ects', 'licenciatura')
    search_fields = ('nome',)
    list_filter = ('ano_curricular', 'semestre', 'licenciatura')

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nivel_preferencia', 'website_oficial')
    search_fields = ('nome',)

@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'nivel')
    search_fields = ('nome', 'tipo')
    list_filter = ('tipo',)

@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instituicao', 'data_inicio', 'data_fim')
    search_fields = ('nome', 'instituicao')

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'unidade_curricular', 'github_url')
    search_fields = ('titulo',)
    filter_horizontal = ('tecnologias', 'competencias')

@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autores', 'orientadores', 'licenciaturas', 'rating', 'destaque')
    search_fields = ('titulo', 'autores', 'orientadores')
    list_filter = ('rating', 'destaque')

@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data')
    search_fields = ('titulo',)