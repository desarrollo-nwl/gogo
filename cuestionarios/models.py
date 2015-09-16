from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from usuarios.models import Proyectos


class Variables( models.Model ):
	id = models.AutoField( primary_key = True )
	descripcion = models.TextField( blank = True, null = True , max_length = 255 )
	estado = models.BooleanField( default = True )
	max_preguntas = models.SmallIntegerField( default = 0 )
	nombre =  models.CharField( max_length = 255 )
	posicion = models.IntegerField( blank = True, null = True )
	proyecto = models.ForeignKey( Proyectos, blank = True, null = True )

	def __unicode__(self):
		return self.nombre

	class Meta:
		managed = True
		db_table = 'cuestionarios_variables'
		verbose_name_plural = 'Variables'


class Preguntas( models.Model ):
	id = models.AutoField( primary_key = True )
	abierta = models.BooleanField( default = False )
	estado = models.BooleanField( default = True )
	multiple = models.BooleanField( default = False )
	numerica = models.BooleanField( default = True )
	posicion = models.IntegerField()
	texto = models.CharField( max_length = 255 )
	variable = models.ForeignKey( Variables )

	def __unicode__(self):
		return self.pregunta

	class Meta:
		managed = True
		db_table = 'cuestionarios_preguntas'
		verbose_name_plural = 'Preguntas'


class Respuestas( models.Model ):
	id = models.AutoField( primary_key = True )
	numerico = models.FloatField( blank = True, null = True )
	pregunta = models.ForeignKey( Preguntas )
	texto = models.CharField( max_length = 255 )

	def __unicode__(self):
		return self.respuesta

	class Meta:
		managed = True
		db_table = 'cuestionarios_respuestas'
		verbose_name_plural = 'Respuestas'


class Bibliotecas( models.Model ):
	id = models.AutoField( primary_key = True )
	descripcion = models.TextField( blank = True, null = True , max_length = 255 )
	nombre = models.CharField( unique = True, max_length = 255 )
	variables = models.ManyToManyField( Variables )

	def __unicode__(self):
		return self.nombre

	class Meta:
		managed = True
		db_table = 'cuestionario_bibliotecas'
		verbose_name_plural = "Bibliotecas"
