from django.shortcuts import redirect
from django.contrib import messages
from django.http import Http404


class TaskPermissionMixin:

    def dispatch(self, request, *args, **kwargs):
        """
            Mixin para realização de comparação de usuário logado com
            usuário relacionado ao objeto requisitado.
        """

        usuario_logado = self.request.user

        if not usuario_logado.is_authenticated:

            messages.error(
                request,
                'Você precisa estar logado para acessar esta página.'
            )

            return redirect('account:login')

        try:

            obj = self.get_object()

        except Http404:

            messages.error(
                request,
                'Objeto não encontrado.'
            )

            return redirect('tasks:home')

        if obj.usuario != usuario_logado:

            messages.error(
                request,
                'Usuário não tem permissão para acessar este registro.'
            )

            return redirect('tasks:home')

        return super().dispatch(request, *args, **kwargs)
