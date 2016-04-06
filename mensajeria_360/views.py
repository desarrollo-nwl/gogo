# -*- encoding: utf-8 -*-
from colaboradores_360.models import Colaboradores_360, ColaboradoresMetricas_360,ColaboradoresDatos_360
from cuestionarios_360.models import Variables_360,Preguntas_360
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import transaction
from django.db.models import F
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_control
from mensajeria_360.models import *
from usuarios.models import *

from django.db.models import Avg
from datetime import datetime as DT
from datetime import timedelta,date
from django.utils import timezone
import random, ujson

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.utils
import smtplib

#===============================================================================
# Administrar el envio
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def gosurvey_360(request):
	proyecto = cache.get(request.user.username)
	proyecto = Proyectos.objects.get(id=proyecto.id)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"] :
		return render_to_response('423.html')
	permisos = request.user.permisos
	datos = proyecto.proyectosdatos
	if permisos.consultor:
		if request.method == 'POST':
			with transaction.atomic():
				if permisos.act_surveys:
					try:
						comprobar = request.POST['iniciable']
						if(permisos.max_proyectos - permisos.max_pro_usados >= 1):
							permisos.max_pro_usados += 1
							proyecto.iniciable = True
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
				# try:
				comprobar = request.POST['activo']
				streaming_crear =[]
				adicionales = 0

				if not request.is_ajax():
					if proyecto.activo :
						proyecto.activo = False
					else:
						proyecto.activo = True

					if not proyecto.activo:
						proyecto.save()
						datos.save()
						cache.set(request.user.username,proyecto,86400)

				if request.is_ajax():

					datos.finicio = DT.strptime(str(request.POST['fec_inicio']),'%d/%m/%Y')
					datos.ffin = DT.strptime(str(request.POST['fec_fin']),'%d/%m/%Y')

					if proyecto.tipo != "360 unico":
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
						proyecto.can_envio = request.POST['can_envio']

						if proyecto.ciclico:
							proyecto.ciclos = request.POST['ciclos']
					else:
						proyecto.prudenciamin = 1
						proyecto.prudenciamax = 2
						proyecto.ciclos = 1

					instrumento = Instrumentos_360.objects.only('id').filter( proyecto_id = proyecto.id ).first()

					if proyecto.tipo == "360 unico" and instrumento:
						red = Redes_360.objects.only('id','evaluado_id').filter(proyecto_id = proyecto.id)[0]
						colaboradores = Colaboradores_360.objects.only('id').filter( proyecto_id = proyecto.id )
						preguntas = Preguntas_360.objects.filter( proyecto_id = proyecto.id, instrumento_id=instrumento.id)

						for i in colaboradores:
							for j in preguntas:
								if not Streaming_360.objects.filter(proyecto_id=proyecto.id,
									colaborador_id = i.id,
									evaluado_id = red.evaluado_id,
									pregunta_id=j.id).exists():
									streaming_crear.append(Streaming_360(
														proyecto_id=proyecto.id,
														instrumento_id=instrumento.id,
														colaborador_id=i.id,
														evaluado_id = red.evaluado_id,
														red_id = red.id,
														rol = "evaluador",
														pregunta_id=j.id))



							aresponder = Streaming_360.objects.filter(proyecto_id=proyecto.id,colaborador_id=i.id).count()
							print aresponder
							if aresponder:
								respuestas = Streaming_360.objects.filter(proyecto_id=proyecto.id,colaborador_id=i.id,respuesta__isnull=False).count()
								Colaboradores_360.objects.filter( id = i.id ).update(
									pre_respuestas = 0,
									pre_aresponder = aresponder,
									tot_avance= 100*respuestas/aresponder,
								)
							else:
								Colaboradores_360.objects.filter( id = i.id ).update(
									pre_respuestas = 0,
									pre_aresponder = 0,
									tot_avance= 0,
								)

					elif proyecto.tipo == "360 redes":
						redes = Redes_360.objects.filter(proyecto_id = proyecto.id)

						for red in redes:
							local = False
							preguntas = Preguntas_360.objects.filter( proyecto_id = proyecto.id, instrumento_id=red.instrumento_id)
							for j in preguntas:
								if not Streaming_360.objects.filter(proyecto_id=proyecto.id,
									colaborador_id=red.colaborador_id,
									evaluado_id = red.evaluado_id,
									pregunta_id=j.id).exists():
									streaming_crear.append(Streaming_360(
														proyecto_id=proyecto.id,
														instrumento_id=red.instrumento_id,
														colaborador_id=red.colaborador_id,
														evaluado_id = red.evaluado_id,
														red_id = red.id,
														rol = red.rol,
														pregunta_id=j.id))
									local = True
									adicionales += 1


							aresponder = Streaming_360.objects.filter(proyecto_id=proyecto.id,colaborador_id=red.colaborador_id).count()
							if aresponder:
								respuestas = Streaming_360.objects.filter(proyecto_id=proyecto.id,colaborador_id=red.colaborador_id,respuesta__isnull=False).count()
								Colaboradores_360.objects.filter(id = red.colaborador_id
								).update(
									pre_respuestas = respuestas,
									pre_aresponder = aresponder,
									tot_avance= 100*respuestas/aresponder,
								)
								print aresponder
							else:
								Colaboradores_360.objects.filter(id = red.colaborador_id
								).update(
									pre_respuestas = 0,
									pre_aresponder = 0,
									tot_avance= 0,
								)


					gran_total = Streaming_360.objects.filter(proyecto_id = proyecto.id).count()
					if gran_total:
						contestadas = Streaming_360.objects.filter(proyecto_id = proyecto.id,respuesta__isnull = False).count()
						proyecto.tot_respuestas = contestadas
						proyecto.tot_aresponder = gran_total
						proyecto.total = 100.0*contestadas/gran_total
					else:
						proyecto.tot_respuestas = 0
						proyecto.tot_aresponder = 0
						proyecto.total = 0


					if adicionales:
						Streaming_360.objects.bulk_create(streaming_crear)
						proyecto.tot_aresponder += adicionales
					proyecto.save()
					datos.save()
					cache.set(request.user.username,proyecto,86400)


				return HttpResponse(ujson.dumps({'estado':1}),content_type="aplication/json")

			# except:
			# 	pass

		return render_to_response('gosurvey_360.html',{
		'Activar':'Contenido','activar':'IniciarDetener','Proyecto':proyecto,'Permisos':permisos
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def metricas_360(request):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"] :
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and proyecto.interna:

		participantes = Colaboradores_360.objects.only('puntaje','respuestas','enviados','propension',
						'reenviados','nombre','apellido','colaboradoresdatos_360__area','estado','descripcion'
						).filter(proyecto = proyecto, estado = True
						).select_related('colaboradoresdatos_360')

		average = Colaboradores_360.objects.filter(proyecto=proyecto).exclude(propension__lte=0,).aggregate(Avg('propension'))

		return render_to_response('metricas_360.html',{
		'Activar':'EstadoAvance','activar':'EnviosRespuestas','Proyecto':proyecto,'Permisos':permisos,
		'Participantes':participantes,'Average':average
		},	context_instance=RequestContext(request))

	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def colaboradoreenviar(request,id_colaborador):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"] :
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
						import unicodedata
						server=smtplib.SMTP('smtp.mandrillapp.com',587)
						# server=smtplib.SMTP('email-smtp.us-east-1.amazonaws.com',587)
						server.ehlo()
						server.starttls()
						server.login('Team@goanalytics.com','pR6yG1ztNHT7xW6Y8yigfw')
						# server.login('AKIAIIG3SGXTWBK23VEQ','AtDj4P2QhDWTSIpkVv9ySRsz50KUFnusZ1cjFt+ZsdHC')
						nom_log =request.user.first_name+' '+request.user.last_name
						Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,accion="Forzó reenvío a",descripcion=colaborador.nombre+" "+colaborador.apellido)
						destinatario = [colaborador.email]
						msg=MIMEMultipart()
						msg["subject"]=  datos.asunto
						msg['From'] = email.utils.formataddr(('GoAnalytics', 'Team@goanalytics.com'))
						# msg['From'] = email.utils.formataddr(('GoAnalytics', 'team@bigtalenter.com'))
						urlimg = 'http://www.changelabtools.com'+datos.logo.url
						if colaborador.colaboradoresdatos.genero.lower() == "femenino":
							genero = "a"
						else:
							genero = "o"
						nombre = (colaborador.nombre).encode("ascii", "xmlcharrefreplace")
						titulo = (datos.tit_encuesta).encode("ascii", "xmlcharrefreplace")
						texto_correo = salvar_html((datos.cue_correo).encode("ascii", "xmlcharrefreplace"))
						url = 'http://www.changelabtools.com/encuesta/'+str(proyecto.id)+'/'+colaborador.key
						html = correo_standar(urlimg,genero,nombre,titulo,texto_correo,url)
						mensaje = MIMEText(html,"html")
						msg.attach(mensaje)
						with transaction.atomic():
							colaborador.reenviados = colaborador.reenviados + 1
							Streaming.objects.filter(colaborador=colaborador).update(fec_controlenvio=timezone.now())
							colaborador.save()
							server.sendmail('Team@goanalytics.com',destinatario,msg.as_string())
							# server.sendmail('team@bigtalenter.com',destinatario,msg.as_string())
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
		stream = Streaming.objects.prefetch_related(
						'pregunta__respuestas_set'
					).select_related(
						'pregunta__variable'
					).filter(
						colaborador_id = encuestado.id,
						pregunta__estado = True,
						respuesta__isnull = True
					).order_by(
						'pregunta__variable__posicion'
					)
		proyecto = encuestado.proyecto
		tiempo = DT.date.today()
		datos = ProyectosDatos.objects.filter(ffin__gte=tiempo,finicio__lte=tiempo).get(id=proyecto)
		total_cuestionario = len(stream)
	except:
		try:
			return render_to_response('fake.html',{
			'Pagina':'http://'+str(encuestado.proyecto.empresa.pagina)
			},	context_instance=RequestContext(request))
		except:
			return render_to_response('fake.html',{
			'Pagina':'http://www.changeamericas.com'
			},	context_instance=RequestContext(request))


	if request.method == 'POST':
		ids_streamig = request.POST.getlist('ids_streaming')
		cuestionario = Streaming.objects.filter(proyecto_id=proyecto.id, id__in=ids_streamig)
		len_cuestionario = len(ids_streamig)
		proyecto.tot_respuestas += len_cuestionario
		chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
		key = ''.join(random.sample(chars, 64))
		encuestado.key = key
		encuestado.respuestas += 1
		proyecto.total = 100*(1.0*proyecto.tot_respuestas/proyecto.tot_aresponder)
		metricas = encuestado.colaboradoresmetricas
		vec_metricas = ujson.loads(metricas.propension)
		try:
			vec_metricas.append((timezone.now()-stream[0].fec_controlenvio).seconds/3600.0)
			metricas.propension = ujson.dumps(vec_metricas)
		except:
			vec_metricas.append(proyecto.prudenciamin)
		encuestado.propension = sum(vec_metricas)/len(vec_metricas)
		metricas.propension = ujson.dumps(vec_metricas)
		with transaction.atomic():
			metricas.save()
			proyecto.save()
			encuestado.save()
			for i in cuestionario:
				i.fecharespuesta = timezone.now()
				if i.pregunta.abierta:
					i.respuesta = request.POST[str(i.pregunta.id)]
				elif i.pregunta.multiple:
					r = ujson.dumps(request.POST.getlist(str(i.pregunta.id)))
					if not r:
						i.respuesta = 'Ninguna seleccionada'
					else:
						i.respuesta = r
				else:
					i.respuesta = request.POST[str(i.pregunta.id)]
				i.save()
			Streaming.objects.filter(colaborador = encuestado).update(fec_controlenvio=timezone.now())
		try:
			return render_to_response('fake.html',{
			'Pagina':'http://'+str(encuestado.proyecto.empresa.pagina)
			},	context_instance=RequestContext(request))
		except:
			return render_to_response('fake.html',{
			'Pagina':'http://www.changeamericas.com'
			},	context_instance=RequestContext(request))

	cuestionario =[]

	# si hay preguntas sin responder en un proyecto activo y NO es aleatorio
	if stream and encuestado.proyecto.activo and proyecto.pordenadas:
		if (proyecto.tipo != 'Completa'):
			len_cuestionario = 0
			cuestionario_preguntas =[]
			while( len_cuestionario < encuestado.proyecto.can_envio and len_cuestionario < total_cuestionario ):
				cuestionario.append(stream[len_cuestionario])
				cuestionario_preguntas.append(stream[len_cuestionario].pregunta)
				len_cuestionario += 1

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

	# si hay preguntas sin responder en un proyecto activo y es aleatorio
	elif stream and encuestado.proyecto.activo and (not proyecto.pordenadas):
		stream_vect = range(total_cuestionario)
		if (proyecto.tipo != 'Completa'):
			len_cuestionario = 0
			cuestionario_preguntas =[]
			random.shuffle(stream_vect)

			while( len_cuestionario < encuestado.proyecto.can_envio and len_cuestionario < total_cuestionario ):
				cuestionario.append(stream[stream_vect[len_cuestionario]])
				len_cuestionario += 1
			cuestionario_preguntas = cuestionario
			if not len_cuestionario:
				try:
					return HttpResponseRedirect('http://'+str(encuestado.poyecto.empresa.pagina))
				except:
					return HttpResponseRedirect('http://www.networkslab.co')
		else:
			cuestionario = stream
			len_cuestionario = len(stream)
			cuestionario_preguntas =[]
			cuestionario_preguntas = stream

	else:
		try:
			return HttpResponseRedirect('http://'+str(encuestado.poyecto.empresa.pagina))
		except:
			return HttpResponseRedirect('http://networkslab.co')

	return render_to_response('encuesta.html',{
	'Encuestado':encuestado,'Preguntas_encuesta':cuestionario_preguntas,'Proyecto':proyecto,'Cuestionario':cuestionario
	},	context_instance=RequestContext(request))


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def detalladas_360(request):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"] :
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.res_exp:
		return render_to_response('detalladas_360.html',{
		'Activar':'EstadoAvance','activar':'RespuestasDetalladas',
		'Proyecto':proyecto,'Permisos':permisos,
		},	context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def exportarinterna_360(request):
	import xlwt
	tit_format = xlwt.easyxf('font:bold on ;align:wrap on, vert centre, horz center;')
	str_format = xlwt.easyxf(num_format_str="@")
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"] :
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
		stream = Streaming.objects.filter(proyecto=proyecto,respuesta__isnull=False).select_related(
				'colaborador__colaboradoresdatos','proyecto__proyectosdatos',
				'pregunta__variable').prefetch_related('pregunta__respuestas_set')
		lens = len(stream)
		k = 0
		ws.write(0,0,u"Nombre",tit_format)
		ws.write(0,1,u"Apellido",tit_format)
		ws.write(0,2,u"Email",tit_format)
		ws.write(0,3,u"Móvil",tit_format)
		ws.write(0,4,u"Género",tit_format)
		ws.write(0,5,u"Área",tit_format)
		ws.write(0,6,u"Cargo",tit_format)
		ws.write(0,7,u"Regional",tit_format)
		ws.write(0,8,u"Ciudad",tit_format)
		ws.write(0,9,u"Nivel académico",tit_format)
		ws.write(0,10,u"Profesión",tit_format)
		ws.write(0,11,u"Fecha de nacimiento",tit_format)
		ws.write(0,12,u"Fecha de ingreso",tit_format)
		if(datos.opcional1):
			ws.write(0,13,datos.opcional1,tit_format)
		else:
			k +=1
		if(datos.opcional2):
			ws.write(0,14-k,datos.opcional2,tit_format)
		else:
			k +=1
		if(datos.opcional3):
			ws.write(0,15-k,datos.opcional3,tit_format)
		else:
			k +=1
		if(datos.opcional4):
			ws.write(0,16-k,datos.opcional4,tit_format)
		else:
			k +=1
		if(datos.opcional5):
			ws.write(0,17-k,datos.opcional5,tit_format)
		else:
			k +=1
		ws.write(0,18-k,u"Fecha de respuesta",tit_format)
		ws.write(0,19-k,u"Variable",tit_format)
		ws.write(0,20-k,u"Pregunta",tit_format)
		ws.write(0,21-k,u"Respuesta numérica",tit_format)
		ws.write(0,22-k,u"Respuesta(s)",tit_format)
		for i in xrange(lens):
			k=0
			ws.write(i+1,0,stream[i].colaborador.nombre,str_format)
			ws.write(i+1,1,stream[i].colaborador.apellido,str_format)
			ws.write(i+1,2,stream[i].colaborador.email,str_format)
			ws.write(i+1,3,stream[i].colaborador.movil,str_format)
			ws.write(i+1,4,stream[i].colaborador.colaboradoresdatos.genero,str_format)
			ws.write(i+1,5,stream[i].colaborador.colaboradoresdatos.area,str_format)
			ws.write(i+1,6,stream[i].colaborador.colaboradoresdatos.cargo,str_format)
			ws.write(i+1,7,stream[i].colaborador.colaboradoresdatos.regional,str_format)
			ws.write(i+1,8,stream[i].colaborador.colaboradoresdatos.ciudad,str_format)
			ws.write(i+1,9,stream[i].colaborador.colaboradoresdatos.niv_academico,str_format)
			ws.write(i+1,10,stream[i].colaborador.colaboradoresdatos.profesion,str_format)
			if stream[i].colaborador.colaboradoresdatos.fec_nacimiento:
				ws.write(i+1,11,u'{0}/{1}/{2}'.format(
					stream[i].colaborador.colaboradoresdatos.fec_nacimiento.day,
					stream[i].colaborador.colaboradoresdatos.fec_nacimiento.month,
					stream[i].colaborador.colaboradoresdatos.fec_nacimiento.year),str_format)
			else:
				ws.write(i+1,11,u"No registra",str_format)
			if stream[i].colaborador.colaboradoresdatos.fec_nacimiento:
				ws.write(i+1,12,u'{0}/{1}/{2}'.format(
					stream[i].colaborador.colaboradoresdatos.fec_ingreso.day,
					stream[i].colaborador.colaboradoresdatos.fec_ingreso.month,
					stream[i].colaborador.colaboradoresdatos.fec_ingreso.year),str_format)
			else:
				ws.write(i+1,12,u"No registra",str_format)
			if(datos.opcional1):
				ws.write(i+1,13,stream[i].colaborador.colaboradoresdatos.opcional1,str_format)
			else:
				k +=1
			if(datos.opcional2):
				ws.write(i+1,14-k,stream[i].colaborador.colaboradoresdatos.opcional2,str_format)
			else:
				k +=1
			if(datos.opcional3):
				ws.write(i+1,15-k,stream[i].colaborador.colaboradoresdatos.opcional3,str_format)
			else:
				k +=1
			if(datos.opcional4):
				ws.write(i+1,16-k,stream[i].colaborador.colaboradoresdatos.opcional4,str_format)
			else:
				k +=1
			if(datos.opcional5):
				ws.write(i+1,17-k,stream[i].colaborador.colaboradoresdatos.opcional5,str_format)
			else:
				k +=1
			ws.write(i+1,18-k,u'{0}/{1}/{2}'.format(
				stream[i].fecharespuesta.day,
				stream[i].fecharespuesta.month,
				stream[i].fecharespuesta.year),str_format)
			ws.write(i+1,19-k,stream[i].pregunta.variable.nombre,str_format)
			ws.write(i+1,20-k,stream[i].pregunta.texto,str_format)

			if not proyecto.ciclico:
				if stream[i].pregunta.numerica and stream[i].pregunta.multiple:
					respuestas = ujson.loads(stream[i].respuesta)
					ans = []
					for respuesta in stream[i].pregunta.respuestas_set.all():
						if respuesta.texto in respuestas:
							ans.append(respuesta.numerico)
					if ans:
						ws.write(i+1,21-k,u';'.join(str(x) for x in ans),str_format)
						ws.write(i+1,22-k,u';'.join(ujson.loads(stream[i].respuesta)),str_format)
					else:
						ws.write(i+1,21-k,u'',str_format)

				elif stream[i].pregunta.numerica and not stream[i].pregunta.multiple:
					for respuesta in stream[i].pregunta.respuestas_set.all():
						if stream[i].respuesta == respuesta.texto:
							ws.write(i+1,21-k,respuesta.numerico,str_format)
							ws.write(i+1,22-k,stream[i].respuesta,str_format)

				elif stream[i].pregunta.multiple and not stream[i].pregunta.numerica:
					ws.write(i+1,21-k,u'',str_format)
					ws.write(i+1,22-k,u';'.join(ujson.loads(stream[i].respuesta)),str_format)

				else:
					ws.write(i+1,21-k,u'',str_format)
					ws.write(i+1,22-k,stream[i].respuesta,str_format)
			else:
				ws.write(i+1,22-k,stream[i].respuesta,str_format)

		wb.save(response)
		return response
	else:
		render_to_response('403.html')

# ==============================================================================
# 	Importacion de respuestas
# ==============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def importarespuestas_exportar_360(request):
	import xlwt
	date_format = xlwt.XFStyle()
	date_format.num_format_str = 'dd/mm/yyyy'
	str_format = xlwt.easyxf(num_format_str="@")
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"] :
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.res_exp:
		response = HttpResponse(content_type='application/ms-excel')
		import string
		a = string.replace(proyecto.nombre,' ','')
		response['Content-Disposition'] = 'attachment; filename=%s.xls'%(a)
		wb = xlwt.Workbook(encoding='utf-8')
		ws = wb.add_sheet(a)
		datos = proyecto.proyectosdatos
		colaboradores = Colaboradores.objects.filter(proyecto_id=proyecto.id).select_related(
				'colaboradoresdatos','proyecto__proyectosdatos')
		lenc = len(colaboradores)
		k = 0
		ws.write(0,0,u"Id usuario")
		ws.write(0,1,u"Nombre")
		ws.write(0,2,u"Apellido")
		ws.write(0,3,u"Email")
		ws.write(0,4,u"Id pregunta")
		ws.write(0,5,u"Texto de la pregunta")
		ws.write(0,6,u"Respuesta")
		ws.write(0,7,u"Móvil")
		ws.write(0,8,u"Género")
		ws.write(0,9,u"Área")
		ws.write(0,10,u"Cargo")
		ws.write(0,11,u"Regional")
		ws.write(0,12,u"Ciudad")
		ws.write(0,13,u"Nivel académico")
		ws.write(0,14,u"Profesión")
		ws.write(0,15,u"Fecha de nacimiento",date_format)
		ws.write(0,16,u"Fecha de ingreso",date_format)
		if(datos.opcional1):
			ws.write(0,17,datos.opcional1)
		else:
			k +=1
		if(datos.opcional2):
			ws.write(0,18-k,datos.opcional2)
		else:
			k +=1
		if(datos.opcional3):
			ws.write(0,19-k,datos.opcional3)
		else:
			k +=1
		if(datos.opcional4):
			ws.write(0,20-k,datos.opcional4)
		else:
			k +=1
		if(datos.opcional5):
			ws.write(0,21-k,datos.opcional5)
		else:
			k +=1

		for i in xrange(lenc):
			k=0
			ws.write(i+1,0,colaboradores[i].id)
			ws.write(i+1,1,colaboradores[i].nombre)
			ws.write(i+1,2,colaboradores[i].apellido)
			ws.write(i+1,3,colaboradores[i].email)
			# ws.write(i+1,4, )
			# ws.write(i+1,5, )
			# ws.write(i+1,6, )
			ws.write(i+1,7,colaboradores[i].movil)
			ws.write(i+1,8,colaboradores[i].colaboradoresdatos.genero)
			ws.write(i+1,9,colaboradores[i].colaboradoresdatos.area)
			ws.write(i+1,10,colaboradores[i].colaboradoresdatos.cargo)
			ws.write(i+1,11,colaboradores[i].colaboradoresdatos.regional)
			ws.write(i+1,12,colaboradores[i].colaboradoresdatos.ciudad)
			ws.write(i+1,13,colaboradores[i].colaboradoresdatos.niv_academico)
			ws.write(i+1,14,colaboradores[i].colaboradoresdatos.profesion)
			if colaboradores[i].colaboradoresdatos.fec_nacimiento:
				ws.write(i+1,15,u'{0}/{1}/{2}'.format(colaboradores[i].colaboradoresdatos.fec_ingreso.day,
					colaboradores[i].colaboradoresdatos.fec_ingreso.month,
					colaboradores[i].colaboradoresdatos.fec_ingreso.year),str_format)

			ws.write(i+1,16,u'{0}/{1}/{2}'.format(colaboradores[i].colaboradoresdatos.fec_ingreso.day,
				colaboradores[i].colaboradoresdatos.fec_ingreso.month,
				colaboradores[i].colaboradoresdatos.fec_ingreso.year),str_format)
			if(datos.opcional1):
				ws.write(i+1,17,colaboradores[i].colaboradoresdatos.opcional1)
			else:
				k +=1
			if(datos.opcional2):
				ws.write(i+1,18-k,colaboradores[i].colaboradoresdatos.opcional2)
			else:
				k +=1
			if(datos.opcional3):
				ws.write(i+1,19-k,colaboradores[i].colaboradoresdatos.opcional3)
			else:
				k +=1
			if(datos.opcional4):
				ws.write(i+1,20-k,colaboradores[i].colaboradoresdatos.opcional4)
			else:
				k +=1
			if(datos.opcional5):
				ws.write(i+1,21-k,colaboradores[i].colaboradoresdatos.opcional5)
			else:
				k +=1

		wb.save(response)
		return response
	else:
		render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def importarespuestas_preguntas_360(request):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"] :
		return render_to_response('423.html')
	if not proyecto.interna:
		return render_to_response('404.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_add:
		error = None
		if request.method == 'POST':
			import xlrd,xlwt
			date_format = xlwt.XFStyle()
			date_format.num_format_str = 'dd/mm/yyyy'
			input_excel = request.FILES['docfile']
			doc = xlrd.open_workbook(file_contents=input_excel.read())
			sheet = doc.sheet_by_index(0)
			filas = sheet.nrows
			var_error = None
			try:
				streaming_crear = []
				proyecto_datos = proyecto.proyectosdatos
				with transaction.atomic():
					for i in xrange(1,filas):
						var_error = sheet.cell_value(i,1)+' '+sheet.cell_value(i,2)
						colaborador = Colaboradores.objects.get(id=sheet.cell_value(i,0))
						colaborador.nombre = sheet.cell_value(i,1)
						colaborador.apellido = sheet.cell_value(i,2)
						colaborador.email = sheet.cell_value(i,3)
						if sheet.cell_value(i,4):
							var_error = ''.join([var_error, ". Verifique que la pregunta {0} ya fue creada en la herramienta.".format(sheet.cell_value(i,4)) ])
							pregunta = Preguntas.objects.get(id=sheet.cell_value(i,4))

						if sheet.cell_value(i,7):
							colaborador.movil=sheet.cell_value(i,7)
						else:
							colaborador.movil = None
						colaborador.save()

						datos = ColaboradoresDatos.objects.get(id = colaborador)
						datos.genero=sheet.cell_value(i,8)
						datos.area=sheet.cell_value(i,9)
						datos.cargo=sheet.cell_value(i,10)
						datos.regional=sheet.cell_value(i,11)
						datos.ciudad=sheet.cell_value(i,12)
						datos.niv_academico=sheet.cell_value(i,13)
						datos.profesion=sheet.cell_value(i,14)
						datos.fec_ingreso = DT.strptime(sheet.cell_value(i,16), '%d/%m/%Y')

						if sheet.cell_value(i,15):
							datos.fec_nacimiento = DT.strptime(sheet.cell_value(i,15), '%d/%m/%Y')
						else:
							datos.fec_nacimiento = None
						if proyecto_datos.opcional1:
							datos.opcional1 = sheet.cell_value(i,17)
						if proyecto_datos.opcional2:
							datos.opcional2 = sheet.cell_value(i,18)
						if proyecto_datos.opcional3:
							datos.opcional3 = sheet.cell_value(i,19)
						if proyecto_datos.opcional4:
							datos.opcional4 = sheet.cell_value(i,20)
						if proyecto_datos.opcional5:
							datos.opcional5 = sheet.cell_value(i,21)
						datos.save()

						if sheet.cell_value(i,4) and not Streaming.objects.filter(proyecto_id=proyecto.id,colaborador_id=colaborador.id,pregunta_id=sheet.cell_value(i,4)).exists():
							if not pregunta.multiple:
								streaming_crear.append(Streaming(
									proyecto_id=proyecto.id,
									colaborador_id=colaborador.id,
									pregunta_id=sheet.cell_value(i,4),
									fecharespuesta=timezone.now(),
									respuesta=sheet.cell_value(i,6),
									))
								proyecto.tot_aresponder += 1
								proyecto.tot_respuestas += 1
							else:
								r = ujson.dumps(sheet.cell_value(i,6).split(';'))
								if r == '[""]':
									r = '[]'
								streaming_crear.append(Streaming(
									proyecto_id=proyecto.id,
									colaborador_id=colaborador.id,
									pregunta_id=sheet.cell_value(i,4),
									fecharespuesta=timezone.now(),
									respuesta=r,
									))
								proyecto.tot_aresponder += 1
								proyecto.tot_respuestas += 1

						elif sheet.cell_value(i,4) and Streaming.objects.filter(proyecto_id=proyecto.id,colaborador_id=colaborador.id,pregunta_id=sheet.cell_value(i,4)).exists():
							if not pregunta.multiple:
								s = Streaming.objects.filter(
									proyecto_id=proyecto.id,
									colaborador_id=colaborador.id,
									pregunta_id=sheet.cell_value(i,4))
								if not s[0].respuesta:
									proyecto.tot_respuestas += 1
								s.update(
									fecharespuesta=timezone.now(),
									respuesta=sheet.cell_value(i,6),
									)

							else:
								r = ujson.dumps(sheet.cell_value(i,6).split(';'))
								if r == '[""]':
									r = '[]'
								s = Streaming.objects.filter(
									proyecto_id=proyecto.id,
									colaborador_id=colaborador.id,
									pregunta_id=sheet.cell_value(i,4))
								if not s[0].respuesta:
									proyecto.tot_respuestas += 1
								s.update(
									fecharespuesta=timezone.now(),
									respuesta=r,
									)

						elif not sheet.cell_value(i,4):
							error = "Cambios realizados con éxito."
						else:
							error = "Verifique que la pregunta {0} ya fue creada en la herramienta.".format(sheet.cell_value(i,4))

					if(streaming_crear):
						Streaming.objects.bulk_create(streaming_crear)
					nom_log = request.user.first_name+' '+request.user.last_name
					Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,accion='Usó el archivo para importar respuestas',descripcion=proyecto.nombre)
					proyecto.save()
					cache.set(request.user.username,proyecto,86400)
				if(permisos.col_see):
					return HttpResponseRedirect('/respuestas/detalladas/')
				else:
					error = "Todos los datos se han subido con éxito"
			except:
				error= ''.join(["Ocurrio un error cuando se procesaba al participante ",var_error])

		return render_to_response('importarespuestas_360.html',{
		'Activar':'EstadoAvance','activar':'ImportarRespuestas',
		'Proyecto':proyecto,'Permisos':permisos,'Error':error
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')
