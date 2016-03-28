from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from cuestionarios_360.models import Proyectos, Instrumentos_360, Preguntas_360
from colaboradores_360.models import Colaboradores_360
from redes_360.models import Redes_360
from django.utils import timezone

class Streaming_360( models.Model ):
	id = models.AutoField( primary_key = True)
	colaborador = models.ForeignKey( Colaboradores_360, related_name="colaborador")
	evaluado = models.ForeignKey( Colaboradores_360, related_name="evaluado", blank=True, null=True )
	rol = models.CharField( max_length = 120 )
	instrumento = models.ForeignKey( Instrumentos_360 )
	pregunta = models.ForeignKey( Preguntas_360 )
	proyecto = models.ForeignKey( Proyectos )
	red = models.ForeignKey( Redes_360 )
	fec_controlenvio = models.DateTimeField( blank = True, null = True  )
	fecharespuesta = models.DateTimeField( blank = True, null = True  )
	respuesta = models.TextField( blank = True, null = True )

	def __unicode__(self):
		return '%s || Q: %s A: %s' %( self.colaborador_id, self.pregunta_id, self.respuesta )

	class Meta:
		managed = True
		db_table = 'mensajeria_360_streaming'
