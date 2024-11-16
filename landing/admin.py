from django.contrib import admin
from .models import Gato

@admin.register(Gato)
class GatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'sexo', 'castrado', 'fiv_felv', 'vacinado')
    list_filter = ('sexo', 'castrado', 'fiv_felv', 'vacinado')
    search_fields = ('nome',)