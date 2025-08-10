from django.urls import path
from . import views


app_name = 'tasks'
urlpatterns = [
    path('', views.BaseTemplateView.as_view(), name='home'),
    path('tarefa/cadastrar/', views.TarefaCriarView.as_view(), name='cadastrar'),
    path('tarefa/listar/', views.TarefaListarView.as_view(), name='listar'),
    path('tarefa/atualizar/<int:pk>/', views.TarefaAtualizarView.as_view(), name='atualizar'),
    path('tarefa/deletar/<int:pk>/', views.TarefaDeletarView.as_view(), name='deletar'),
]