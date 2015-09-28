from django.contrib import admin
from cuestionarios.models import Variables,Preguntas,Respuestas

admin.site.register(Preguntas)
admin.site.register(Respuestas)
admin.site.register(Variables)
