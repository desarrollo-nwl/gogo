# -*- encoding: utf-8 -*-
from colaboradores.models import Colaboradores,ColaboradoresMetricas
from cuestionarios.models import Variables,Preguntas
from datetime import datetime as DT
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import transaction
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_control
from mensajeria.models import *
from usuarios.models import *

from django.db.models import Avg
from datetime import timedelta,date
from django.utils import timezone
import datetime
import random
import json

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.utils
import smtplib

from django.db.models import Max
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
			if permisos.act_surveys:
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
				streaming_crear =[]
				if proyecto.interna:
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
					proyecto.prudenciamin = dMin
					proyecto.prudenciamax = dMax

					if proyecto.tipo != "Completa":
						proyecto.can_envio = request.POST['can_envio']

					if proyecto.activo:
						colaboradores = Colaboradores.objects.filter(proyecto=proyecto)
						variables = proyecto.variables_set.all()
						preguntas = Preguntas.objects.filter(variable__in=variables)
						for i in colaboradores:
							for j in preguntas:
								if not Streaming.objects.filter(proyecto=proyecto,colaborador=i,pregunta=j).exists():
									streaming_crear.append(Streaming(proyecto=proyecto,colaborador=i,pregunta=j))
									proyecto.tot_aresponder += 1
					if proyecto.tot_aresponder:
						proyecto.total = 100*(proyecto.tot_respuestas)/proyecto.tot_aresponder
				try:
					datos.finicio = DT.strptime(str(request.POST['fec_inicio']),'%d/%m/%Y')
					datos.ffin = DT.strptime(str(request.POST['fec_fin']),'%d/%m/%Y')
				except:
					pass
				if(proyecto.activo):
					proyecto.activo = False
				else:
					proyecto.activo = True
				with transaction.atomic():
					if streaming_crear:
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
	if not proyecto:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.det_see and permisos.res_see and proyecto.interna:
		respuestas = Streaming.objects.filter(proyecto = proyecto
						).select_related('colaborador','pregunta__variable')

	elif permisos.consultor and permisos.det_see and permisos.res_see and (not proyecto.interna):
		respuestas = Externa.objects.filter(proyecto = proyecto).select_related('pregunta__variable')
	else:
		return render_to_response('403.html')

	return render_to_response('detalladas.html',{
	'Activar':'EstadoAvance','activar':'RespuestasDetalladas','Proyecto':proyecto,'Permisos':permisos,
	'Participantes':respuestas
	},	context_instance=RequestContext(request))


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def metricas(request):
	proyecto = cache.get(request.user.username)
	if not proyecto:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and proyecto.interna:
		participantes = Colaboradores.objects.filter(proyecto = proyecto
						).select_related('colaboradoresdatos',
						'colaboradoresmetricas')
		average = Colaboradores.objects.filter(proyecto=proyecto).aggregate(Avg('propension'))
		return render_to_response('metricas.html',{
		'Activar':'EstadoAvance','activar':'EnviosRespuestas','Proyecto':proyecto,'Permisos':permisos,
		'Participantes':participantes,'Average':average
		},	context_instance=RequestContext(request))
	elif permisos.consultor and not proyecto.interna:
		metricas = MetricasExterna.objects.filter(proyecto = proyecto)
		average = MetricasExterna.objects.filter(proyecto=proyecto).aggregate(Avg('encuestados'))
		return render_to_response('metricas.html',{
		'Activar':'EstadoAvance','activar':'EnviosRespuestas','Proyecto':proyecto,'Permisos':permisos,
		'Metricas':metricas,'Average':average
		},	context_instance=RequestContext(request))
	else:
		return render_to_response('404.html')

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def colaboradoractivarmensajeria(request,id_colaborador):
	proyecto = cache.get(request.user.username)
	if not proyecto:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.col_edit:
		try:participante = Colaboradores.objects.only('estado').filter(proyecto=proyecto).get(id=int(id_colaborador))
		except:return render_to_response('403.html')
		if(participante.estado):
			participante.estado = False
		else:
			participante.estado = True
		participante.save()
		return HttpResponseRedirect('/respuestas/metricas')
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def colaboradoreenviar(request,id_colaborador):
	proyecto = cache.get(request.user.username)
	if not proyecto:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and proyecto.activo:
		try:
			colaborador = Colaboradores.objects.get(id=int(id_colaborador))
			if Streaming.objects.filter(colaborador=int(id_colaborador),respuesta__isnull=True).exists():
				alerta = None
				if request.method == 'POST':
					if colaborador.estado:
						datos = proyecto.proyectosdatos
						from usuarios.strings import correo_standar
						from corrector import salvar_html
						import cgi,unicodedata
						server=smtplib.SMTP('smtp.mandrillapp.com',587)
						server.ehlo()
						server.starttls()
						server.login('Team@goanalytics.com','pR6yG1ztNHT7xW6Y8yigfw')
						nom_log =request.user.first_name+' '+request.user.last_name
						Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,accion="Forzó reenvío a",descripcion=colaborador.nombre+" "+colaborador.apellido)
						destinatario = [colaborador.email]
						msg=MIMEMultipart()
						msg["subject"]=  cgi.escape(datos.asunto).decode("utf-8")
						msg['From'] = email.utils.formataddr(('GoAnalytics', 'Team@goanalytics.com'))
						urlimg = 'http://www.lavozdemisclientes.com'+datos.logo.url
						if colaborador.colaboradoresdatos.genero.lower() == "femenino":
							genero = "a"
						else:
							genero = "o"
						nombre = cgi.escape(colaborador.nombre).decode("utf-8").encode("ascii", "xmlcharrefreplace")
						titulo = cgi.escape(datos.tit_encuesta).decode("utf-8").encode("ascii", "xmlcharrefreplace")
						texto_correo = salvar_html(cgi.escape(datos.cue_correo).encode("ascii", "xmlcharrefreplace"))
						url = 'http://www.lavozdemisclientes.com/encuesta/'+str(proyecto.id)+'/'+colaborador.key
						html = correo_standar(urlimg,genero,nombre,titulo,texto_correo,url)
						mensaje = MIMEText(html,"html")
						msg.attach(mensaje)
						with transaction.atomic():
							colaborador.reenviados = colaborador.reenviados + 1
							Streaming.objects.filter(colaborador=colaborador).update(fec_controlenvio=timezone.now())
							colaborador.save()
							server.sendmail('Team@goanalytics.com',destinatario,msg.as_string())
						server.quit()
						alerta = 'Correo enviado exitosamente.'
					else:
						alerta = 'Debe activar primero al colaborador para forzar el envío. Asegúrese de tener los permisos necesarios para editar participantes.'
				return render_to_response('colaboradoreenviar.html',{
				'Activar':'EstadoAvance','activar':'EnviosRespuestas','Colaborador':colaborador,
				'Permisos':permisos,'Proyecto':proyecto,'Alerta':alerta
				}, context_instance=RequestContext(request))
			else:
				return render_to_response('403.html')
		except:
			return render_to_response('404.html')
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
def encuesta(request,id_proyecto,key):
	try:
		encuestado = Colaboradores.objects.only('nombre','proyecto__proyectosdatos',
					'proyecto__tot_respuestas','proyecto__can_envio','colaboradoresmetricas'
					).filter(proyecto_id=int(id_proyecto)
					).select_related('proyecto__proyectosdatos','colaboradoresmetricas',
					'proyecto__tot_respuestas','proyecto__can_envio'
					).get(key=key)
		if not encuestado.estado:
			return render_to_response('403.html')
		stream = Streaming.objects.filter(
					colaborador = encuestado,
					respuesta__isnull = True).prefetch_related(
					'pregunta__respuestas_set').select_related('pregunta__variable'
					).order_by('pregunta__variable__posicion')
		proyecto = encuestado.proyecto
		tiempo = datetime.date.today()
		datos = ProyectosDatos.objects.filter(ffin__gte=tiempo,finicio__lte=tiempo).get(id=proyecto)
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
		if (pronto_acceso < proyecto.prudenciamin):
			acceso = False
		else:
			acceso = True
	except:
		acceso = True

	if stream and encuestado.proyecto.activo and acceso:
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
					return HttpResponseRedirect('http://www.networkslab.co')
		else:
			cuestionario = stream
			len_cuestionario = len(stream)
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
		encuestado.respuestas += 1
		proyecto.total = 100*(1.0*proyecto.tot_respuestas/proyecto.tot_aresponder)
		metricas = encuestado.colaboradoresmetricas
		vec_metricas = json.loads(metricas.propension)
		try:
			vec_metricas.append((timezone.now()-stream[0].fec_controlenvio).days)
			metricas.propension = json.dumps(vec_metricas)
		except:
			vec_metricas.append(proyecto.prudenciamin)
		encuestado.propension = sum(vec_metricas)/len(vec_metricas)
		metricas.propension = json.dumps(vec_metricas)
		with transaction.atomic():
			metricas.save()
			proyecto.save()
			encuestado.save()
			for i in cuestionario:
				i.fecharespuesta = timezone.now()
				if i.pregunta.abierta:
					i.respuesta = request.POST[str(i.pregunta.id)]
				elif i.pregunta.multiple:
					r = json.dumps(request.POST.getlist(str(i.pregunta.id)))
					if not r:
						respuesta = 'Ninguna seleccionada'
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
	'Encuestado':encuestado,'Preguntas':cuestionario_preguntas,'Proyecto':proyecto
	},	context_instance=RequestContext(request))


@cache_control(no_store=True)
def encuestaexterna(request,id_proyecto,key):
	try:
		tiempo = datetime.date.today()
		proyecto = Proyectos.objects.select_related('proyectosdatos').filter(id=id_proyecto).get(key=key)
		datos = ProyectosDatos.objects.filter(ffin__gte=tiempo,finicio__lte=tiempo).get(id=proyecto)
		if not proyecto.activo:
			return render_to_response('403.html')
		variables = Variables.objects.filter(proyecto = proyecto)
		preguntas = Preguntas.objects.prefetch_related('respuestas_set'
			).select_related('variable').filter(variable__in = variables,estado = True
			).order_by('variable__posicion')
		len_cuestionario = len(preguntas)
	except:
		return render_to_response('404.html')

	if not len_cuestionario:
		return render_to_response('403.html')

	if request.method == 'POST':
		proyecto.tot_respuestas += len_cuestionario
		if proyecto.tot_preguntas:
			proyecto.total = proyecto.tot_respuestas / proyecto.tot_preguntas
		else:
			proyecto.total = 0

		x = timezone.now()
		hoy = date(year=x.year,month=x.month,day=x.day)
		ayer = hoy - timedelta(1)
		try:
			metrica = MetricasExterna.objects.filter(proyecto=proyecto).get(fecha=hoy)
			metrica.encuestados += 1
			try:
				metricas_ayer = MetricasExterna.objects.filter(proyecto=proyecto).get(fecha=ayer)
				if metrica.acumulado:
					metrica.acumulado += 1
				else:
					metrica.acumulado = 1 + metricas_ayer.acumulado
			except:
				if metrica.acumulado:
					metrica.acumulado += 1
				else:
					metrica.acumulado = 1
		except:
			metrica = MetricasExterna(proyecto=proyecto,fecha=hoy,encuestados=1)
			try:
				metricas_ayer = MetricasExterna.objects.filter(proyecto=proyecto).get(fecha=ayer)
				metrica.acumulado = 1 + metricas_ayer.acumulado
			except:
				metrica.acumulado = 1

		colaborador = metrica.acumulado
		streaming = []
		for i in preguntas:
			if i.abierta:
				respuesta = request.POST[str(i.id)]
			elif i.multiple:
				respuesta = json.dumps(request.POST.getlist(str(i.id)))
				if not respuesta:
					respuesta = 'Ninguna seleccionada'
			else:
				respuesta = request.POST[str(i.id)]
			streaming.append(Externa(colaborador=colaborador,proyecto=proyecto,pregunta=i,
							fecharespuesta=timezone.now(),
							respuesta=respuesta))
		with transaction.atomic():
			metrica.save()
			proyecto.save()
			Externa.objects.bulk_create(streaming)

		return HttpResponseRedirect('/externa2/'+str(proyecto.id)+'/'+key)

	return render_to_response('encuesta.html',{
	'Proyecto':proyecto,'Preguntas':preguntas,
	},	context_instance=RequestContext(request))

@cache_control(no_store=True)
def encuestaexterna2(request,id_proyecto,key):
	link = '/externa/'+id_proyecto+'/'+key
	return render_to_response('externa2.html',{
	'Link':link
	},	context_instance=RequestContext(request))

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def exportarexterna(request):
	import xlwt
	date_format = xlwt.XFStyle()
	date_format.num_format_str = 'dd/mm/yyyy'
	proyecto = cache.get(request.user.username)
	if not proyecto:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.res_exp:
		response = HttpResponse(content_type='application/ms-excel')
		import string
		a = string.replace(proyecto.nombre,' ','')
		response['Content-Disposition'] = 'attachment; filename=%s.xls'%(a)
		wb = xlwt.Workbook(encoding='utf-8')
		ws = wb.add_sheet("GoAnalytics")
		datos = proyecto.proyectosdatos
		stream = Externa.objects.filter(proyecto=proyecto).select_related(
				'pregunta__variable').prefetch_related('pregunta__respuestas_set')
		lens = len(stream)
		k = 0
		ws.write(0,0,u"Participante #")
		ws.write(0,1,u"Variable")
		ws.write(0,2,u"Pregunta")
		ws.write(0,3,u"Numerico")
		ws.write(0,4,u"Respuesta")
		ws.write(0,5,u"Fecha de respuesta")
		for i in xrange(lens):
			k=0
			ws.write(i+1,0,stream[i].colaborador)
			ws.write(i+1,1,stream[i].pregunta.variable.nombre)
			ws.write(i+1,2,stream[i].pregunta.texto)
			if stream[i].pregunta.numerica and stream[i].pregunta.multiple:
				respuestas = json.loads(stream[i].respuesta)
				ans = []
				for respuesta in stream[i].pregunta.respuestas_set.all():
					if respuesta.texto in respuestas:
						ans.append(respuesta.numerico)
				if ans:
					ws.write(i+1,3,json.dumps(ans))
				else:
					ws.write(i+1,3,u"[]")
			elif stream[i].pregunta.numerica and not stream[i].pregunta.multiple:
				for respuesta in stream[i].pregunta.respuestas_set.all():
					if stream[i].respuesta == respuesta.texto:
						ws.write(i+1,3,respuesta.numerico)
			else:
				ws.write(i+1,3,"No aplica")
			if stream[i].respuesta:
				ws.write(i+1,4,stream[i].respuesta)
			else:
				ws.write(i+1,4,u"")
			ws.write(i+1,5,stream[i].fecharespuesta.isoformat())
		wb.save(response)
		return response
	else:
		render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def exportarinterna(request):
	import xlwt
	date_format = xlwt.XFStyle()
	date_format.num_format_str = 'dd/mm/yyyy'
	proyecto = cache.get(request.user.username)
	if not proyecto:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.res_exp:
		response = HttpResponse(content_type='application/ms-excel')
		import string
		a = string.replace(proyecto.nombre,' ','')
		response['Content-Disposition'] = 'attachment; filename=%s.xls'%(a)
		wb = xlwt.Workbook(encoding='utf-8')
		ws = wb.add_sheet("GoAnalytics")
		datos = proyecto.proyectosdatos
		stream = Streaming.objects.filter(proyecto=proyecto).select_related(
				'colaborador__colaboradoresdatos','proyecto__proyectosdatos',
				'pregunta__variable').prefetch_related('pregunta__respuestas_set')
		lens = len(stream)
		k = 0
		ws.write(0,0,u"Nombre")
		ws.write(0,1,u"Apellido")
		ws.write(0,2,u"Email")
		ws.write(0,3,u"Móvil")
		ws.write(0,4,u"Género")
		ws.write(0,5,u"Área")
		ws.write(0,6,u"Cargo")
		ws.write(0,7,u"Regional")
		ws.write(0,8,u"Ciudad")
		ws.write(0,9,u"Nivel académico")
		ws.write(0,10,u"Profesión")
		ws.write(0,11,u"Fecha de nacimiento",date_format)
		ws.write(0,12,u"Fecha de ingreso",date_format)
		if(datos.opcional1):
			ws.write(0,13,datos.opcional1)
		else:
			k +=1
		if(datos.opcional2):
			ws.write(0,14-k,datos.opcional2)
		else:
			k +=1
		if(datos.opcional3):
			ws.write(0,15-k,datos.opcional3)
		else:
			k +=1
		if(datos.opcional4):
			ws.write(0,16-k,datos.opcional4)
		else:
			k +=1
		if(datos.opcional5):
			ws.write(0,17-k,datos.opcional5)
		else:
			k +=1
		ws.write(0,18-k,u"Fecha de respuesta")
		ws.write(0,19-k,u"Variable")
		ws.write(0,20-k,u"Pregunta")
		ws.write(0,21-k,u"Respuesta numérica (si aplica)")
		ws.write(0,22-k,u"Respuesta(s)")
		for i in xrange(lens):
			k=0
			ws.write(i+1,0,stream[i].colaborador.nombre)
			ws.write(i+1,1,stream[i].colaborador.apellido)
			ws.write(i+1,2,stream[i].colaborador.email)
			ws.write(i+1,3,stream[i].colaborador.movil)
			ws.write(i+1,4,stream[i].colaborador.colaboradoresdatos.genero)
			ws.write(i+1,5,stream[i].colaborador.colaboradoresdatos.area)
			ws.write(i+1,6,stream[i].colaborador.colaboradoresdatos.cargo)
			ws.write(i+1,7,stream[i].colaborador.colaboradoresdatos.regional)
			ws.write(i+1,8,stream[i].colaborador.colaboradoresdatos.ciudad)
			ws.write(i+1,9,stream[i].colaborador.colaboradoresdatos.niv_academico)
			ws.write(i+1,10,stream[i].colaborador.colaboradoresdatos.profesion)
			if stream[i].colaborador.colaboradoresdatos.fec_nacimiento:
				ws.write(i+1,11,stream[i].colaborador.colaboradoresdatos.fec_nacimiento.isoformat())
			else:
				ws.write(i+1,11,u"No registra")
			ws.write(i+1,12,stream[i].colaborador.colaboradoresdatos.fec_ingreso.isoformat())
			if(datos.opcional1):
				ws.write(i+1,13,stream[i].colaborador.colaboradoresdatos.opcional1)
			else:
				k +=1
			if(datos.opcional2):
				ws.write(i+1,14-k,stream[i].colaborador.colaboradoresdatos.opcional2)
			else:
				k +=1
			if(datos.opcional3):
				ws.write(i+1,15-k,stream[i].colaborador.colaboradoresdatos.opcional3)
			else:
				k +=1
			if(datos.opcional4):
				ws.write(i+1,16-k,stream[i].colaborador.colaboradoresdatos.opcional4)
			else:
				k +=1
			if(datos.opcional5):
				ws.write(i+1,17-k,stream[i].colaborador.colaboradoresdatos.opcional5)
			else:
				k +=1
			ws.write(i+1,18-k,stream[i].fecharespuesta.isoformat())
			ws.write(i+1,19-k,stream[i].pregunta.variable.nombre)
			ws.write(i+1,20-k,stream[i].pregunta.texto)
			if stream[i].pregunta.numerica and stream[i].pregunta.multiple:
				respuestas = json.loads(stream[i].respuesta)
				ans = []
				for respuesta in stream[i].pregunta.respuestas_set.all():
					if respuesta.texto in respuestas:
						ans.append(respuesta.numerico)
				if ans:
					ws.write(i+1,21-k,json.dumps(ans))
				else:
					ws.write(i+1,21-k,u"[]")
			elif stream[i].pregunta.numerica and not stream[i].pregunta.multiple:
				for respuesta in stream[i].pregunta.respuestas_set.all():
					if stream[i].respuesta == respuesta.texto:
						ws.write(i+1,21-k,respuesta.numerico)
			else:
				ws.write(i+1,21-k,"No aplica")
			if stream[i].respuesta:
				ws.write(i+1,22-k,stream[i].respuesta)
			else:
				ws.write(i+1,22-k,u"")
		wb.save(response)
		return response
	else:
		render_to_response('403.html')
