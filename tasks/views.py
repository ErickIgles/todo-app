
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    UpdateView,
    DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .forms import TaskModelForm

from .models import Task
from .utils.mixins import TaskPermissionMixin


class BaseTemplateView(
    LoginRequiredMixin,
    TemplateView
):
    template_name = 'base.html'


class TarefaCriarView(
    LoginRequiredMixin,
    CreateView
):
    template_name = 'tasks/form_add.html'
    form_class = TaskModelForm
    success_url = reverse_lazy('tasks:listar')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        usuario = self.request.user

        kwargs['usuario'] = usuario

        return kwargs

    def form_valid(self, form):

        messages.success(
            self.request,
            f'Tarefa {form.instance.titulo} adicionado com sucesso.'
        )

        return super().form_valid(form)

    def form_invalid(self, form):

        messages.error(
            self.request,
            'Erro ao adicionar uma nova tarefa. Confira os campos.'
        )

        return super().form_invalid(form)


class TarefaListarView(
    LoginRequiredMixin,
    ListView
):
    template_name = 'tasks/list.html'
    queryset = Task.objects.all()
    context_object_name = 'tasks'

    def get_usuario(self):

        usuario = self.request.user

        return usuario

    def get_queryset(self):

        queryset = super().get_queryset()

        usuario = self.get_usuario()

        queryset = queryset.filter(
            usuario=usuario
        )

        return queryset


class TarefaAtualizarView(
    LoginRequiredMixin,
    TaskPermissionMixin,
    UpdateView
):
    template_name = 'tasks/form_update.html'
    model = Task
    form_class = TaskModelForm
    context_object_name = 'task'
    success_url = reverse_lazy('tasks:listar')

    def form_valid(self, form):

        messages.success(
            self.request,
            'Tarefa atualizada com sucesso.'
        )

        return super().form_valid(form)

    def form_invalid(self, form):

        messages.error(
            self.request,
            'Erro ao tentar atualizar os dados da tarefa. Confira os campos.'
        )

        return super().form_invalid(form)


class TarefaDeletarView(
    LoginRequiredMixin,
    TaskPermissionMixin,
    DeleteView
):
    template_name = 'tasks/form_delete.html'
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks:listar')
