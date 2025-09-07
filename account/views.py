
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth.views import LoginView, LogoutView


from .forms import UserForm, UserLoginForm


class UsuarioCriarView(CreateView):
    template_name = 'account/form_register.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('tasks:home')

    def form_valid(self, form):
        messages.success(
            self.request,
            'Usuário cadastrado com sucesso.'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            'Erro ao realizar o cadastro. Verifique às informações.'
        )
        return super().form_invalid(form)


class UsuarioLoginView(LoginView):
    template_name = 'account/form_login.html'
    redirect_authenticated_user = True
    form_class = UserLoginForm


class UsuarioLogoutView(LogoutView):
    next_page = 'account:login'
