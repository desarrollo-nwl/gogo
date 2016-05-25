from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from cuestionarios_360.models import Proyectos


class Participacion_360( models.Model ):
	id = models.OneToOneField( Proyectos, primary_key = True)
	arbol = models.TextField( )
	diccionario = models.TextField( )
	fecha = model.DateTimeField( now_add = True )

	def __unicode__(self):
		return self.diccionario

	class Meta:
		managed = True
		db_table = 'analisis_360_participacion'
		verbose_name_plural = 'Participacion 360'
