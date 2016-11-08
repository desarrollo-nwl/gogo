from django.contrib import admin
from colaboradores_360.models import *
from actions import enviar_correo_masivo
from daterange_filter.filter import DateRangeFilter


class Colaboradores360Admin(admin.ModelAdmin):
    list_filter = ['proyecto', 'estado', 'respuestas', ('colaborador__fecharespuesta', DateRangeFilter), ]
    search_fields = ['nombre', 'apellido', 'email']
    actions = [enviar_correo_masivo]

admin.site.register(Colaboradores_360, Colaboradores360Admin)
admin.site.register(ColaboradoresDatos_360)
admin.site.register(ColaboradoresMetricas_360)
