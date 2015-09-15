from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from usuarios.models import Empresas


class Proyectos( models.Model ):
	id = models.AutoField( primary_key=True )
	activo = models.BooleanField( default = False )
    descripcion = models.TextField( blank = True, null = True, max_length = 255 )
    nombre =  models.CharField( max_length = 255 )
    usuario = models.ForeignKey( User )
    empresa = models.ForeignKey( Empresas )
    fec_registro =  models.DateTimeField( auto_now_add = True )
    publico = models.BooleanField( default = False )
	prudenciamax = models.IntegerField( default = 2 )
	prudenciamin = models.IntegerField( default = 1 )
    can_envio = models.IntegerField( default = 5 )
	def __unicode__(self):
		return self.nombre

	class Meta:
		managed = True
		db_table = 'cuestionarios_proyectos'
		verbose_name_plural = 'Proyectos'


class ProyectosDatos( models.Model ):
	id = models.OneToOneField( Proyectos, primary_key = True )
	cue_correo = models.TextField( blank = True, null = True )
	empresa = models.ForeignKey( Empresas )
	fregistro = models.DateField( auto_now_add = True )
	int_encuesta = models.TextField( blank = True, null = True )
	logo = models.ImageField( upload_to = 'logos' )
	logoenc = models.ImageField( upload_to = 'logos', blank = True, null = True )
	permiso = models.BooleanField( default = False )
	senso = models.BooleanField( default = True )
	tipo = models.IntegerField( blank = True, null = True )
	tit_encuesta = models.CharField( max_length = 255, blank = True, null = True )
    usuarios = models.ManyToManyField( User )

	def __unicode__(self):
		return self.nombre

	class Meta:
		managed = True
		db_table = 'cuestionarios_proyectosdatos'
		verbose_name_plural = "Proyectos datos"


class Variables( models.Model ):
	id = models.AutoField( primary_key = True )
	descripcion = models.TextField( blank = True, null = True , max_length = 255 )
	estado = models.BooleanField( default = True )
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
    pregunta = models.CharField( max_length = 255 )
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
    respuesta = models.CharField( max_length = 255 )

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
