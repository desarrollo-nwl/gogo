from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from cuestionarios_360.models import Proyectos,Instrumentos_360


class Colaboradores_360( models.Model ):
	id = models.AutoField( primary_key = True )
	apellido = models.CharField( max_length = 45 )
	descripcion = models.CharField( max_length = 255, blank=True, null=True )
	email = models.EmailField( )
	enviados = models.PositiveSmallIntegerField( default = 0 )
	estado = models.BooleanField( default = True)
	externo = models.BooleanField( default = False )
	genero = models.CharField( max_length = 10, blank = True, null = True)
	key = models.CharField( max_length = 64 )
	key_old = models.CharField( max_length = 64, default = "HACK" )
	nombre = models.CharField( max_length = 45 )
	pre_aresponder = models.PositiveSmallIntegerField( default = 0)
	pre_respuestas = models.PositiveSmallIntegerField( default = 0)
	tot_avance = models.PositiveSmallIntegerField( default = 0)
	can_instrumentos = models.PositiveSmallIntegerField( default = 0)
	propension = models.FloatField( default = -1 )
	proyecto = models.ForeignKey( Proyectos )
	puntaje = models.FloatField( default = 0 )
	reenviados = models.PositiveSmallIntegerField( default = 0)
	respuestas = models.PositiveSmallIntegerField( default = 0 )

	def __unicode__(self):
		return '%s %s ' % (self.nombre,self.apellido)

	class Meta:
		managed = True
		db_table = 'colaboradores_360_colaboradores'
		verbose_name_plural = 'Colaboradores 360'


class ColaboradoresDatos_360( models.Model ):
	id = models.OneToOneField( Colaboradores_360, primary_key = True )
	area = models.CharField( max_length = 200, blank = True, null = True )
	cargo = models.CharField( max_length = 200, blank = True, null = True  )
	ciudad = models.CharField( max_length = 100, blank = True, null = True)
	fec_ingreso = models.DateField( blank = True, null = True )
	fec_nacimiento = models.DateField( blank = True, null = True )
	niv_academico = models.CharField( max_length = 50, blank = True, null = True )
	opcional1 = models.CharField( max_length=100, blank=True, null=True )
	opcional2 = models.CharField( max_length=100, blank=True, null=True )
	opcional3 = models.CharField( max_length=100, blank=True, null=True )
	opcional4 = models.CharField( max_length=100, blank=True, null=True )
	opcional5 = models.CharField( max_length=100, blank=True, null=True )
	ciudad = models.CharField( max_length = 100, blank = True, null = True)
	profesion = models.CharField( max_length = 200, blank = True, null = True  )
	regional = models.CharField( max_length = 200, blank = True, null = True )

	def __unicode__(self):
		return '%s %s' % (self.id.nombre,self.id.apellido)

	class Meta:
		managed = True
		db_table = 'colaboradores_360_datos'
		verbose_name_plural = 'Colaboradores datos 360'


class ColaboradoresMetricas_360( models.Model ):
	id = models.OneToOneField( Colaboradores_360, primary_key=True )
	propension = models.TextField( default=u'[]' )
	ord_instrumentos = models.TextField( default=u'[]' )
	ins_actual = models.PositiveIntegerField( default = 0 )

	def __unicode__(self):
		return '%s' % (self.id)

	class Meta:
		managed = True
		db_table = 'colaboradores_360_metricas'
		verbose_name_plural = 'Metricas propension 360'


class Roles_360( models.Model ):
	id =  models.AutoField( primary_key = True )
	nombre = models.CharField( max_length = 128 )
	proyecto = models.ForeignKey( Proyectos )

	def __unicode__(self):
		return '%s' % (self.id)

	class Meta:
		managed = True
		db_table = 'colaboradores_360_roles'
		verbose_name_plural = 'Roles 360'
