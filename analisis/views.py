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
import grafos as gr
import string

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def focalizados(request):
	proyecto = cache.get(request.user.username)
	if not proyecto:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.res_see:
		variables = Variables.objects.filter(proyecto_id=proyecto.id)
		preguntas = Preguntas.objects.prefetch_related('respuestas_set').filter(variable__in=variables,abierta=False)
		datos = Streaming.objects.filter(
				proyecto_id=proyecto.id,pregunta__abierta=False,respuesta__isnull=False
				).select_related('proyecto__proyectosdatos',
				'pregunta','pregunta__variable','colaborador','colaborador__colaboradoresdatos').order_by('fecharespuesta')
		return render_to_response('focalizado.html',{
		'Activar':'AnalisisResultados','activar':'Focalizados',
		'Proyecto':proyecto,'Permisos':permisos,'Datos':datos,'Preguntas':preguntas
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')



def solucion(a):
	a = str(a).lower()
	a = string.replace(a,',','')
	a = string.replace(a,'(','')
	a = string.replace(a,')','')
	a = string.replace(a,'[','')
	a = string.replace(a,']','')
	a = string.replace(a,'{','')
	a = string.replace(a,'}','')
	a = string.replace(a,"'",'')
	a = string.replace(a,'.','')
	a = string.replace(a,':','')
	a = string.replace(a,';','')
	a = string.replace(a,'=','')
	a = string.replace(a,'?','')
	a = string.replace(a,'¿','')
	a = string.replace(a,'&','')
	a = string.replace(a,'#','')
	a = string.replace(a,'%','porciento')
	a = string.replace(a,'|','')
	a = string.replace(a,'!','')
	a = string.replace(a,'¡','')
	a = string.replace(a,'á','a')
	a = string.replace(a,'é','e')
	a = string.replace(a,'í','i')
	a = string.replace(a,'ó','o')
	a = string.replace(a,'ú','u')
	return a


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def wordanalytics(request):
	proyecto = cache.get(request.user.username)
	if not proyecto:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.res_see:
			# HINTS
			# streaming.objects.filter(preguntas__in=preguntas_abiertas)
			# preguntas_abiertas = Preguntas.objects.filter(abierta=True, proyecto_id=1)
			# el proyecton se recoge de la cache
			# streaming.objects.filter(preguntas__in=preguntas_abiertas,respuestas__isnull=False)
			# hint1: la tabla streaming esta en mensajeria
			# hint2: la tabla preguntas esta en cuestionarios
			# hint3: programar en las views de analisis
			preguntasAbiertas = Preguntas.objects.filter(abierta = True, proyecto_id = proyecto.id)
			objetosStreaming = Streaming.objects.filter(preguntas_in = preguntasAbiertas).filter(respuestas__isnull = False)
			listaPreguntas = []
			datasetgrafo = []
			for i in objetosStreaming:
				if i.pregunta in listaPreguntas:
					indi = listaPreguntas.index(i.pregunta)
					datasetgrafo[indi].append(i.respuesta)
				elif i.pregunta not in listaPreguntas:
					listaPreguntas.append(i.pregunta)
					dastasetgrafo.append([i.pregunta,i.respuesta])
			grafoPorPregunta,diccionariosPorPregunta,cantidades = gr.Grafos(datasetgrafo)
			listaPreguntas = gr.preguntas(datasetgrafo)
			return render_to_response('wordanalytics.html',{
			'Activar':'AnalisisResultados',
			'activar':'WordAnalytics',
			'Proyecto':proyecto,
			'Permisos':permisos,
			'activarG':3,
			'activar':'grafos',
			'grafos':grafoPorPregunta,'diccionarios':diccionariosPorPregunta,'cantidades':cantidades,'listaPreguntas':listaPreguntas,
			}, context_instance=RequestContext(request))

	else:
			return render_to_response('403.html')
