from django.contrib import admin
from .models import Licenciatura, UnidadeCurricular

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'duracao_anos', 'ects_total')
    search_fields = ('nome', 'sigla')

@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano_curricular', 'semestre', 'ects', 'licenciatura')
    search_fields = ('nome',)
    list_filter = ('ano_curricular', 'semestre', 'licenciatura')