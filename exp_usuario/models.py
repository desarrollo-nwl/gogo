from django.db import models
from usuarios.models import Proyectos
from colaboradores.models import Colaboradores

# Create your models here.
############## PENDIENTE DE CONFIRMACION !!!!!!!!!!!!!!!!
class Lideres(models.Model):
    proyecto = models.ForeignKey(Proyectos,blank = True, null = True)
    lider = models.ForeignKey(Colaboradores,blank = True, null = True)

class CategoriasProductos(models.Model):
    proyecto = models.ForeignKey(Proyectos,blank = True, null = True )
    categoria = models.CharField(max_length = 100)
    observaciones = models.CharField(max_length = 500)


class Productos(models.Model):
    categoria = models.ForeignKey(CategoriasProductos,blank = True, null = True )
    producto = models.CharField(max_length = 100)
    puntos = models.FloatField(default = 0 )
    observaciones = models.CharField(max_length = 500,null = True, blank = True )
    canjeado  = models.FloatField(default = 0)


class ColaboradoresExpUsuario(models.Model):
    id  = models.OneToOneField(Colaboradores,primary_key  = True )
    lider = models.ForeignKey(Lideres, blank  = True, null = True )
    puntosLogrados = models.FloatField(default = 0 )
    puntosDisponibles = models.FloatField(default = 0 )
    premiosCanjeados = models.ManyToManyField(Productos, blank = True)

#####################3####################################3


class Planes(models.Model):
    proyecto = models.ForeignKey(Proyectos,blank = True, null = True)
    lider = models.ForeignKey(Lideres,null = True, blank = True)
    plan = models.CharField(max_length = 500,null = False,blank = False)
    avance = models.FloatField(default = 0 )
    impacto = models.FloatField(default = 0 )
    fechaInicio = models.DateField(blank = True, null = True )
    fechaFin = models.DateField(blank = True, null = True )
    observaciones = models.CharField(max_length = 500 )
    aprobacion = models.BooleanField(default = False )

class Comentarios(models.Model):
    comentario = models.FloatField(max_length  = 500)
    plan = models.ForeignKey(Planes,blank = True,null = True)
    colaboradorExpUsuario = models.ForeignKey(ColaboradoresExpUsuario,null = True,blank = True)
    fecha = models.DateField(blank = True, null = True )
