from django.urls import path
from . import views


app_name = 'tasks'
urlpatterns = [
    path('', views.BaseTemplateView.as_view(), name='home'),
    path('tarefa/cadastro/', views.TarefaCriarView.as_view(), name='cadastro'),
]