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
	key = models.Charfield( max_length = 64 )
	def __unicode__(self):
		return '%s %s ' % (self.nombre,self.apellido)

	class Meta:
		managed = True
		db_table = 'colaboradores_colaboradores'
		verbose_name_plural = 'Colaboradores'


class ColaboradoresDatos( models.Model ):
	id = models.OneToOneField( Colaboradores, primary_key = True )
	area = models.CharField( max_length = 50, blank = True, null = True )
	car_ocupados = models.CharField( max_length = 1000, blank = True, null = True)
	cargo = models.CharField( max_length = 200, blank = True, null = True  )
	dni = models.IntegerField( blank = True, null = True )
	est_civil = models.CharField( max_length = 15, blank = True, null = True )
	fec_ingreso = models.DateField( blank = True, null = True )#### antiguedad o fecha de ingreso????
	fec_nacimiento = models.DateField( blank = True, null = True )
	fec_retiro = models.IntegerField( blank = True, null = True )
	genero = models.CharField( max_length = 10, blank = True, null = True)
	gente_a_cargo = models.BooleanField( default = True )
	niv_academico = models.CharField( max_length = 50, blank = True, null = True )
	profesion = models.CharField( max_length = 200, blank = True, null = True  )
	regional = models.CharField( max_length = 50, blank = True, null = True )
	sueldo = models.FloatField( blank = True, null = True )
	vice = models.CharField( max_length = 50, blank = True, null = True )

	def __unicode__(self):
		return '%s %s ' % (self.nombre,self.apellido)

	class Meta:
		managed = True
		db_table = 'colaboradores_datos'
		verbose_name_plural = 'Colaboradores datos'


class ColaboradoresSalud( models.Model ):
	id = models.OneToOneField( Colaboradores, primary_key = True )
	peso = models.FloatField( default = -1 )

	def __unicode__(self):
		return '%s %s ' % (self.nombre,self.apellido)

	class Meta:
		managed = True
		db_table = 'colaboradores_salud'
		verbose_name_plural = 'Colaboradores salud'


class MColaboradores( models.Model ):
	id = models.AutoField( primary_key = True )
	colaborador = models.ForeignKey( Colaboradores )
	fec_envio = models.DateTimeField( auto_now_add = True )
	fec_respuesta = models.DateTimeField( blank = True, null = True )

	def __unicode__(self):
		return '%s' % (self.colaborador)

	class Meta:
		managed = True
		db_table = 'colaboradores_metricas'
		verbose_name_plural = 'Metricas colaboradores'
