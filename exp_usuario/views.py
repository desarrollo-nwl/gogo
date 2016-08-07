# -*- encoding: utf-8 -*-
from datetime import datetime
from django.shortcuts import render
from cuestionarios_360.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import transaction
from django.db.models import F
from django.http import HttpResponseRedirect,HttpResponse
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils import timezone
from django.views.decorators.cache import cache_control
from mensajeria_360.models import Streaming_360
from usuarios.models import Empresas, Proyectos, Logs
from exp_usuario.models import Planes, Lideres, ColaboradoresExpUsuario
from cuestionarios_360.models import Variables_360, Preguntas_360
import ujson
# Create your views here.

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def planesAccion(request):
    proyecto = request.user.username
    planes = Planes.objects.select_related().filter(proyecto_id = proyecto.id )
    variables = Variables_360.objects.filter(proyecto_id = proyecto.id,estado = True)
    lideres = Lideres.objects.filter(proyecto_id = proyecto.id)
    #  PROCESO DE CREACION CUESTIONARIO OPTIMIZAR CON C++
    datos = Streaming_360.objects.filter(proyecto__id = proyecto.id,respuesta__isnull = False)
    preguntas = Preguntas_360.objects.filter(proyecto_id = proyecto.id )
    # for pregunta in preguntasObjetos:
    #     vector = [pregunta.id]
    #     for respuesta in pregunta.respuestas_360_set.all():
    #         vector.append(respuesta)
    #     cuestionario.append(vector)
    if request.method == 'POST':
        contador = request.POST['numeroPlanes']
        contador = int(contador) + 1
        try:
            with transaction.atomic():
                for i in range(contador):
                    lider = request.POST['lider%s'%i]
                    planAccion = request.POST['planAccion%s'%i]
                    fechaInicio = request.POST['fechaInicio%s'%i]
                    fechaFin = request.POST['fechaFin%s'%i]
                    variable = request.POST['variable%s'%i]
                    lider = Lideres.objects.get(id = lider )
                    Planes.objects.create(
                    proyecto = proyecto,
                    lider = lider,
                    plan = planAccion,
                    fechaInicio = fechaInicio,
                    fechaFin = fechaFin,
                    )
        except:
            print 'errror'
    print 'hola'
    print 'soy variable %s'%lideres
    return render_to_response('planesAccion.html',{
        'Activar':'Contenido','activar':'Instrumentos',
        'variables': variables,
        'lideres': lideres,
        'planes': planes,
        'idProyecto': proyecto.id,
        'datos': datos,
        'preguntas': preguntas,
        },context_instance=RequestContext(request))


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def planesAccionPeticionAjax(request):
    if request.method == 'POST':
        idProyecto = int(request.POST['idProyecto'])
        idLider = request.POST['filtroLider']
        lider = Lideres.objects.get(id = idLider)
        idLiderColaborador = lider.lider.id
        datosLider = Streaming_360.objects.filter(evaluado = lider.lider)
        ###CONSTRUCCION TABLA DE PLANES POR LIDER
        planes = lider.planes_set.all()
        a = [idLiderColaborador]
        for i in planes:
            print 'holA'
            b = {'plan':i.plan,'avance':i.avance,'impacto':i.impacto,'fechaInicio':'%s/%s/%s'%(i.fechaInicio.year,i.fechaInicio.month,i.fechaInicio.day),'fechaFin':'%s/%s/%s'%(i.fechaFin.year,i.fechaFin.month,i.fechaFin.day)}
            a.append(b)
        a = ujson.dumps(a)


    return HttpResponse(a,content_type='aplication/json')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def puntosTalenter(request):
    proyecto = request.user.username
    colaboradoresExpUsuario = ColaboradoresExpUsuario.objects.filter(proyecto_id = proyecto.id)
    return render_to_response('puntosTalenter.html',{
        'colaboradoresExpUsuario': colaboradoresExpUsuario,
        'Activar':'Contenido','activar':'Instrumentos',
        },context_instance=RequestContext(request))

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def miLiderazgo(request):
    return render_to_response('miLiderazgo.html',{
        'Activar':'Contenido','activar':'Instrumentos',
        },context_instance=RequestContext(request))

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def dashBoard(request):
    return render_to_response('dashBoard.html',{
        'Activar':'Contenido','activar':'Instrumentos',
        },context_instance=RequestContext(request))
