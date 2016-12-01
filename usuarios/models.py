from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


class Empresas( models.Model ):
    id = models.AutoField( primary_key = True )
    departamento =  models.CharField(  max_length = 100 , blank = True, null = True )
    nit = models.CharField(  max_length = 20 , blank = True, null = True )
    nombre = models.CharField( max_length = 100 )
    num_empleados =  models.IntegerField( blank= True, null = True )
    pagina = models.CharField( max_length=1000, blank= True, null = True )
    pais =  models.CharField(  max_length = 100 , blank = True, null = True )
    sector = models.CharField(  max_length = 100, blank = True, null = True )
    usuario = models.ForeignKey( User )
    zdel = models.DateTimeField( blank = True, null = True )

    def __unicode__(self):
        return self.nombre

    class Meta:
        managed = True
        db_table = 'usuarios_empresas'
        verbose_name_plural = 'Empresas'


class Proyectos( models.Model ):
    id = models.AutoField( primary_key=True )
    activo = models.BooleanField( default = False )
    can_envio = models.IntegerField( default = 5 )
    ciclico = models.BooleanField( default = False ) #pendientemigracion
    ciclos = models.PositiveSmallIntegerField( default = 1 ) #pendientemigracion
    empresa = models.ForeignKey( Empresas )
    fec_registro =  models.DateTimeField( auto_now_add = True )
    iniciable = models.BooleanField( default = False )
    interna = models.BooleanField( default = False )
    pordenadas = models.BooleanField( default = False )
    max_variables = models.PositiveSmallIntegerField( default = 0 ) #Intrumentos para Go2.1+
    nombre =  models.CharField( max_length = 255 )
    prudenciamax = models.FloatField( default = 2 )
    prudenciamin = models.FloatField( default = 1 )
    tipo = models.CharField( max_length = 15, default = "Completa" )
    tot_preguntas = models.PositiveSmallIntegerField( default = 0)
    tot_participantes = models.PositiveIntegerField(default = 0)
    tot_aresponder = models.IntegerField( default = 0)
    tot_respuestas = models.IntegerField( default = 0)
    total = models.FloatField( default = 0 )
    usuarios = models.ManyToManyField( User )
    key = models.CharField(max_length=64, blank = True, null = True)
    zdel = models.DateTimeField( blank = True, null = True )

    def __unicode__(self):
        return self.nombre

    class Meta:
        managed = True
        db_table = 'cuestionarios_proyectos' #ojo con este nombre
        verbose_name_plural = 'Proyectos'


class ProyectosDatos( models.Model ):
    id = models.OneToOneField( Proyectos, primary_key = True )
    asunto = models.CharField( max_length = 75, blank = True, null = True )
    cue_correo = models.TextField( blank = True, null = True )
    fregistro = models.DateField( auto_now_add = True )
    int_encuesta = models.TextField( blank = True, null = True )
    logo = models.ImageField( upload_to = 'logos' )
    logoenc = models.ImageField( upload_to = 'logos', blank = True, null = True )
    censo = models.BooleanField( default = True )
    tit_encuesta = models.CharField( max_length = 255, blank = True, null = True )
    opcional1 = models.CharField( max_length=100, blank=True, null=True )
    opcional2 = models.CharField( max_length=100, blank=True, null=True )
    opcional3 = models.CharField( max_length=100, blank=True, null=True )
    opcional4 = models.CharField( max_length=100, blank=True, null=True )
    opcional5 = models.CharField( max_length=100, blank=True, null=True )
    msm = models.BooleanField( default = False )
    finicio = models.DateField( blank = True, null = True)
    ffin = models.DateField( blank = True, null = True)

    def __unicode__(self):
        return  "%s"%(self.id)

    class Meta:
        managed = True
        db_table = 'usuarios_proyectosdatos'
        verbose_name_plural = "Proyectos datos"

# para la migracion cambiar pre por red
class Permisos( models.Model ):
    id = models.OneToOneField( User, primary_key = True )
    consultor = models.BooleanField( default = False )
    act_surveys = models.BooleanField( default = False )
    act_variables = models.BooleanField( default = False )
    col_add = models.BooleanField( default = False )#colaboradores
    col_del = models.BooleanField( default = False )
    col_edit = models.BooleanField( default = False )
    col_see = models.BooleanField( default = False )
    cre_usuarios = models.BooleanField( default = False )
    det_see = models.BooleanField( default = False )#exportar graficas verlas en detallado
    max_pro_usados = models.PositiveSmallIntegerField( default = 0 )
    max_proyectos = models.PositiveSmallIntegerField( default = 0 )
    pro_add = models.BooleanField( default = False )#proyectos
    pro_del = models.BooleanField( default = False )
    pro_edit = models.BooleanField( default = False )
    pro_see = models.BooleanField( default = False )
    red_add = models.BooleanField( default = False ) #Columna_Agregar antes pre (preguntas) #pendientemigracion
    red_del = models.BooleanField( default = False ) #pendientemigracion
    red_edit = models.BooleanField( default = False ) #pendientemigracion
    red_see = models.BooleanField( default = False )#redes #pendientemigracion
    res_exp = models.BooleanField( default = False )#exportar resultados #pendientemigracion
    res_see = models.BooleanField( default = False )#graficas
    var_add = models.BooleanField( default = False )#"variacion" pasan a a ser cuestionarios
    var_del = models.BooleanField( default = False )
    var_edit = models.BooleanField( default = False )
    var_see = models.BooleanField( default = False )

    def __unicode__(self):
        return '%s'%(self.id)

    class Meta:
        managed = True
        db_table = 'usuarios_permisos'
        verbose_name_plural = 'Permisos'


class IndiceUsuarios( MPTTModel ):
    id = models.AutoField( primary_key = True )
    usuario =  models.OneToOneField( User )
    name = models.CharField( max_length = 100, db_index=True )
    parent = TreeForeignKey('self', null=True, blank = True )

    def __unicode__( self ):
        return '%s' %(self.name)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        managed = True
        db_table = "usuarios_indice"
        verbose_name_plural = "Indice de usuarios"


class Logs( models.Model ):
    id = models.AutoField( primary_key=True )
    usuario = models.CharField( max_length=1000 )
    usuario_username = models.CharField( max_length=1000 )
    accion = models.TextField( )
    descripcion = models.TextField( )
    fregistro = models.DateTimeField( auto_now_add = True )

    def __unicode__(self):
        return '%s %s %s'%(self.usuario,self.accion,self.descripcion )

    class Meta:
        managed = True
        db_table = 'usuarios_logs'
        verbose_name_plural = 'Logs'


class Recuperar( models.Model ):
    id = models.AutoField( primary_key=True )
    usuario = models.ForeignKey( User )
    link = models.CharField( max_length = 96 )
    fregistro = models.DateTimeField( auto_now_add = True )

    def __unicode__(self):
        return '%s'%self.usuario

    class Meta:
        managed = True
        db_table = 'usuarios_recuperar'
        verbose_name_plural = 'Recuperar'


class Errores( models.Model ):
    id = models.AutoField( primary_key=True )
    usuario = models.CharField( max_length = 500 )
    reporte = models.TextField()
    imagen = models.ImageField( upload_to = 'errores', blank = True, null = True )
    fregistro = models.DateTimeField( auto_now_add = True )

    def __unicode__(self):
        return '%s'%self.id

    class Meta:
        managed = True
        db_table = 'usuarios_errores'
        verbose_name_plural = 'Errores'


class Desafio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=500, null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.nombre


class DesafioSeleccionado(models.Model):
    id = models.AutoField(primary_key=True)
    desafio = models.ManyToManyField('usuarios.Desafio', related_name='desafio')
    nombre = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=50, blank=True, null=True)
    mensaje = models.TextField()

    def __unicode__(self):
        return '%s' % self.nombre
