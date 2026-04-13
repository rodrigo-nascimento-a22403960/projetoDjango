from django.contrib import admin
from .models import Projeto

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'unidade_curricular', 'github_url')
    search_fields = ('titulo',)
    list_filter = ('unidade_curricular',)
    filter_horizontal = ('tecnologias', 'competencias')