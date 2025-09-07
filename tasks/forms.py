from django.forms import ModelForm
from django import forms

from .models import Task


class TaskModelForm(ModelForm):

    class Meta:
        model = Task
        fields = ['titulo', 'descricao', 'status']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('usuario', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):

        tarefa = super().save(commit=False)

        if self.usuario is not None:

            tarefa.usuario = self.usuario

        if commit:

            tarefa.save()

        return tarefa
