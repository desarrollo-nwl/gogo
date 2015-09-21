from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from cuestionarios.models import Proyectos


class Colaboradores( models.Model ):
	id = models.AutoField( primary_key = True )
	apellido = models.CharField( max_length = 45 )
	email = models.EmailField( )
	nombre = models.CharField( max_length = 45 )
	proyecto = models.ForeignKey( Proyectos )
	key = models.CharField( max_length = 64 )
	def __unicode__(self):
		return '%s %s ' % (self.nombre,self.apellido)

	class Meta:
		managed = True
		db_table = 'colaboradores_colaboradores'
		verbose_name_plural = 'Colaboradores'


class ColaboradoresDatos( models.Model ):
	id = models.OneToOneField( Colaboradores, primary_key = True )
	area = models.CharField( max_length = 50, blank = True, null = True )
	cargo = models.CharField( max_length = 200, blank = True, null = True  )
	ciudad = models.CharField( max_length = 100, blank = True, null = True)
	fec_ingreso = models.DateField( blank = True, null = True )
	fec_nacimiento = models.DateField( blank = True, null = True )
	genero = models.CharField( max_length = 10, blank = True, null = True)
	niv_academico = models.CharField( max_length = 50, blank = True, null = True )
	opcional1 = models.CharField( max_length=100, blank=True, null=True )
	opcional2 = models.CharField( max_length=100, blank=True, null=True )
	opcional3 = models.CharField( max_length=100, blank=True, null=True )
	opcional4 = models.CharField( max_length=100, blank=True, null=True )
	opcional5 = models.CharField( max_length=100, blank=True, null=True )
	pais = models.CharField( max_length = 100, blank = True, null = True)
	ciudad = models.CharField( max_length = 100, blank = True, null = True)	
	profesion = models.CharField( max_length = 200, blank = True, null = True  )
	regional = models.CharField( max_length = 50, blank = True, null = True )

	def __unicode__(self):
		return '%s %s ' % (self.nombre,self.apellido)

	class Meta:
		managed = True
		db_table = 'colaboradores_datos'
		verbose_name_plural = 'Colaboradores datos'


class ColaboradoresMetricas( models.Model ):
	id = models.AutoField( primary_key = True )
	colaborador = models.ForeignKey( Colaboradores )
	fec_envio = models.DateTimeField( auto_now_add = True )
	fec_respuesta = models.DateTimeField( blank = True, null = True )

	def __unicode__(self):
		return '%s' % (self.colaborador)

	class Meta:
		managed = True
		db_table = 'colaboradores_metricas'
		verbose_name_plural = 'Metricas envio-repuesta'
