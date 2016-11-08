from django.core.exceptions import PermissionDenied
from django.contrib import messages
from mensajeria.views import colaboradoreenviar


def enviar_correo_masivo(modeladmin, request, queryset):
    if not request.user.is_staff:
        raise PermissionDenied
    for colaborador in queryset:
        colaboradoreenviar(request, colaborador.id)
        messages.add_message(
            request, messages.INFO,
            'Enviado correo a: {0}'.format(colaborador))
