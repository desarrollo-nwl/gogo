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
from cuestionarios.models import Variables
from exp_usuario.models import Planes, Lideres
# Create your views here.

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def planesAccion(request):
    proyecto = cache.get(request.user.username)
    planes = Planes.objects.filter(proyecto_id = proyecto.id )
    print planes
    variables = Variables.objects.filter(proyecto_id = proyecto.id,estado = True)
    lideres = Lideres.objects.filter(proyecto_id = proyecto.id)
    if request.method == 'POST':
        contador = request.POST['numeroPlanes']
        contador = int(contador) + 1
        # try:
        #     with transaction.atomic():
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
            )
        # except:
        #     print 'errror'


    return render_to_response('planesAccion.html',{
        'Activar':'Contenido','activar':'Instrumentos',
        'variables': variables,
        'lideres': lideres,
        'planes': planes,
        },context_instance=RequestContext(request))

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def puntosTalenter(request):
    return render_to_response('puntosTalenter.html',{
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
