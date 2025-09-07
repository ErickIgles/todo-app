from django.contrib import admin


from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'usuario',
        'titulo',
        'descricao',
        'status',
        'criado',
        'atualizado',
        'ativo'
    ]

    list_display_links = [
        'id',
        'titulo'
    ]

    search_fields = ('titulo', )

    ordering = (
        'id',
    )
