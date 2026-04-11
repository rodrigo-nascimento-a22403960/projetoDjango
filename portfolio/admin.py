from django.contrib import admin
from .models import Licenciatura, Docente, UnidadeCurricular, TFC, Tecnologia, Competencia, Projeto

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    # Visualização da tabela
    list_display = ('nome', 'sigla', 'duracao_anos', 'ects_total')
    # Campos de pesquisa
    search_fields = ('nome', 'sigla')
    # Filtros laterais
    list_filter = ('duracao_anos',)

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pagina_pessoal_url')
    search_fields = ('nome',)


@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano_curricular', 'semestre', 'ects', 'licenciatura')
    search_fields = ('nome',)
    list_filter = ('ano_curricular', 'semestre', 'licenciatura')

@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'ano', 'destaque', 'licenciatura')
    search_fields = ('titulo', 'autor')
    list_filter = ('ano', 'destaque')


@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nivel_preferencia')

@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'nivel')
    list_filter = ('tipo',)

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'unidade_curricular')
    search_fields = ('titulo', 'descricao')
    list_filter = ('unidade_curricular',)