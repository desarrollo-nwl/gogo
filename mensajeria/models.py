from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from usuarios.models import Empresas
from cuestionarios.models import Proyectos, Preguntas
from colaboradores.models import Colaboradores
from django.utils import timezone

class Streaming( models.Model ):
	id = models.AutoField( primary_key = True)
	colaborador = models.ForeignKey( Colaboradores )
	pregunta = models.ForeignKey( Preguntas )
	proyecto = models.ForeignKey( Proyectos )
	fec_controlenvio = models.DateTimeField( blank = True, null = True  )
	fecharespuesta = models.DateTimeField( blank = True, null = True  )
	respuesta = models.TextField( blank = True, null = True )

	def __unicode__(self):
		return '%s || Q: %s A: %s' %( self.colaborador_id, self.pregunta_id, self.respuesta )

	class Meta:
		managed = True
		db_table = 'mensajeria_streaming'


class Externa( models.Model ):
	id = models.AutoField( primary_key = True)
	colaborador = models.IntegerField( default = 0 )
	proyecto = models.ForeignKey( Proyectos,db_index = True)
	pregunta = models.ForeignKey( Preguntas )
	fecharespuesta = models.DateTimeField( blank = True, null = True  )
	respuesta = models.TextField( blank = True, null = True )

	def __unicode__(self):
		return '%s || Q: %s A: %s' %( self.colaborador, self.pregunta_id, self.respuesta )

	class Meta:
		managed = True
		db_table = 'mensajeria_externa'


class MetricasExterna( models.Model ):
	id = models.AutoField( primary_key = True)
	acumulado = models.IntegerField( default = 0 )
	encuestados = models.IntegerField( default = 0 )
	fecha = models.DateField( default = timezone.now )
	proyecto = models.ForeignKey( Proyectos,db_index = True)

	def __unicode__(self):
		return '%s %s'%(self.proyecto,self.fecha)

	class Meta:
		managed = True
		db_table = 'mensajeria_metricasexterna'


class SRS( models.Model ):
	id = models.AutoField( primary_key = True)
	usuario = models.ForeignKey( Colaboradores )
	fecharespuesta = models.DateTimeField( auto_now_add = True  )
	respuesta = models.TextField( blank = True, null = True )

	def __unicode__(self):
		return '%s %s'%( self.usuario,self.respuesta )

	class Meta:
		managed = True
		db_table = 'mensajeria_srs'
