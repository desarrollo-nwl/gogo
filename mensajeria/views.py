# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.cache import cache
# from django.db import connection
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_control
from usuarios.models import *

#===============================================================================
# Administrar el envio
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def igsurvey(request):
    proyecto = cache.get(request.user.username)
    permisos = request.user.permisos
    if permisos.consultor:
    	if request.method == 'POST':
    		if(permisos.act_surveys):
    			try:
                    comprobar = request.post['iniciable']
                    iniciable = 1 - int(proyecto.iniciable)
                    proyecto.iniciable = iniciable
        			proyecto.save()
                    cache.set(request.user.username,proyecto,86400)
                except:
                    pass
    		try:
                comprobar = request.post['activo']
                activo = 1- int(proyecto.activo)
                proyecto.activo = activo
                if(activo):
                    encolar(proyecto,5)
                proyecto.save()
                cache.set(request.user.username,proyecto,86400)
			except:
                pass
		total = Streaming.objects.filter(proyecto = proyecto).count()
		respuesto = Streaming.objects.filter(
                    proyecto = proyecto,
                    respuesta__isnull=False).count()
        try:
            porcentaje = round(100*total/respuesto,2)
		except:
			porcentaje = 0

    	return render_to_response('igsurvey.html', {
    	'activar':'survey','Proyecto':proyecto,'Permisos':permisos,
        'Total': total,'Respuesto',respuesto,'Porcentaje',porcentaje,
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
	encuestado = Colaboradores.objects.get(key=key).select_related("proyecto__empresa")
	Preguntas = Streaming.objects.filter(
            colaborador = encuestado,
            respuesta__isnull = True).select_related(
            'pregunta__variable').prefetch_related(
            'pregunta_set')
    total_cuestionario = len(Preguntas)
    if(Preguntas and encuestado.proyecto.activo):
        i = 0
        len_cuestionario = 0
        cuestionario =[]
        cuestionario_preguntas =[]
        cuestionario_variables =[]
        while( len_cuestionario < encuestado.proyecto.can_envio and i < total_cuestionario):
            if(Preguntas[i].pregunta.activa):
                cuestionario.append(Preguntas[i])
                cuestionario_preguntas.append(Preguntas[i].pregunta)### usaremos template regroup
                cuestionario_variables.append(Preguntas[i].pregunta.variable)
                len_cuestionario += 1
            i += 1
    else:
        try:
            return HttpResponseRedirect('http://'+str(encuestado.poyecto.empresa.pagina))
        except:
            return HttpResponseRedirect('http://networkslab.co')

	if request.method == 'POST':
		for i in cuestionario:
			R = Streaming.objects.get(id =i.id)
			R.fecharespuesta = timezone.now()
			R.respuesta = request.POST[str(i.id)] ### falta hacerlo para todos los tipos de pregunta
			R.save()
			R = Streaming.objects.filter(colaborador = encuestado).update(fec_controlenvio=timezone.now())
        try:
            return HttpResponseRedirect('http://'+str(encuestado.poyecto.empresa.pagina))
        except:
            return HttpResponseRedirect('http://networkslab.co')


	up = len(auxvar)+1
	lenu = range(1,up)

	return render_to_response('encuesta2.html',{
	'EMA': C.nombre,'up':up,'lenu':lenu,'Preguntas':pregparalaencuesta,
	'variables':auxvar,'Proyecto':pro
	},	context_instance=RequestContext(request))
