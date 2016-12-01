from django.contrib import admin
from usuarios.models import *


class AdminDesafio(admin.ModelAdmin):
    list_display = ('nombre', )


class AdminDesafioSeleccionado(admin.ModelAdmin):
    list_display = ('nombre', 'email', )
    list_filter = ('desafio', 'email')
    search_fields = ('nombre', 'email', 'desafio')

admin.site.register(Errores)
admin.site.register(IndiceUsuarios)
admin.site.register(Logs)
admin.site.register(Permisos)
admin.site.register(Proyectos)
admin.site.register(ProyectosDatos)
admin.site.register(Empresas)
admin.site.register(Recuperar)
admin.site.register(Desafio, AdminDesafio)
admin.site.register(DesafioSeleccionado, AdminDesafioSeleccionado)
