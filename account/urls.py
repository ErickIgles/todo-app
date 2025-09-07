from django.urls import path

from . import views

app_name = 'account'
urlpatterns = [
    path(
        'registrar/',
        views.UsuarioCriarView.as_view(),
        name='registrar'
    ),
    path(
        'login/',
        views.UsuarioLoginView.as_view(),
        name='login'
    ),
    path(
        'logout/',
        views.UsuarioLogoutView.as_view(),
        name='logout'
    )
]
