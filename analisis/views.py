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
from mensajeria_360.models import Streaming_360
from usuarios.models import Proyectos,ProyectosDatos, Logs
import grafos as gr
import string,datetime
import json
from django.core import serializers

from datetime import timedelta


SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR
WEEK = 7 * DAY
MONTH = 30 * DAY

def humanize(dt):
    now = datetime.date.today()
    delta_time = dt - now

    delta =  delta_time.days * DAY + delta_time.seconds
    minutes = delta / MINUTE
    hours = delta / HOUR
    days = delta / DAY

    if delta <  0:
        return "Ha finalizado"

    if delta < 1 * MINUTE:
      if delta == 1:
          return  "Un segundo"
      else:
          return ''.join([str(delta) , " segundos"])

    if delta < 2 * MINUTE:
        return "Un minuto"

    if delta < 45 * MINUTE:
        return ''.join([str(minutes) , " minutos"])

    if delta < 90 * MINUTE:
        return "Una hora"

    if delta < 24 * HOUR:
        return ''.join([str(hours) , " horas"])

    if delta < 48 * HOUR:
        return "Mañana"

    if delta < 30 * DAY:
        return ''.join([str(days) , " dias"])

    if delta < 12 * MONTH:
        months = delta / MONTH
        if months <= 1:
            return "Un mes"
        else:
            semanas =  days / 30 -1
            if semanas > 1:
                return ''.join([str(months) , " meses, " , str(semanas) ," semanas"])
            elif semanas == 1:
                return ''.join([str(months) , " meses, " , str(semanas) ," semana"])
            else:
                return ''.join([str(months) , " meses"])
    else:
      years = days / 365.0
      if  years <= 1:
          return "Un año"
      else:
          return ''.join([str(months) , " años"])


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def participacion(request):
    proyecto = cache.get(request.user.username)

    if not proyecto:
        return render_to_response('423.html')
    if proyecto.tipo in ["Completa","Fragmenta","Externa"] :
        permisos = request.user.permisos
        if permisos.res_see:
            datos = Streaming.objects.filter(
                        proyecto_id=proyecto.id
                    ).select_related(
                        'proyecto__proyectosdatos',
                        'colaborador','colaborador__colaboradoresdatos'
                    )
            if( proyecto.tot_preguntas and proyecto.tot_respuestas ):
                finalizados = proyecto.tot_respuestas/proyecto.tot_preguntas
            else:
                finalizados = 0
            print '#################################################3'
            data = serializers.serialize("json", datos)
            print datos
            return render_to_response('participacion.html',{
                'Activar':'AnalisisResultados','activar':'Participacion',
                'Proyecto':proyecto,'Permisos':permisos,'Datos':datos,'Finalizados':finalizados
            }, context_instance=RequestContext(request))
        else:
            return render_to_response('403.html')
    else:
        permisos = request.user.permisos
        if permisos.res_see:
            datos = Streaming_360.objects.filter(
                        proyecto_id=proyecto.id
                    ).select_related(
                        'proyecto__proyectosdatos',
                        'colaborador','colaborador__colaboradoresdatos_360'
                    ).values()
            if( proyecto.tot_preguntas and proyecto.tot_respuestas ):
                finalizados = proyecto.tot_respuestas/proyecto.tot_preguntas
            else:
                finalizados = 0
            print '#################################################3'
            print datos
            json.JSONEncoder.default = lambda self,obj: (obj.isoformat() if isinstance(obj, datetime.datetime) else None)
            js_data = json.dumps(list(datos))

            # data = serializers.serialize("json", datos)
            # for i in datos:
            #     # print i.instrumento
            #     for j in i.instrumento.dimension.all():
            #         print j.nombre
            return render_to_response('analisis_instrumento.html',{
                'Activar':'AnalisisResultados','activar':'Participacion',
                'Proyecto':proyecto,'Permisos':permisos,'Datos':js_data,'Finalizados':finalizados
            }, context_instance=RequestContext(request))
        else:
            return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def general(request):
    proyecto = cache.get(request.user.username)

    if not proyecto:
        return render_to_response('423.html')
    permisos = request.user.permisos
    if permisos.res_see:
        variables = Variables.objects.filter(proyecto_id=proyecto.id)
        preguntas = Preguntas.objects.prefetch_related('respuestas_set').filter(variable__in=variables,abierta=False)
        datos = Streaming.objects.filter(
                    proyecto_id=proyecto.id,
                    pregunta__abierta=False,
                    respuesta__isnull=False
                ).select_related(
                    'proyecto__proyectosdatos',
                    'pregunta','pregunta__variable',
                    'colaborador','colaborador__colaboradoresdatos'
                ).order_by('fecharespuesta')
        return render_to_response('focalizado.html',{
            'Activar':'AnalisisResultados','activar':'Focalizados',
            'Proyecto':proyecto,'Permisos':permisos,'Datos':datos,'Preguntas':preguntas
        }, context_instance=RequestContext(request))

    else:
        return render_to_response('403.html')

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def focalizado(request):
    proyecto = cache.get(request.user.username)

    pdatos = proyecto.proyectosdatos
    if not proyecto or proyecto.tipo in ["360 redes","360 unico"]:
        return render_to_response('423.html')
    permisos = request.user.permisos
    if permisos.res_see:
        if proyecto.iniciable:
            variables = Variables.objects.filter(proyecto_id=proyecto.id)
            preguntas = Preguntas.objects.prefetch_related('respuestas_set').filter(variable__in=variables,abierta=False)
            datos = Streaming.objects.only(
                    'respuesta','fecharespuesta',
                    'pregunta__multiple',
                    'colaborador_id','pregunta_id',
                    'pregunta'
                    ).filter(
                        proyecto_id=proyecto.id,
                        pregunta__abierta=False,
                        respuesta__isnull=False
                    ).select_related('pregunta')

            colaboradores = Colaboradores.objects.only('id').filter(proyecto_id = proyecto.id)
            colaboradores = ColaboradoresDatos.objects.only(
                'id_id','area','cargo','ciudad','opcional1','opcional2','opcional3',
                'opcional4','opcional5','ciudad','regional'
                ).filter( id__in = colaboradores)

            variables = Variables.objects.only('id').filter(proyecto_id = proyecto.id)
            cuestionario = Preguntas.objects.only(
                            'id','texto','variable__nombre'
                            ).filter(variable__in =  variables
                            ).select_related('variable__nombre'
                            ).prefetch_related('respuestas_set')

            return render_to_response('focalizado.html',{
                'Activar':'AnalisisResultados','activar':'Focalizados','PDatos':pdatos,
                'Proyecto':proyecto,'Permisos':permisos,'Datos':datos,'Cuestionario':cuestionario,
                'Participantes':colaboradores
            }, context_instance=RequestContext(request))
        else:
            return render_to_response('sindatos.html',{
                'Activar':'AnalisisResultados','activar':'Focalizado','Localizacion':'Focalizado',
                'Proyecto':proyecto,'Permisos':permisos
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
    if not proyecto or proyecto.tipo in ["360 redes","360 unico"]:
        return render_to_response('423.html')
    permisos = request.user.permisos
    if permisos.res_see:

            objetosStreaming = Streaming.objects.filter(
                                    proyecto_id=proyecto.id,
                                    pregunta__abierta = True,
                                    pregunta__cuerpo = False,
                                    respuesta__isnull = False
                                ).select_related(
                                    'pregunta'
                                ).prefetch_related(
                                    'pregunta__respuestas_set'
                                )

            listaPreguntas = []
            datasetgrafo = []
            for i in objetosStreaming:
                if i.pregunta in listaPreguntas:
                    indi = listaPreguntas.index(i.pregunta)
                    datasetgrafo[indi].append(i.respuesta)
                elif i.pregunta not in listaPreguntas:
                    listaPreguntas.append(i.pregunta)
                    datasetgrafo.append([i.pregunta,i.respuesta])
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


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def cuerpo(request):
    proyecto = cache.get(request.user.username)
    if not proyecto or proyecto.tipo in ["360 redes","360 unico"]:
        return render_to_response('423.html')
    permisos = request.user.permisos
    if permisos.res_see:

        datos = Streaming.objects.only(
                 "pregunta__texto","pregunta__cuerpo",
                 "colaborador__nombre",
                 "colaborador__apellido",
                 "colaborador__colaboradoresdatos__regional",
                 "colaborador__colaboradoresdatos__ciudad",
                 "colaborador__colaboradoresdatos__area",
                 "colaborador__colaboradoresdatos__cargo",
                 "respuesta","fecharespuesta",
                ).filter(
                    proyecto_id = proyecto.id,
                    pregunta__cuerpo = True,
                    respuesta__isnull = False
                ).select_related(
                    "colaborador__colaboradoresdatos",
                    "pregunta",
                )
        fechas = proyecto.proyectosdatos
        return render_to_response('cuerpo.html',{
            'Activar':'AnalisisResultados',
            'activar':'CuerpoHumano',
            'Proyecto':proyecto,
            'fechas': fechas, 
            'Permisos':permisos,
            'activarG':3,
            'Datos': datos,
        }, context_instance=RequestContext(request))
    else:
        return render_to_response('403.html')
