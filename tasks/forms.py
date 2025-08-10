from django.forms import ModelForm
from django import forms

from .models import Task



class TaskModelForm(ModelForm):

    class Meta:
        model = Task
        fields = ['titulo', 'descricao', 'status']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': ''}),
            'descricao': forms.Textarea(attrs={'class': ''}),
            'status': forms.Select(attrs={'class': ''})
        }
