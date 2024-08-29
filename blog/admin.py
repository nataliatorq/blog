# blog/admin.py
from django.contrib import admin
from .models import GostosPessoais, Curiosidades, SobreMim

@admin.register(GostosPessoais)
class GostosPessoaisAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'imagem')  # Atualize o display

@admin.register(Curiosidades)
class CuriosidadesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'imagem')  # Atualize o display

@admin.register(SobreMim)
class SobreMimAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'imagem')  # Adicione 'foto' aqui
    