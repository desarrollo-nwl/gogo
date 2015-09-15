from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from usuarios.models import Empresas
from cuestionarios.models import Proyectos, Preguntas
from Colaboradores.models import Colaboradores


class Streaming( models.Model ):
    colaborador = models.ForeignKey( Colaboradores )
    pregunta = models.ForeignKey( Preguntas )
    proyecto = models.ForeignKey( Proyectos, db_index = True)
    fec_enviopregunta = models.DateTimeField( blank = True, null = True  )
    fecharespuesta = models.DateTimeField( db_index = True, blank = True, null = True  )
    respuesta = models.CharField( max_length = 350, blank = True, null = True )

    def __unicode__(self):
		return '%s || Q: %s A: %s' %( self.colaborador, self.pregunta, self.respuesta )

    class Meta:
        managed = True
        db_table = 'mensajeria_streaming'


class Envio( models.Model ):
	id_envio = models.AutoField( primary_key=True )
	usuario = models.ForeignKey( User )
    link = models.charfield( max_length = 96 )
	fregistro = models.DateTimeField( auto_now_add = True )

	def __unicode__(self):
		return self.email

	class Meta:
		managed = True
		db_table = 'mensajeria_envio'
		verbose_name_plural = 'Envios'
