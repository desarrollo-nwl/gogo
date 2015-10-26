# -*- encoding: utf-8 -*-
from colaboradores.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import transaction
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.views.decorators.cache import cache_control
from usuarios.models import Proyectos, Logs
from datetime import datetime as DT
from cuestionarios.models import  Preguntas, Variables
from colaboradores.models import Colaboradores
from mensajeria.models import Streaming
import random
#===============================================================================
# indices
#===============================================================================


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def colaboradores_ind(request):
	proyecto = cache.get(request.user.username)
	if not proyecto:
		return render_to_response('423.html')
	if not proyecto.interna:
		return render_to_response('404.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.col_see:
		participantes = Colaboradores.objects.filter(proyecto=proyecto
						).only('nombre','apellido','email','colaboradoresdatos__cargo'
						).select_related('colaboradoresdatos')
		return render_to_response('colaboradores_ind.html',{
		'Activar':'Configuracion','activar':'Participantes','activarp':'Individual',
		'Proyecto':proyecto,'Permisos':permisos,'Participantes':participantes
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')

#===============================================================================
# nuevo
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def colaboradornuevo(request):
	proyecto = cache.get(request.user.username)
	if not proyecto:
		return render_to_response('423.html')
	if not proyecto.interna:
		return render_to_response('404.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.col_add:
		emails = Colaboradores.objects.only('email').filter(proyecto=proyecto)
		if request.method == 'POST':
			chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
			key = ''.join(random.sample(chars, 64))
			if not Colaboradores.objects.filter(proyecto=proyecto,email=request.POST['email']).exists():
				participante = Colaboradores(
					nombre = request.POST['nombre'],
					apellido = request.POST['apellido'],
					key = key,
					email = request.POST['email'],
					proyecto = proyecto)
				try:
					if(request.POST['estado']):
						participante.estado = True
				except:
					participante.estado = False
				try:participante.movil = request.POST['movil']
				except:pass
				with transaction.atomic():
					participante.save()
					datos = ColaboradoresDatos(
						id = participante,
						area = request.POST['area'],
						cargo = request.POST['cargo'],
						ciudad = request.POST['ciudad'],
						fec_ingreso = DT.strptime(str(request.POST['fec_ingreso']),'%d/%m/%Y'),
						genero = request.POST['genero'],
						niv_academico = request.POST['niv_academico'],
						profesion = request.POST['profesion'],
						regional = request.POST['regional'])
					try:
						if(request.POST['fec_nacimiento']):
							datos.fec_nacimiento = DT.strptime(str(request.POST['fec_nacimiento']),'%d/%m/%Y')
					except:
						datos.fec_nacimiento = None
					proyecto_datos = proyecto.proyectosdatos
					if proyecto_datos.opcional1:
						datos.opcional1 = request.POST['opcional1']
					if proyecto_datos.opcional2:
						datos.opcional2 = request.POST['opcional2']
					if proyecto_datos.opcional3:
						datos.opcional3 = request.POST['opcional3']
					if proyecto_datos.opcional4:
						datos.opcional4 = request.POST['opcional4']
					if proyecto_datos.opcional5:
						datos.opcional5 = request.POST['opcional5']
					proyecto.tot_participantes += 1
					streaming_crear = []
					datos.save()
					ColaboradoresMetricas.objects.create(id=participante)
					variables = proyecto.variables_set.all()
					preguntas = Preguntas.objects.filter(variable__in=variables)
					for j in preguntas:
						try:
							streaming_crear.append(Streaming(proyecto=proyecto,colaborador=participante,pregunta=j))
							proyecto.tot_aresponder += 1
						except:
							pass
					if(streaming_crear):
						Streaming.objects.bulk_create(streaming_crear)
					proyecto.save()
					nom_log = request.user.first_name+' '+request.user.last_name
					Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,
					accion="Creó al participante",descripcion=participante.nombre+' '+participante.apellido)
					cache.set(request.user.username,proyecto,86400)
				return HttpResponseRedirect('/participantes/individual')

		return render_to_response('colaboradornuevo.html',{
		'Activar':'Configuracion','activar':'Participantes','activarp':'Individual',
		'Proyecto':proyecto,'Permisos':permisos,'Emails':emails
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


#===============================================================================
# editar
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def colaboradoreditar(request,id_colaborador):
	proyecto = cache.get(request.user.username)
	if not proyecto:
		return render_to_response('423.html')
	if not proyecto.interna:
		return render_to_response('404.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.col_edit:
		try:participante = Colaboradores.objects.filter(proyecto=proyecto
							).select_related('colaboradoresdatos').get(id=int(id_colaborador))
		except:return render_to_response('403.html')
		emails = Colaboradores.objects.only('email').filter(proyecto=proyecto).exclude(id=id_colaborador)
		if request.method == 'POST':
			if not Colaboradores.objects.exclude(id=id_colaborador).filter(proyecto=proyecto,email=request.POST['email']).exists():
				participante.nombre = request.POST['nombre']
				participante.apellido = request.POST['apellido']
				participante.email = request.POST['email']
				participante.movil = request.POST['movil']
				try:
					if(request.POST['estado']):
						participante.estado = True
				except:
					participante.estado = False
				datos = participante.colaboradoresdatos
				datos.area = request.POST['area']
				datos.cargo = request.POST['cargo']
				datos.ciudad = request.POST['ciudad']
				datos.fec_ingreso = DT.strptime(str(request.POST['fec_ingreso']),'%d/%m/%Y')
				try:
					if(request.POST['fec_nacimiento']):
						datos.fec_nacimiento = DT.strptime(str(request.POST['fec_nacimiento']),'%d/%m/%Y')
				except:
					datos.fec_nacimiento = None
				datos.genero = request.POST['genero']
				datos.niv_academico = request.POST['niv_academico']
				datos.profesion = request.POST['profesion']
				datos.regional = request.POST['regional']
				proyecto_datos = proyecto.proyectosdatos
				if proyecto_datos.opcional1:
					datos.opcional1 = request.POST['opcional1']
				if proyecto_datos.opcional2:
					datos.opcional2 = request.POST['opcional2']
				if proyecto_datos.opcional3:
					datos.opcional3 = request.POST['opcional3']
				if proyecto_datos.opcional4:
					datos.opcional4 = request.POST['opcional4']
				if proyecto_datos.opcional5:
					datos.opcional5 = request.POST['opcional5']
				with transaction.atomic():
					participante.save()
					datos.save()
					nom_log = request.user.first_name+' '+request.user.last_name
					Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,
					accion="Editó al participante",descripcion=participante.nombre+' '+participante.apellido)
				return HttpResponseRedirect('/participantes/individual')
		return render_to_response('colaboradoreditar.html',{
		'Activar':'Configuracion','activar':'Participantes','activarp':'Individual',
		'Proyecto':proyecto,'Permisos':permisos,'Participante':participante,'Emails':emails,
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')

#===============================================================================
# activar/desactivar
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def colaboradoractivar(request,id_colaborador):
	proyecto = cache.get(request.user.username)
	if not proyecto:
		return render_to_response('423.html')
	if not proyecto.interna:
		return render_to_response('404.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.col_edit:
		try:participante = Colaboradores.objects.only('estado').filter(proyecto=proyecto).get(id=int(id_colaborador))
		except:return render_to_response('403.html')
		if(participante.estado):
			participante.estado = False
		else:
			participante.estado = True
		participante.save()
		return HttpResponseRedirect('/participantes/individual/')
	else:
		return render_to_response('403.html')

#===============================================================================
# nuevo archivo
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def archivo(request):
	import xlwt
	date_format = xlwt.XFStyle()
	date_format.num_format_str = 'dd/mm/yyyy'
	proyecto = cache.get(request.user.username)
	if not proyecto:
		return render_to_response('423.html')
	if not proyecto.interna:
		return render_to_response('404.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.col_add:
		response = HttpResponse(content_type='application/ms-excel')
		import string
		a = string.replace(proyecto.nombre,' ','')
		response['Content-Disposition'] = 'attachment; filename=%s.xls'%(a)
		wb = xlwt.Workbook(encoding='utf-8')
		ws = wb.add_sheet("GoAnalytics")
		datos = proyecto.proyectosdatos
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
		ws.write(0,11,u"Fecha de nacimiento dd/mm/yyyy",date_format)
		ws.write(0,12,u"Fecha de ingreso dd/mm/yyyy",date_format)
		for i in xrange(1,10000):
			ws.write(i,11,"",date_format)
			ws.write(i,12,"",date_format)
		if(datos.opcional1):
			ws.write(0,13,datos.opcional1)
		if(datos.opcional2):
			ws.write(0,14,datos.opcional2)
		if(datos.opcional3):
			ws.write(0,15,datos.opcional3)
		if(datos.opcional4):
			ws.write(0,16,datos.opcional4)
		if(datos.opcional5):
			ws.write(0,17,datos.opcional5)
		wb.save(response)
		return response

#===============================================================================
# subir participantes archivo
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def colaboradores_xls(request):
	proyecto = cache.get(request.user.username)
	if not proyecto:
		return render_to_response('423.html')
	if not proyecto.interna:
		return render_to_response('404.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.col_add:
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
				proyecto_datos = proyecto.proyectosdatos
				vector_personas = []
				vector_ignorar = []
				nacimientos_arreglados =[]
				for i in xrange(1,filas):
					if Colaboradores.objects.filter(proyecto=proyecto,email=sheet.cell_value(i,2)).exists():
						vector_ignorar.append(i)
						vector_personas.append('dummy')
						nacimientos_arreglados.append(0)
					else:
						var_error = sheet.cell_value(i,0)+' '+sheet.cell_value(i,1)
						chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
						key = ''.join(random.sample(chars, 64))
						persona = Colaboradores(
							nombre=sheet.cell_value(i,0),
							apellido = sheet.cell_value(i,1),
							key = key,
							email=sheet.cell_value(i,2),
							estado=True,proyecto=proyecto)
						try:persona.movil = sheet.cell_value(i,3)
						except:pass
						vector_personas.append(persona)
						try:
							nacimientos_arreglados.append(DT(*xlrd.xldate_as_tuple(sheet.cell_value(i,11), 0)))
						except:
							nacimientos_arreglados.append(0)
				vector_datos = []
				vector_metricas = []
				streaming_crear = []
				variables = proyecto.variables_set.all()
				preguntas = Preguntas.objects.filter(variable__in=variables)
				proyecto.tot_participantes += filas-1
				with transaction.atomic():
					for i in xrange(1,filas):
						if i not in vector_ignorar:
							vector_personas[i-1].save()
							vector_metricas.append(ColaboradoresMetricas(id=vector_personas[i-1]))
							datos = ColaboradoresDatos(id = vector_personas[i-1],
								genero=sheet.cell_value(i,4),
								area=sheet.cell_value(i,5),
								cargo=sheet.cell_value(i,6),
								regional=sheet.cell_value(i,7),
								ciudad=sheet.cell_value(i,8),
								niv_academico=sheet.cell_value(i,9),
								profesion=sheet.cell_value(i,10),
								fec_ingreso=DT(*xlrd.xldate_as_tuple(sheet.cell_value(i,12), 0))
								)
							if(nacimientos_arreglados[i-1]):
								datos.fec_nacimiento=nacimientos_arreglados[i-1]
							if proyecto_datos.opcional1:
								datos.opcional1 = sheet.cell_value(i,13)
							if proyecto_datos.opcional2:
								datos.opcional2 = sheet.cell_value(i,14)
							if proyecto_datos.opcional3:
								datos.opcional3 = sheet.cell_value(i,15)
							if proyecto_datos.opcional4:
								datos.opcional4 = sheet.cell_value(i,16)
							if proyecto_datos.opcional5:
								datos.opcional5 = sheet.cell_value(i,17)
							vector_datos.append(datos)
							for j in preguntas:
								if not Streaming.objects.filter(proyecto=proyecto,colaborador=vector_personas[i-1],pregunta=j).exists():
									streaming_crear.append(Streaming(proyecto=proyecto,colaborador=vector_personas[i-1],pregunta=j))
									proyecto.tot_aresponder += 1
					ColaboradoresDatos.objects.bulk_create(vector_datos)
					ColaboradoresMetricas.objects.bulk_create(vector_metricas)
					if(streaming_crear):
						Streaming.objects.bulk_create(streaming_crear)
					proyecto.save()
					cache.set(request.user.username,proyecto,86400)
				if(permisos.col_see):
					return HttpResponseRedirect('/participantes/individual/')
				else:
					error = "Todos los colaboradores se han subido con éxito"
			except:
				error= "Ocurrio un error cuando se procesaba al participante "+var_error

		return render_to_response('colaboradores_xls.html',{
		'Activar':'Configuracion','activar':'Participantes','activarp':'AcrhivoPlano',
		'Proyecto':proyecto,'Permisos':permisos,'Error':error
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')

#===============================================================================
# eliminar
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def colaboradoreliminar(request,id_colaborador):
	proyecto = cache.get(request.user.username)
	if not proyecto:
		return render_to_response('423.html')
	if not proyecto.interna:
		return render_to_response('404.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.col_see and permisos.col_del:
		try:
			participante = Colaboradores.objects.filter(proyecto_id=proyecto.id).get(id=int(id_colaborador))
		except:
			return render_to_response('403.html')
		if request.method == 'POST':
			maestro = Proyectos.objects.get(id=1)
			proyecto.tot_participantes -= 1
			proyecto.tot_aresponder -= Streaming.objects.filter(proyecto=proyecto,colaborador_id=int(id_colaborador)).count()
			with transaction.atomic():
				Colaboradores.objects.filter(id=id_colaborador).update(proyecto=maestro,zdel=timezone.now())
				Streaming.objects.filter(id=id_colaborador).update(proyecto=maestro)
				nom_log = request.user.first_name+' '+request.user.last_name
				Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,
				accion="Eliminó al participante",descripcion=participante.nombre+' '+participante.apellido)
				proyecto.save()
				cache.set(request.user.username,proyecto,86400)
			return HttpResponseRedirect('/participantes/individual/')
	return render_to_response('col_eliminar.html',{
	'Activar':'Configuracion','activar':'Participantes','activarp':'Individual',
	'objeto':'Participante','Participante':participante,
	'Proyecto':proyecto,'Permisos':permisos,
	}, context_instance=RequestContext(request))
