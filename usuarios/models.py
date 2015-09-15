from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class Empresas( models.Model ):
    id = models.AutoField( primary_key = True )
    activa = models.BooleanField( default = True )
    departamento =  models.CharField(  max_length = 100 , blank = True, null = True )
    nit = models.CharField(  max_length = 20 , blank = True, null = True )
    nombre = models.CharField( max_length = 100 )
    num_empleados =  models.IntegerField( blank= True, null = True )
    pagina = models.CharField( max_length=1000, blank= True, null = True )
    pais =  models.CharField(  max_length = 100 , blank = True, null = True )
    sector = models.CharField(  max_length = 100, blank = True, null = True )
    usuarios = models.ManyToManyField( User )

    def __unicode__(self):
		return self.nombre

    class Meta:
        managed = True
        db_table = 'usuarios_empresas'
        verbose_name_plural = 'Empresas'


class permisos( models.Model ):
    id = models.OneToOneField( User, primary_key = True )
    consultor = models.BooleanField( default = True )
    act_permisos = models.BooleanField( default = True )
    act_surveys = models.BooleanField( default = False)
    act_variables = models.BooleanField( default = True )
    col_add = models.BooleanField( default = True )#colaboradores
    col_del = models.BooleanField( default = True )
    col_edit = models.BooleanField( default = True )
    col_see = models.BooleanField( default = True )
    det_see = models.BooleanField( default = True )#respuestas detalladas
    pre_add = models.BooleanField( default = True )#preguntas
    pre_del = models.BooleanField( default = True )
    pre_edit = models.BooleanField( default = True )
    pre_see = models.BooleanField( default = True )
    pro_add = models.BooleanField( default = True )#proyectos
    pro_del = models.BooleanField( default = True )
    pro_edit = models.BooleanField( default = True )
    pro_see = models.BooleanField( default = True )
    res_exp = models.BooleanField( default = True )#exportar resultados
    res_see = models.BooleanField( default = True )#graficas

    def __unicode__(self):
		return self.nombre

    class Meta:
        managed = True
        db_table = 'usuarios_permisos'
        verbose_name_plural = 'Permisos'
