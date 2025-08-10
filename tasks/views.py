
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
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


class TarefaAtualizarView(UpdateView):
    template_name = 'tasks/form_update.html'
    model = Task
    form_class = TaskModelForm
    context_object_name = 'task'
    success_url = reverse_lazy('tasks:listar')

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)


class TarefaDeletarView(DeleteView):
    template_name = 'tasks/form_delete.html'
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks:listar')

