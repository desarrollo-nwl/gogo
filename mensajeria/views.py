# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_control
from usuarios.models import *
from mensajeria.models import Streaming,SRS
from cuestionarios.models import Variables,Preguntas
from colaboradores.models import Colaboradores,ColaboradoresMetricas
from datetime import datetime as DT

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
							Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,accion="Activó el proyecto",descripcion=proyecto.nombre)
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
				streaming_crear =[]
				metricas = []
				if(proyecto.activo):
					colaboradores = Colaboradores.objects.filter(proyecto=proyecto)
					variables = proyecto.variables_set.all()
					preguntas = Preguntas.objects.filter(variable__in=variables)
					for i in colaboradores:
						metricas.append(ColaboradoresMetricas(id=i))
						for j in preguntas:
							if not Streaming.objects.filter(proyecto=proyecto,colaborador=i,pregunta=j).exists():
								streaming_crear.append(Streaming(proyecto=proyecto,colaborador=i,pregunta=j))

				with transaction.atomic():
					if(streaming_crear):
						Streaming.objects.bulk_create(streaming_crear)
						ColaboradoresMetricas.objects.bulk_create(metricas)
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
def Respuestas(request):
	proyecto = cache.get(request.user.username)
	permisos = request.user.permisos
	if permisos.consultor and permisos.det_see:
		respuestas = Streaming.objects.filter(
				proyecto = proyecto).defear(
				'fec_controlenvio','fecharespuesta').select_related(
				'colaborador','pregunta')
	else:
		return render_to_response('403.html')

	return render_to_response('stream.html',{
	'activar':'survey','Proyecto':proyecto,'Permisos':permisos,
	'Respuestas':respuestas
	},	context_instance=RequestContext(request))



@cache_control(no_store=True)
def encuesta(request,key):
	encuactivo = Colaboradores.objects.get(key=key).select_related("proyecto__empresa")
	Preguntas = Streaming.objects.filter(
			colaborador = encuactivo,
			respuesta__isnull = True).select_related(
			'pregunta__variable').prefetch_related(
			'pregunta_set')
	total_cuestionario = len(Preguntas)
	if(Preguntas and encuactivo.proyecto.activo):
		i = 0
		len_cuestionario = 0
		cuestionario =[]
		cuestionario_preguntas =[]
		cuestionario_variables =[]
		while( len_cuestionario < encuactivo.proyecto.can_envio and i < total_cuestionario):
			if(Preguntas[i].pregunta.activa):
				cuestionario.append(Preguntas[i])
				cuestionario_preguntas.append(Preguntas[i].pregunta)### usaremos template regroup
				cuestionario_variables.append(Preguntas[i].pregunta.variable)
				len_cuestionario += 1
			i += 1
	else:
		try:
			return HttpResponseRedirect('http://'+str(encuactivo.poyecto.empresa.pagina))
		except:
			return HttpResponseRedirect('http://networkslab.co')

	if request.method == 'POST':
		for i in cuestionario:
			streaming = Streaming.objects.get(id =i.id)
			streaming.fecharespuesta = timezone.now()
			streaming.save()
			for i in xrange(request.POST['repuestas de esta pregunta']):### falta acoplarlo para las vistas
				respuesta = StreamingRespuestas(request.POST[str(i)], streaming = R )
			Streaming.objects.filter(colaborador = encuactivo).update(fec_controlenvio=timezone.now())
		try:
			return HttpResponseRedirect('http://'+str(encuactivo.poyecto.empresa.pagina))
		except:
			return HttpResponseRedirect('http://networkslab.co')


	return render_to_response('encuesta2.html',{
	###aqui van las variables
	},	context_instance=RequestContext(request))
