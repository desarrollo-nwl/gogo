from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from usuarios.models import Empresas
from cuestionarios.models import Proyectos, Preguntas
from colaboradores.models import Colaboradores


class Streaming( models.Model ):
	id = models.AutoField( primary_key = True)
	colaborador = models.ForeignKey( Colaboradores )
	pregunta = models.ForeignKey( Preguntas )
	proyecto = models.ForeignKey( Proyectos, db_index = True)
	fec_controlenvio = models.DateTimeField( blank = True, null = True  )
	fecharespuesta = models.DateTimeField( blank = True, null = True  )

	def __unicode__(self):
		return '%s || Q: %s A: %s' %( self.colaborador, self.pregunta, self.respuesta )

	class Meta:
		managed = True
		db_table = 'mensajeria_streaming'


class StreamingRespuestas( models.Model ):
	id = models.AutoField( primary_key = True)
	streaming = models.ForeignKey( Streaming )
	respuesta = models.CharField( max_length = 350, blank = True, null = True )

	def __unicode__(self):
		return '%s'%( self.respuesta )

	class Meta:
		managed = True
		db_table = 'mensajeria_streamingrespuestas'


class SRS( models.Model ):
	id = models.AutoField( primary_key = True)
	usuario = models.ForeignKey( User )
	fecharespuesta =  models.DateTimeField( auto_now_add = True )
	respuesta = models.CharField( max_length = 350, blank = True, null = True )

	def __unicode__(self):
		return '%s %s'%( self.usuario,self.respuesta )

	class Meta:
		managed = True
		db_table = 'mensajeria_srs'
