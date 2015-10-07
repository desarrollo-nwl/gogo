# -*- encoding: utf-8 -*-
from colaboradores.models import Colaboradores,ColaboradoresMetricas
from cuestionarios.models import Variables,Preguntas
from datetime import datetime as DT
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_control
from mensajeria.models import Streaming,SRS
from usuarios.models import *

from datetime import timedelta
from django.utils import timezone
import json


#===============================================================================
# Administrar el envio
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def gosurvey(request):
	proyecto = cache.get(request.user.username)
	if not proyecto:
		return render_to_response('423.html')
	permisos = request.user.permisos
	datos = proyecto.proyectosdatos
	if permisos.consultor:
		if request.method == 'POST':
			if(permisos.act_surveys):
				try:
					comprobar = request.POST['iniciable']
					if(permisos.max_proyectos - permisos.max_pro_usados >= 1):
						permisos.max_pro_usados += 1
						proyecto.iniciable = True
						with transaction.atomic():
							permisos.save()
							proyecto.save()
							nom_log = request.user.first_name+' '+request.user.last_name
							Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,accion='Activó el proyecto',descripcion=proyecto.nombre)
							cache.set(request.user.username,proyecto,86400)

					else:
						return render_to_response('gosurvey.html',{
						'Activar':'Configuracion','activar':'IniciarDetener','Proyecto':proyecto,
						'Permisos':permisos,'Error':'Ha excedido el cupo de activaciones. No se pudo completar la solicitud'
						}, context_instance=RequestContext(request))
				except:
					pass
			try:
				comprobar = request.POST['activo']

				if(float(request.POST['dMin']) < float(request.POST['dMax'])):
					dMax = float(request.POST['dMax'])
					dMin = float(request.POST['dMin'])
				else:
					if(float(request.POST['dMin']) == float(request.POST['dMax'])):
						dMin = float(request.POST['dMin'])
						dMax = float(request.POST['dMax'])+1
					else:
						dMax = float(request.POST['dMin'])
						dMin = float(request.POST['dMax'])

				if(proyecto.activo):
					proyecto.activo = False
				else:
					proyecto.activo = True
				try:
					datos.finicio = DT.strptime(str(request.POST['fec_inicio']),'%d/%m/%Y')
					datos.ffin = DT.strptime(str(request.POST['fec_fin']),'%d/%m/%Y')
				except:
					pass

				proyecto.prudenciamin = dMin
				proyecto.prudenciamax = dMax
				proyecto.can_envio = request.POST['can_envio']
				streaming_crear =[]
				metricas = []
				if(proyecto.activo):
					colaboradores = Colaboradores.objects.filter(proyecto=proyecto)
					variables = proyecto.variables_set.all()
					preguntas = Preguntas.objects.filter(variable__in=variables)
					for i in colaboradores:
						for j in preguntas:
							if not Streaming.objects.filter(proyecto=proyecto,colaborador=i,pregunta=j).exists():
								streaming_crear.append(Streaming(proyecto=proyecto,colaborador=i,pregunta=j))
								proyecto.tot_aresponder += 1
				with transaction.atomic():
					if(streaming_crear):
						Streaming.objects.bulk_create(streaming_crear)
					proyecto.save()
					datos.save()
					cache.set(request.user.username,proyecto,86400)
			except:
				pass
		return render_to_response('gosurvey.html',{
		'Activar':'Configuracion','activar':'IniciarDetener','Proyecto':proyecto,'Permisos':permisos
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def detalladas(request):
	proyecto = cache.get(request.user.username)
	permisos = request.user.permisos
	if permisos.consultor and permisos.det_see:
		respuestas = Streaming.objects.filter(proyecto = proyecto,
						respuesta__isnull=False).select_related('pregunta',
						'colaborador__colaboradoresdatos__cargo')
	else:
		return render_to_response('403.html')

	return render_to_response('detalladas.html',{
	'Activar':'EstadoAvance','activar':'RepuestasDetalladas','Proyecto':proyecto,'Permisos':permisos,
	'Participantes':respuestas
	},	context_instance=RequestContext(request))


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def metricas(request):
	proyecto = cache.get(request.user.username)
	permisos = request.user.permisos

	participantes = Colaboradores.objects.filter(proyecto = proyecto
					).select_related('colaboradoresdatos',
					'colaboradoresmetricas')

	return render_to_response('metricas.html',{
	'Activar':'EstadoAvance','activar':'EnviosRespuestas','Proyecto':proyecto,'Permisos':permisos,
	'Participantes':participantes
	},	context_instance=RequestContext(request))


#aqui falta el reenvío manual


@cache_control(no_store=True)
def encuesta(request,id_proyecto,key):
	try:
		encuestado = Colaboradores.objects.only('nombre','proyecto__proyectosdatos',
					'proyecto__tot_respuestas','proyecto__can_envio','colaboradoresmetricas'
					).filter(proyecto_id=int(id_proyecto)
					).select_related('proyecto__proyectosdatos','colaboradoresmetricas',
					'proyecto__tot_respuestas','proyecto__can_envio'
					).get(key=key)
		stream = Streaming.objects.filter(
					colaborador = encuestado,
					respuesta__isnull = True).prefetch_related(
					'pregunta__respuestas_set').select_related('pregunta__variable'
					).order_by('pregunta__variable__posicion')
		proyecto = encuestado.proyecto
		total_cuestionario = len(stream)
	except:
		return render_to_response('404.html')
	try:
		ultima_respuesta = Streaming.objects.only('fecharespuesta').filter(
						proyecto_id=proyecto.id,
						colaborador_id=encuestado.id,
						respuesta__isnull=False
						).latest('fecharespuesta')
		pronto_acceso = (timezone.now() - ultima_respuesta.fecharespuesta).days
		print pronto_acceso
		if (pronto_acceso <= proyecto.prudenciamin):
			acceso = False
		else:
			acceso = True
	except:
		acceso = True

	if(stream and encuestado.proyecto.activo and acceso):
		if (proyecto.tipo != 'Completa'):
			i = 0
			len_cuestionario = 0
			cuestionario =[]
			cuestionario_preguntas =[]
			while( len_cuestionario < encuestado.proyecto.can_envio and i < total_cuestionario):
				if(stream[i].pregunta.estado):
					cuestionario.append(stream[i])
					cuestionario_preguntas.append(stream[i].pregunta)
					len_cuestionario += 1
				i += 1

			if not len_cuestionario:
				try:
					return HttpResponseRedirect('http://'+str(encuestado.poyecto.empresa.pagina))
				except:
					return HttpResponseRedirect('http://networkslab.co')
		else:
			cuestionario = stream
			cuestionario_preguntas =[]
			for i in cuestionario:
				cuestionario_preguntas.append(i.pregunta)
	else:
		try:
			return HttpResponseRedirect('http://'+str(encuestado.poyecto.empresa.pagina))
		except:
			return HttpResponseRedirect('http://networkslab.co')

	if request.method == 'POST':
		proyecto.tot_respuestas += len_cuestionario
		chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
		key = ''.join(random.sample(chars, 64))
		encuestado.key = key
		encuestado.repuestas += 1
		proyecto.total = 100*(proyecto.tot_respuestas/proyecto.tot_aresponder)
		metricas = encuestado.colaboradoresmetricas
		vec_metricas = json.loads(metricas.propension)
		try:
			vec_metricas.append((timezone.now()-stream[0].fec_controlenvio).days)
			metricas.propension = json.dumps(vec_metricas)
		except:
			vec_metricas.append(proyecto.prudenciamin)
		encuestado.propension = sum(vec_metricas)/len(vec_metricas)
		metricas.propension = json.dumps(vec_metricas)
		print metricas.propension
		with transaction.atomic():
			metricas.save()
			proyecto.save()
			encuestado.save()
			for i in cuestionario:
				i.fecharespuesta = timezone.now()
				if i.pregunta.abierta:
					print request.POST[str(i.pregunta.id)]
					i.respuesta = request.POST[str(i.pregunta.id)]
				elif i.pregunta.multiple:
					r = json.dumps(request.POST.getlist(str(i.pregunta.id)))
					i.respuesta = r
				else:
					i.respuesta = request.POST[str(i.pregunta.id)]
				i.save()
			Streaming.objects.filter(colaborador = encuestado).update(fec_controlenvio=timezone.now())
		try:
			return HttpResponseRedirect('http://'+str(encuestado.proyecto.empresa.pagina))
		except:
			return HttpResponseRedirect('http://networkslab.co')

	return render_to_response('encuesta.html',{
	'Encuestado':encuestado,'Preguntas':cuestionario_preguntas,
	},	context_instance=RequestContext(request))
