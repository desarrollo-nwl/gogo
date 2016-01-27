# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import transaction
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.views.decorators.cache import cache_control
from colaboradores.models import Colaboradores, ColaboradoresDatos
from cuestionarios.models import  Preguntas, Variables, Respuestas
from mensajeria.models import Streaming
from usuarios.models import Proyectos, Logs


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def focalizados(request):
	proyecto = cache.get(request.user.username)
	if not proyecto:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.res_see:
		# Ivan hace el superquery para mandar al js
		return render_to_response('focalizado.html',{
		'Activar':'AnalisisResultados','activar':'Focalizados',
		'Proyecto':proyecto,'Permisos':permisos,
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


# HINTS
# streaming.objects.filter(preguntas__in=preguntas_abiertas)
# preguntas_abiertas = Preguntas.objects.filter(abierta=True, proyecto_id=1)
# el proyecton se recoge de la cache
# streaming.objects.filter(preguntas__in=preguntas_abiertas,respuestas__isnull=False)
# hint1: la tabla streaming esta en mensajeria
# hint2: la tabla preguntas esta en cuestionarios
# hint3: programar en las views de analisis


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def wordanalytics(request):
	proyecto = cache.get(request.user.username)
	# if not proyecto:
	# 	return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.res_see:
		# Lucho se encarga de hacer lo que necesita aqui
		return render_to_response('wordanalytics.html',{
		'Activar':'AnalisisResultados','activar':'WordAnalytics',
		'Proyecto':proyecto,'Permisos':permisos,
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def grafoLocal(request):

	return render_to_response('grafos.html',{},context_instance =RequestContext(request))
