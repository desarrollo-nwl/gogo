from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from cuestionarios_360.models import Proyectos,Instrumentos_360
from colaboradores_360.models import Colaboradores_360,Roles_360

class Redes_360( models.Model ):
	id = models.AutoField( primary_key = True )
	colaborador = models.ForeignKey( Colaboradores_360, related_name="colaborador_red")
	estado = models.BooleanField( default = True )
	evaluado = models.ForeignKey( Colaboradores_360, related_name="evaluado_red")
	instrumento = models.ForeignKey( Instrumentos_360 )
	proyecto = models.ForeignKey( Proyectos )
	rol = models.CharField( max_length = 128 )
	rol_idn = models.PositiveIntegerField( db_index = True )

	def __unicode__(self):
		return '%s' % (self.id)

	class Meta:
		managed = True
		db_table = 'redes_360_redes'
		verbose_name_plural = 'Redes 360'
