
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView
from .forms import TaskModelForm

from .models import Task

class BaseTemplateView(TemplateView):
    template_name = 'base.html'



class TarefaCriarView(CreateView):
    template_name = 'tasks/form_add.html'
    form_class = TaskModelForm
    success_url = reverse_lazy('tasks:home')

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)


class TarefaListaView(ListView):
    template_name = 'tasks/list.html'
    queryset = Task.objects.all()
    context_object_name = 'tasks'

