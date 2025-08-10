from django.urls import path
from . import views


app_name = 'tasks'
urlpatterns = [
    path('', views.BaseTemplateView.as_view(), name='home'),
    path('tarefa/cadastro/', views.TarefaCriarView.as_view(), name='cadastro'),
    path('tarefa/lista/', views.TarefaListaView.as_view(), name='listar'),
    path('tarefa/atualizar/<int:pk>/', views.TarefaAtualizarView.as_view(), name='atualizar'),
]