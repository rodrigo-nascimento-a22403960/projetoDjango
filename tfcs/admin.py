from django.contrib import admin
from .models import TFC

@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autores', 'orientadores', 'licenciaturas', 'rating', 'destaque')
    search_fields = ('titulo', 'autores', 'orientadores')
    list_filter = ('rating', 'destaque', 'licenciaturas')