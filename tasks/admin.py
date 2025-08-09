from django.contrib import admin


from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'status')
    list_display_links = ('id', 'titulo')
    search_fields = ('title', )

