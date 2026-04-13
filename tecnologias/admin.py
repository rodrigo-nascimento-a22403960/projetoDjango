from django.contrib import admin
from .models import Tecnologia

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nivel_preferencia', 'website_oficial')
    search_fields = ('nome',)
    list_filter = ('nivel_preferencia',)