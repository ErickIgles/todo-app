
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import TaskModelForm



class BaseTemplateView(TemplateView):
    template_name = 'base.html'



class TarefaCriarView(CreateView):
    template_name = 'tasks/form_add.html'
    form_class = TaskModelForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)

