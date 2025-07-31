from django.contrib import admin

from .models import Tarefa


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):

    list_display = ['id', 'titulo', 'descricao', 'usuario', 'criado', 'modificado', 'ativo']
    list_display_links = ['id', 'titulo', 'descricao', 'usuario']

