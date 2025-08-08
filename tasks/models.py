from django.db import models


class Base(models.Model):

    criado = models.DateField(verbose_name='Criado', auto_now_add=True)
    atualizado = models.DateTimeField(verbose_name='Atualizado', auto_now=True)
    ativo = models.BooleanField(verbose_name='Ativo', default=True)

    class Meta:
        abstract = True


class Task(Base):

    class Status(models.TextChoices):
        PENDENTE = 'pendente', 'Pendente'
        EM_ANDAMENTO = 'em_andamento', 'Em andamento'
        CONCLUIDA = 'concluida', 'Concluída'

    titulo = models.CharField(
        verbose_name='Título', 
        max_length=100
        )
    descricao = models.TextField(
        verbose_name='Descrição', 
        blank=True, 
        null=True
        )
    status = models.BooleanField(
        verbose_name='Status',
        choices=Status.choices,
        default=Status.PENDENTE,
        max_length=20
        )
    
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
    
    def __str__(self):
        return f'{self.titulo}'

