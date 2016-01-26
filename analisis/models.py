from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from usuarios.models import Proyectos
from json_field import JSONField


class Busqueda( models.Model ):
	id = models.OneToOneField( Proyectos, primary_key = True )
	fecha = models.DateTimeField( )
	facebook = JSONField( null = True )
	twitter = JSONField( null = True )
	youtube = JSONField( null = True )
	terminos = models.TextField( )
	masculino = models.PositiveIntegerField( default = 0 )
	femenino = models.PositiveIntegerField( default = 0 )
	publico = models.PositiveIntegerField( default = 0 )
	e_10_18 = models.PositiveIntegerField( default = 0 )
	e_19_24 = models.PositiveIntegerField( default = 0 )
	e_25_34 = models.PositiveIntegerField( default = 0 )
	e_35_44 = models.PositiveIntegerField( default = 0 )
	e_45_54 = models.PositiveIntegerField( default = 0 )
	positivo = models.PositiveIntegerField( default = 0 )
	negativo = models.PositiveIntegerField( default = 0 )
	neutro = models.PositiveIntegerField( default = 0 )
	total = models.PositiveIntegerField( default = 0 )

	def __unicode__(self):
		return "{0}".format(self.proyecto)

	class Meta:
		managed = True
		db_table = 'analisis_busqueda'
		verbose_name_plural = 'Busqueda'


class Twitter( models.Model ):
	id = models.AutoField( primary_key = True )
	diccionario = JSONField( null=True )
	fecha = models.DateField( )
	terminos = models.TextField( )
	twitter = models.ForeignKey( Busqueda )
	masculino = models.PositiveIntegerField( default = 0 )
	femenino = models.PositiveIntegerField( default = 0 )
	publico = models.PositiveIntegerField( default = 0 )
	e_10_18 = models.PositiveIntegerField( default = 0 )
	e_19_24 = models.PositiveIntegerField( default = 0 )
	e_25_34 = models.PositiveIntegerField( default = 0 )
	e_35_44 = models.PositiveIntegerField( default = 0 )
	e_45_54 = models.PositiveIntegerField( default = 0 )
	positivo = models.PositiveIntegerField( default = 0 )
	negativo = models.PositiveIntegerField( default = 0 )
	neutro = models.PositiveIntegerField( default = 0 )
	total = models.PositiveIntegerField( default = 0 )
	id_str = JSONField( null = True )

	def __unicode__(self):
		return "{0}".format(self.numero)

	class Meta:
		managed = True
		db_table = 'analisis_twitter'
		verbose_name_plural = 'Twitter'


class Tweets( models.Model ):
	id = models.AutoField( primary_key = True )
	fecha = models.DateField( index_db = True )
	twitter = models.ForeignKey( Twitter )
	tweet = JSONField( )

	def __unicode__(self):
		return "{0}".format(self.numero)

	class Meta:
		managed = True
		db_table = 'analisis_twitts'
		verbose_name_plural = 'Twitts'


class Facebook( models.Model ):
	id = models.AutoField( primary_key = True )
	diccionario = JSONField( null=True )
	fecha = models.DateField( )
	terminos = models.TextField( )
	facebook = models.CharField( max_length = 100 )
	masculino = models.PositiveIntegerField( default = 0 )
	femenino = models.PositiveIntegerField( default = 0 )
	publico = models.PositiveIntegerField( default = 0 )
	e_10_18 = models.PositiveIntegerField( default = 0 )
	e_19_24 = models.PositiveIntegerField( default = 0 )
	e_25_34 = models.PositiveIntegerField( default = 0 )
	e_35_44 = models.PositiveIntegerField( default = 0 )
	e_45_54 = models.PositiveIntegerField( default = 0 )
	positivo = models.PositiveIntegerField( default = 0 )
	negativo = models.PositiveIntegerField( default = 0 )
	neutro = models.PositiveIntegerField( default = 0 )
	total = models.PositiveIntegerField( default = 0 )

	def __unicode__(self):
		return "{0}".format(self.numero)

	class Meta:
		managed = True
		db_table = 'analisis_facebook'
		verbose_name_plural = 'Facebook'


class Publicacion( models.Model ):
	id = models.AutoField( primary_key = True )
	fecha = DateField( index_db = True )
	facebook = models.ForeignKey( Facebook )
	publicacion = JSONField( )

	def __unicode__(self):
		return "{0}".format(self.numero)

	class Meta:
		managed = True
		db_table = 'analisis_publicacion'
		verbose_name_plural = 'Publicacion'


class Youtube( models.Model ):
	id = models.AutoField( primary_key = True )
	diccionario = JSONField( null=True )
	fecha = models.DateField( index_db = True  )
	terminos = models.TextField( )
	youtube = models.ForeignKey( Busqueda )
	masculino = models.PositiveIntegerField( default = 0 )
	femenino = models.PositiveIntegerField( default = 0 )
	publico = models.PositiveIntegerField( default = 0 )
	e_10_18 = models.PositiveIntegerField( default = 0 )
	e_19_24 = models.PositiveIntegerField( default = 0 )
	e_25_34 = models.PositiveIntegerField( default = 0 )
	e_35_44 = models.PositiveIntegerField( default = 0 )
	e_45_54 = models.PositiveIntegerField( default = 0 )
	positivo = models.PositiveIntegerField( default = 0 )
	negativo = models.PositiveIntegerField( default = 0 )
	neutro = models.PositiveIntegerField( default = 0 )
	total = models.PositiveIntegerField( default = 0 )
	videos = JSONField( null = True )

	def __unicode__(self):
		return "{0}".format(self.numero)

	class Meta:
		managed = True
		db_table = 'analisis_youtube'
		verbose_name_plural = 'Youtube'


class Comentarios( models.Model ):
	id = models.AutoField( primary_key = True )
	fecha = DateField( )
	youtube = models.ForeignKey( Youtube )
	videoid = models.CharField( max_length = 100 )
	vistas = models.CharField( max_length = 50 )
	mgusta = models.CharField( max_length = 20 )
	nmgusta = models.CharField( max_length = 20 )
	comentarios = JSONField( )

	def __unicode__(self):
		return "{0}".format(self.numero)

	class Meta:
		managed = True
		db_table = 'analisis_publicacion'
		verbose_name_plural = 'Publicacion'



class Resumen( models.Model ):
	id = models.AutoField( primary_key = True )
	busqueda = models.ForeignKey( Busqueda )
	fecha = models.DateField( )
	masculino = models.PositiveIntegerField( default = 0 )
	femenino = models.PositiveIntegerField( default = 0 )
	publico = models.PositiveIntegerField( default = 0 )
	e_10_18 = models.PositiveIntegerField( default = 0 )
	e_19_24 = models.PositiveIntegerField( default = 0 )
	e_25_34 = models.PositiveIntegerField( default = 0 )
	e_35_44 = models.PositiveIntegerField( default = 0 )
	e_45_54 = models.PositiveIntegerField( default = 0 )
	positivo = models.PositiveIntegerField( default = 0 )
	negativo = models.PositiveIntegerField( default = 0 )
	neutro = models.PositiveIntegerField( default = 0 )
	total = models.PositiveIntegerField( default = 0 )

	def __unicode__(self):
		return "{0}".format(self.numero)

	class Meta:
		managed = True
		db_table = 'analisis_resumen'
		verbose_name_plural = 'Resumen'
