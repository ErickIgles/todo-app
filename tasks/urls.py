from django.urls import path
from . import views

urlpatterns = [
    path('', views.BaseTemplateView.as_view(), name='home'),
]