from django.contrib import admin
from .models import Licenciatura, Docente

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