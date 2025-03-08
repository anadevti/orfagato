from django.contrib import admin
from .models import Interessado, Gato

@admin.register(Interessado)
class InteressadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'trabalha', 'tem_outros_pets', 'mora', 'concordam_adocao')
    search_fields = ('nome', 'idade')

@admin.register(Gato)
class GatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'sexo', 'castrado', 'vacinado', 'fiv_felv')  # Listagem
    search_fields = ('nome', 'sexo')  # Campos para busca
    list_filter = ('sexo', 'castrado', 'vacinado', 'fiv_felv')  # Filtros laterais
    ordering = ('nome',)  # Ordenação padrão
    fieldsets = (  # Organização dos campos no formulário de edição
        ("Informações Básicas", {
            'fields': ('nome', 'idade', 'sexo', 'descricao')
        }),
        ("Detalhes de Saúde", {
            'fields': ('castrado', 'vacinado', 'fiv_felv')
        }),
        ("Imagem", {
            'fields': ('imagem',)
        }),
    )
