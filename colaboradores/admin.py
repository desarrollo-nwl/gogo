from django.contrib import admin
from colaboradores.models import *
from actions import enviar_correo_masivo
from daterange_filter.filter import DateRangeFilter


class ColaboradoresAdmin(admin.ModelAdmin):
    list_filter = ['proyecto', 'estado', 'respuestas', ('colaborador__fecharespuesta', DateRangeFilter), ]
    search_fields = ['nombre', 'apellido', 'email']
    actions = [enviar_correo_masivo]

admin.site.register(Colaboradores, ColaboradoresAdmin)
admin.site.register(ColaboradoresDatos)
admin.site.register(ColaboradoresMetricas)
