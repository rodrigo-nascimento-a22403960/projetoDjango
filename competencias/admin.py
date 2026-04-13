from django.contrib import admin
from .models import Competencia

@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'nivel')
    search_fields = ('nome', 'tipo')
    list_filter = ('tipo',)