
from django.contrib.auth.models import User

from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserForm



class UsuarioCriarView(CreateView):
    template_name = 'account/form_register.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('tasks:home')

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)

