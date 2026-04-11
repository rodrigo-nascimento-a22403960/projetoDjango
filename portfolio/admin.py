from django.contrib import admin
from .models import Licenciatura, Docente, UnidadeCurricular, TFC

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