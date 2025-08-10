from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('', views.UsuarioCriarView.as_view(), name='registrar'),
]

