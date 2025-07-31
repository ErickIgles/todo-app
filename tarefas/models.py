from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):
    criado = models.DateField(verbose_name='Criardo', auto_now_add=True)
    modificado = models.DateTimeField(verbose_name='Atualizado', auto_now=True)
    ativo = models.BooleanField(verbose_name='Ativo', default=True)

    class Meta:
        abstract = True



class Tarefa(Base):
    STATUS_CHOICES = [
        ('P', 'Pendente'),
        ('A', 'Em andamento'),
        ('C', 'Concluído')
    ]

    titulo = models.CharField(verbose_name='Título', max_length=70)
    descricao = models.TextField(verbose_name='Descrição')
    status = models.CharField(verbose_name='Status', max_length=1, choices=STATUS_CHOICES, default='P')
    usuario = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.titulo}'
    
