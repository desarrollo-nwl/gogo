# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import transaction
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.views.decorators.cache import cache_control
from usuarios.models import Proyectos, Logs
from datetime import datetime as DT
from cuestionarios_360.models import *
from colaboradores_360.models import *
from mensajeria_360.models import Streaming_360
import random, colabora
#===============================================================================
# indices
#===============================================================================


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def colaboradores_ind_360(request):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"] :
		return render_to_response('423.html')
	if not proyecto.interna:
		return render_to_response('404.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.col_see:
		# participantes = Colaboradores_360.objects.filter(proyecto=proyecto
		# 				).only(
		# 					'nombre','apellido','email',
		# 					'colaboradoresdatos_360__cargo','estado'
		# 				).select_related('colaboradoresdatos_360')
		tabla = colabora.ver_colaboradores(str(proyecto.id),permisos.col_edit,permisos.col_del)
		print tabla
		return render_to_response('colaboradores_ind_360.html',{
		'Activar':'Contenido','activar':'Individual',
		'Proyecto':proyecto,'Permisos':permisos,'Tabla':tabla
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')

#===============================================================================
# nuevo
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def colaboradornuevo_360(request):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"] :
		return render_to_response('423.html')
	if not proyecto.interna:
		return render_to_response('404.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.col_add:
		emails = Colaboradores_360.objects.only('email').filter(proyecto_id=proyecto.id)
		if request.method == 'POST':
			chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
			key = ''.join(random.sample(chars, 64))
			if not Colaboradores_360.objects.filter(proyecto=proyecto,email=request.POST['email']).exists():
				participante = Colaboradores_360(
								nombre = request.POST['nombre'],
								apellido = request.POST['apellido'],
								key = key,
								key_old = 'HACK',
								email = request.POST['email'].lower(),
								genero = request.POST['genero'],
								proyecto_id = proyecto.id)

				try:
					if(request.POST['estado']):
						participante.estado = True
				except:
					participante.estado = False

				try:
					if(request.POST['externo']):
						participante.externo = True
				except:
					participante.externo = False

				try: participante.descripcion = request.POST['descripcion']
				except: participante.descripcion = None

				with transaction.atomic():
					participante.save()
					datos = ColaboradoresDatos_360(
						id = participante,
						area = request.POST['area'],
						cargo = request.POST['cargo'],
						ciudad = request.POST['ciudad'],
						fec_ingreso = DT.strptime(str(request.POST['fec_ingreso']),'%d/%m/%Y'),
						regional = request.POST['regional'])
					try:datos.niv_academico = request.POST['niv_academico']
					except:pass
					try:datos.profesion = request.POST['profesion']
					except:pass
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
					ColaboradoresMetricas_360.objects.create(id=participante)
					#  dependiendo del tipo se ejecuta auto o no
					if (proyecto.tipo =="360 unico"):
						instrumento = Instrumentos_360.objects.only('id').filter( proyecto_id = proyecto.id )[0]
						preguntas = Preguntas_360.objects.filter( proyecto_id = proyecto.id, instrumento_id=instrumento.id)
						for j in preguntas:
							try:
								streaming_crear.append(Streaming_360(
														proyecto_id=proyecto.id,
														instrumento_id=instrumento.id,
														colaborador_id=participante.id,
														pregunta_id=j.id))
								proyecto.tot_aresponder += 1
							except:
								pass
						if(proyecto.tot_aresponder):
							proyecto.total = 100.0*proyecto.tot_respuestas/proyecto.tot_aresponder
						else:
							proyecto.total = 0.0
						if(streaming_crear):
							Streaming_360.objects.bulk_create(streaming_crear)
						proyecto.save()
						cache.set(request.user.username,proyecto,86400)
					nom_log = request.user.first_name+' '+request.user.last_name
					Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,
					accion="Creó al participante",descripcion=participante.nombre+' '+participante.apellido)
				return HttpResponseRedirect('/360/participantes/individual')

		return render_to_response('colaborador.html',{
		'Activar':'Contenido','activar':'Individual','accion':'registrar',
		'Proyecto':proyecto,'Permisos':permisos,'Emails':emails
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


#===============================================================================
# editar
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def colaboradoreditar_360(request,id_colaborador):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"] :
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.col_edit:
		try:participante = Colaboradores_360.objects.filter(proyecto=proyecto
							).select_related('colaboradoresdatos_360').get(id=id_colaborador)
		except:return render_to_response('403.html')
		emails = Colaboradores_360.objects.only('email').filter(proyecto=proyecto).exclude(id=id_colaborador)
		if request.method == 'POST':
			if not Colaboradores_360.objects.exclude(id=id_colaborador).filter(proyecto=proyecto,email=request.POST['email']).exists():
				participante.nombre = request.POST['nombre']
				participante.apellido = request.POST['apellido']
				participante.email = request.POST['email']
				participante.genero = request.POST['genero']
				try:
					if(request.POST['estado']):
						participante.estado = True
				except:
					participante.estado = False
				try:
					if(request.POST['externo']):
						participante.externo = True
				except:
					participante.externo = False
				try:
					if(request.POST['descripcion']):
						participante.descripcion = True
				except:
					participante.descripcion = False
				datos = participante.colaboradoresdatos_360
				datos.area = request.POST['area']
				datos.cargo = request.POST['cargo']
				datos.ciudad = request.POST['ciudad']
				datos.fec_ingreso = DT.strptime(str(request.POST['fec_ingreso']),'%d/%m/%Y')
				try:
					if(request.POST['fec_nacimiento']):
						datos.fec_nacimiento = DT.strptime(str(request.POST['fec_nacimiento']),'%d/%m/%Y')
				except:
					datos.fec_nacimiento = None
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
				return HttpResponseRedirect('/360/participantes/individual')
		return render_to_response('colaborador.html',{
		'Activar':'Contenido','activar':'Individual','accion':'editar',
		'Proyecto':proyecto,'Permisos':permisos,'Participante':participante,'Emails':emails,
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')

#===============================================================================
# activar/desactivar
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def colaboradoractivar_360(request,id_colaborador):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"] :
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.col_edit:
		try:participante = Colaboradores_360.objects.only('estado').filter(proyecto=proyecto).get(id=id_colaborador)
		except:return render_to_response('403.html')
		if(participante.estado):
			 Colaboradores_360.objects.filter(id=id_colaborador).update(estado=False)
		else:
			Colaboradores_360.objects.filter(id=id_colaborador).update(estado=True)
		return JsonResponse({'id': id_colaborador,'estado':1-int(participante.estado)})
	else:
		return render_to_response('403.html')

#===============================================================================
# nuevo archivo
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def archivo_360(request):
	import xlwt
	date_format = xlwt.XFStyle()
	date_format.num_format_str = 'dd/mm/yyyy'
	tit_format = xlwt.easyxf('font:bold on ;align:wrap on, vert centre, horz center;')
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"] :
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
		ws = wb.add_sheet("Participantes")
		datos = proyecto.proyectosdatos
		ws.write(0,0,u"Nombre",tit_format)
		ws.write(0,1,u"Apellido",tit_format)
		ws.write(0,2,u"Email",tit_format)
		ws.write(0,3,u"Género",tit_format)
		ws.write(0,4,u"Área",tit_format)
		ws.write(0,5,u"Cargo",tit_format)
		ws.write(0,6,u"Regional",tit_format)
		ws.write(0,7,u"Ciudad",tit_format)
		ws.write(0,8,u"Nivel académico",tit_format)
		ws.write(0,9,u"Profesión",tit_format)
		ws.write(0,10,u"Fecha de nacimiento dd/mm/yyyy",tit_format)
		ws.write(0,11,u"Fecha de ingreso dd/mm/yyyy",tit_format)
		for i in xrange(1,10000):
			ws.write(i,10,"",date_format)
			ws.write(i,11,"",date_format)
		if(datos.opcional1):
			ws.write(0,12,datos.opcional1,tit_format)
		if(datos.opcional2):
			ws.write(0,13,datos.opcional2,tit_format)
		if(datos.opcional3):
			ws.write(0,14,datos.opcional3,tit_format)
		if(datos.opcional4):
			ws.write(0,15,datos.opcional4,tit_format)
		if(datos.opcional5):
			ws.write(0,16,datos.opcional5,tit_format)
		ws = wb.add_sheet("Evaluadores externos")
		ws.write(0,0,u"Nombre",tit_format)
		ws.write(0,1,u"Apellido",tit_format)
		ws.write(0,2,u"Email",tit_format)
		ws.write(0,3,u"Género",tit_format)
		ws.write(0,4,u"Descripción",tit_format)
		wb.save(response)
		return response

#===============================================================================
# subir participantes archivo
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def colaboradores_xls_360(request):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"] :
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
			ext_sheet = doc.sheet_by_index(1)
			ext_filas = ext_sheet.nrows
			var_error = None
			try:
				proyecto_datos = proyecto.proyectosdatos
				vector_personas = []
				vector_ignorar = []
				nacimientos_arreglados =[]
				chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
				for i in xrange(1,filas):
					if Colaboradores.objects.filter(proyecto=proyecto,email=sheet.cell_value(i,2)).exists():
						vector_ignorar.append(i)
						vector_personas.append('dummy')
						nacimientos_arreglados.append(0)
					else:
						var_error = sheet.cell_value(i,0)+' '+sheet.cell_value(i,1)
						key = ''.join(random.sample(chars, 64))
						persona = Colaboradores_360(
							nombre=sheet.cell_value(i,0),
							apellido = sheet.cell_value(i,1),
							key = key,
							email=sheet.cell_value(i,2).lower(),
							estado=True,proyecto=proyecto)
						try:persona.movil = sheet.cell_value(i,3)
						except:pass
						vector_personas.append(persona)
						try:
							nacimientos_arreglados.append(DT(*xlrd.xldate_as_tuple(sheet.cell_value(i,11), 0)))
						except:
							nacimientos_arreglados.append(0)
				colaboradores_externos = []
				for i in xrange(1,ext_filas):
					if not ColaboradoresExternos_360.objects.filter(proyecto_id=proyecto.id,email=sheet.cell_value(i,2)).exists():
						key = ''.join(random.sample(chars, 64))
						colaboradores_externos.append( ColaboradoresExternos_360(
												nombre=sheet.cell_value(i,0),
												apellido = sheet.cell_value(i,1),
												key = key,
												email=sheet.cell_value(i,2).lower(),
												genero=sheet.cell_value(i,3).capitalize(),
												descripcion=sheet.cell_value(i,4),
												estado=True,proyecto=proyecto)
												)
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
								genero=sheet.cell_value(i,4).capitalize(),
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

		return render_to_response('colaboradores_xls_360.html',{
		'Activar':'Contenido','activar':'AcrhivoPlano',
		'Proyecto':proyecto,'Permisos':permisos,'Error':error
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')

#===============================================================================
# eliminar
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def colaboradoreliminar_360(request,id_colaborador):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"] :
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
			proyecto.tot_respuestas -= Streaming.objects.filter(proyecto=proyecto,colaborador_id=int(id_colaborador),respuesta__isnull=False).count()
			if(proyecto.tot_aresponder):
				proyecto.total = 100.0*proyecto.tot_respuestas/proyecto.tot_aresponder
			else:
				proyecto.total = 0.0
			with transaction.atomic():
				Colaboradores.objects.filter(id=id_colaborador).delete()
				nom_log = request.user.first_name+' '+request.user.last_name
				Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,
				accion="Eliminó al participante",descripcion=participante.nombre+' '+participante.apellido)
				proyecto.save()
				cache.set(request.user.username,proyecto,86400)
			return HttpResponseRedirect('/participantes/individual/')
	return render_to_response('col_eliminar.html',{
	'Activar':'Contenido','activar':'Individual',
	'objeto':'Participante','Participante':participante,
	'Proyecto':proyecto,'Permisos':permisos,
	}, context_instance=RequestContext(request))
