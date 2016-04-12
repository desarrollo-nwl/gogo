# -*- encoding: utf-8 -*-
from cuestionarios_360.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import transaction
from django.db.models import F
from django.http import HttpResponseRedirect,HttpResponse
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils import timezone
from django.views.decorators.cache import cache_control
from usuarios.models import Empresas, Proyectos, Logs
from mensajeria_360.models import Streaming_360

#===============================================================================
# indices
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def instrumentos(request):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"]:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_see:
		instrumentos = Instrumentos_360.objects.filter(proyecto_id = proyecto.id)
		if(proyecto.max_variables > 0 and proyecto.tipo =="360 unico"):
			bandera = False
		else:
			bandera = True
		return render_to_response('instrumentos.html',{
			'Activar':'Contenido','activar':'Instrumentos','Instrumentos':instrumentos,
			'Proyecto':proyecto,'Permisos':permisos,'Agregar_instrumento':bandera
			}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def dimensiones(request,id_instrumento):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"]:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_see:
		try:instrumento = Instrumentos_360.objects.only('id','proyecto_id').filter(proyecto_id=proyecto.id ).get(id=id_instrumento)
		except:return render_to_response('404.html')
		dimensiones = Dimensiones_360.objects.filter(proyecto_id = proyecto.id,instrumento_id=instrumento.id)
		return render_to_response('dimensiones.html',{
			'Activar':'Contenido','activar':'Instrumentos','Instrumento':instrumento,
			'Proyecto':proyecto,'Permisos':permisos,'Dimensiones':dimensiones,
			}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def variables_360(request,id_dimension):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"]:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_see:
		try:dimension = Dimensiones_360.objects.only('id','proyecto_id','instrumento_id','nombre').filter(proyecto_id=proyecto.id ).get(id=id_dimension)
		except:return render_to_response('404.html')
		variables = Variables_360.objects.filter(proyecto_id=proyecto.id,dimension_id=dimension.id )
		return render_to_response('variables_360.html',{
		'Activar':'Contenido','activar':'Instrumentos','Variables':variables,
		'Proyecto':proyecto,'Permisos':permisos,'Instrumento_id':dimension.instrumento_id,
		'Dimension':dimension
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def preguntas_360(request,id_variable):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"]:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor:
		try:variable = Variables_360.objects.filter(proyecto_id=proyecto.id).get(id=id_variable)
		except:return render_to_response('404.html')
		preguntas = Preguntas_360.objects.filter(proyecto_id=proyecto.id,variable_id=variable.id)
		return render_to_response('preguntas_360.html',{
		'Activar':'Contenido','activar':'Instrumentos','Variable':variable,
		'Proyecto':proyecto,'Permisos':permisos,'Instrumento_id':variable.instrumento_id,
		'Dimension_id':variable.dimension_id,'Preguntas':preguntas
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


#===============================================================================
# nuevos
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def instrumentonuevo(request):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"]:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_add:
		if proyecto.tipo == '360 unico' and proyecto.max_variables >= 1:
			return render_to_response('403.html')
		instrumentos = Instrumentos_360.objects.only('nombre').filter(proyecto_id=proyecto.id)
		if request.method == 'POST':

			if(Instrumentos_360.objects.filter(proyecto_id=proyecto.id,nombre=request.POST['nombre']).exists()):
				return render_to_response('instrumento.html',{
				'Activar':'Contenido','activar':'Dimensiones','Proyecto':proyecto,'Instrumentos':instrumentos,
				'Permisos':permisos,'accion':'registrar',"Error":"Este instrumento ya existe"
				},context_instance=RequestContext(request))

			with transaction.atomic():
				instrumento = Instrumentos_360(
					nombre = request.POST['nombre'],
					proyecto_id = proyecto.id)
				try:
					if(request.POST['estado']):
						instrumento.estado = True
				except:
					instrumento.estado = False
				instrumento.save()
				Proyectos.objects.filter(id=proyecto.id).update(
					max_variables = F('max_variables') + 1)
				nom_log = request.user.first_name+' '+request.user.last_name
				Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,accion="Creó el instrumento",descripcion=instrumento.nombre)
				proyecto.max_variables += 1
				cache.set(request.user.username,proyecto,86400)
				proyecto = cache.get(request.user.username)
				return HttpResponseRedirect(''.join(['/360/instrumento/',str(instrumento.id),'/dimension/nueva/']))

		return render_to_response('instrumento.html',{
			'Activar':'Contenido','activar':'Dimensiones','Proyecto':proyecto,
			'Permisos':permisos,'accion':'registrar','Instrumentos':instrumentos
			}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def dimensionueva(request,id_instrumento):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"]:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_add:
		try:instrumento = Instrumentos_360.objects.only('id','proyecto_id').filter(proyecto_id=proyecto.id ).get(id=id_instrumento)
		except:return render_to_response('403.html')
		if request.method == 'POST':
			with transaction.atomic():
				dimension = Dimensiones_360(
					nombre = request.POST['nombre'],
					descripcion = request.POST['descripcion'],
					posicion = request.POST['posicion'],
					proyecto_id = proyecto.id,
					instrumento_id = instrumento.id)
				try:
					if(request.POST['estado']):
						dimension.estado = True
				except:
					dimension.estado = False
				dimension.save()
				Instrumentos_360.objects.filter(id=instrumento.id).update(
					max_dimensiones = F('max_dimensiones') + 1)
				nom_log = request.user.first_name+' '+request.user.last_name
				Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,accion="Creó la dimensión",descripcion=dimension.nombre)

				return HttpResponseRedirect(''.join(['/360/dimension/',str(dimension.id),'/variable/nueva']))

		return render_to_response('dimension.html',{
		'Activar':'Configuracion','activar':'Variables','Permisos':permisos,
		'Proyecto':proyecto,'accion':'registrar','Instrumento':instrumento
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def variablenueva_360(request,id_dimension):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"]:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_add:
		try:dimension = Dimensiones_360.objects.only('id','proyecto_id','instrumento_id').filter(proyecto_id=proyecto.id ).get(id=id_dimension)
		except:return render_to_response('403.html')
		if request.method == 'POST':
			with transaction.atomic():
				variable = Variables_360(
					nombre = request.POST['nombre'],
					descripcion = request.POST['descripcion'],
					posicion = request.POST['posicion'],
					proyecto_id = proyecto.id,
					instrumento_id = dimension.instrumento_id,
					dimension_id = dimension.id)
				try:
					if(request.POST['estado']):
						variable.estado = True
				except:
						variable.estado = False
				variable.save()
				Dimensiones_360.objects.filter(id=dimension.id).update(
					max_variables = F('max_variables') + 1)
				nom_log = request.user.first_name+' '+request.user.last_name
				Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,accion="Creó la variable",descripcion=variable.nombre)
				return HttpResponseRedirect(''.join(['/360/variable/',str(variable.id),'/pregunta/nueva']))

		return render_to_response('variable.html',{
		'Activar':'Configuracion','activar':'Variables','Permisos':permisos,
		'Proyecto':proyecto,'accion':'registrar','Instrumento_id':dimension.instrumento_id,
		'Dimension':dimension,'accion':'registrar'
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def preguntanueva_360(request,id_variable):
	proyecto = cache.get(request.user.username)
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_add:
		try:variable = Variables_360.objects.filter(proyecto_id=proyecto.id).get(id = id_variable)
		except:return render_to_response('404.html')
		if request.method == 'POST':
			pregunta = Preguntas_360(
						texto = request.POST['texto'],
						posicion = request.POST['posicion'],
						puntaje = request.POST['puntaje'],
						proyecto_id = proyecto.id,
						instrumento_id = variable.instrumento_id,
						dimension_id = variable.dimension_id,
						variable_id = variable.id)

			if(request.POST['tipo'] =="Abierta"):
				pregunta.abierta = True
				pregunta.numerica = False
				pregunta.multiple = False
			elif(request.POST['tipo'] =="Unica"):
				pregunta.abierta = False
				pregunta.numerica = False
				pregunta.multiple = False
			elif(request.POST['tipo'] =="Numerica"):
				pregunta.abierta = False
				pregunta.numerica = True
				pregunta.multiple = False
			elif(request.POST['tipo'] =="Multiple"):
				pregunta.abierta = False
				pregunta.numerica = False
				pregunta.multiple =True
			elif(request.POST['tipo'] =="MultipleNumerica"):
				pregunta.abierta = False
				pregunta.numerica = True
				pregunta.multiple =True
			else:
				return render_to_response('500.html')
			try:
				if(bool(request.POST['estado']) and variable.estado):
					pregunta.estado = True
				else:
					pregunta.estado = False
			except:
				pregunta.estado = False
			with transaction.atomic():
				pregunta.save()
				if ((not  pregunta.abierta) and pregunta.numerica):
					for i in xrange(int(request.POST['contador'])):
						aux_texto = 'respuesta%s'%(i)
						respuesta = request.POST[aux_texto]
						aux_numerico = 'numerico%s'%(i)
						numerico = request.POST[aux_numerico]
						Respuestas_360.objects.create(texto = respuesta, numerico = numerico, pregunta = pregunta )

				elif not( pregunta.abierta or pregunta.numerica):
					for i in xrange(int(request.POST['contador'])):
						aux_texto = 'respuesta%s'%(i)
						respuesta = request.POST[aux_texto]
						R = Respuestas_360.objects.create( texto = respuesta, pregunta = pregunta )

				Variables_360.objects.filter(id=variable.id).update(max_preguntas = F('max_preguntas') + 1)
				Instrumentos_360.objects.filter(id=variable.instrumento_id).update(max_preguntas = F('max_preguntas') + 1)
				nom_log = request.user.first_name+' '+request.user.last_name
				Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,accion='Creó la pregunta',descripcion=pregunta.texto)

			return HttpResponseRedirect(''.join(['/360/variable/',str(variable.id),'/preguntas/']))
		return render_to_response('pregunta.html',{
		'Activar':'Contenido','activar':'Instrumentos','Permisos':permisos,
		'Proyecto':proyecto,'Variable':variable,'Dimension_id':variable.dimension_id,
		'Instrumento_id':variable.instrumento_id,'accion':'registrar','numero_respuestas':1
		}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('403.html')

#===============================================================================
# activar
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def instrumentoactivar(request,id_instrumento):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"]:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.act_variables:
		try:
			instrumento = Instrumentos_360.objects.only('id','estado').filter(proyecto_id=proyecto.id).get(id=id_instrumento)
		except:
			return render_to_response('404.html')
		if(instrumento.estado):
			instrumento.estado = False
		else:
			instrumento.estado = True
		with transaction.atomic():
			Instrumentos_360.objects.filter(id=instrumento.id).update(estado=instrumento.estado)
			Dimensiones_360.objects.filter(instrumento_id=instrumento.id).update(estado=instrumento.estado)
			Variables_360.objects.filter(instrumento_id=instrumento.id).update(estado=instrumento.estado)
			Preguntas_360.objects.filter(instrumento_id=instrumento.id).update(estado=instrumento.estado)
		return JsonResponse({'id': id_instrumento,'estado':int(instrumento.estado)})
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def dimensionactivar(request,id_dimension):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"]:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.act_variables:
		try:
			dimension = Dimensiones_360.objects.only('id','estado').filter(proyecto_id=proyecto.id).get(id=id_dimension)
		except:
			return render_to_response('404.html')
		if(dimension.estado):
			dimension.estado = False
		else:
			dimension.estado = True
		with transaction.atomic():
			Dimensiones_360.objects.filter(id=dimension.id).update(estado=dimension.estado)
			Variables_360.objects.filter(dimension_id=dimension.id).update(estado=dimension.estado)
			Preguntas_360.objects.filter(dimension_id=dimension.id).update(estado=dimension.estado)
		return JsonResponse({'id': id_dimension,'estado':int(dimension.estado)})
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def variableactivar_360(request,id_variable):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"]:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.act_variables:
		try:
			variable = Variables_360.objects.only('id','estado').filter(proyecto_id=proyecto.id).get(id=id_variable)
		except:
			return render_to_response('404.html')
		if(variable.estado):
			variable.estado = False
		else:
			variable.estado = True
		with transaction.atomic():
			Variables_360.objects.filter(id=variable.id).update(estado=variable.estado)
			Preguntas_360.objects.filter(variable_id=variable.id).update(estado=variable.estado)
		return JsonResponse({'id': id_variable,'estado':int(variable.estado)})
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def preguntactivar_360(request,id_pregunta):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"]:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.act_variables:
		try:
			pregunta = Preguntas_360.objects.only('id','estado').filter(proyecto_id=proyecto.id).get(id=id_pregunta)
		except:
			return HttpResponse('404')
		if(pregunta.estado):
			Preguntas_360.objects.filter(id=pregunta.id).update(estado=False)
		else:
			Preguntas_360.objects.filter(id=pregunta.id).update(estado=True)
		return JsonResponse({'id': id_pregunta,'estado':1-int(pregunta.estado)})
	else:
		return render_to_response('403.html')


# #===============================================================================
# # editar
# #===============================================================================


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def instrumentoeditar(request,id_instrumento):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"]:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_add:
		try:instrumento = Instrumentos_360.objects.filter(proyecto_id=proyecto.id).get(id=id_instrumento)
		except:render_to_response('404.html')
		instrumentos = Instrumentos_360.objects.only('nombre').filter(proyecto_id=proyecto.id).exclude(id=id_instrumento)
		if request.method == 'POST':

			if(Instrumentos_360.objects.exclude(id=id_instrumento).filter(nombre=request.POST['nombre']).exists()):
				return render_to_response('instrumento.html',{
				'Activar':'Contenido','activar':'Dimensiones','Proyecto':proyecto,'Instrumentos':instrumentos,
				'Permisos':permisos,'accion':'editar','Instrumento':instrumento,"Error":"Este instrumento ya existe"
				},context_instance=RequestContext(request))

			with transaction.atomic():
				instrumento.nombre = request.POST['nombre']
				try:
					if(request.POST['estado']):
						instrumento.estado = True
				except:
						instrumento.estado = False
				instrumento.save()
				nom_log = request.user.first_name+' '+request.user.last_name
				Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,accion="Editó el instrumento",descripcion=instrumento.nombre)
				return HttpResponseRedirect('/360/instrumentos/')

		return render_to_response('instrumento.html',{
			'Activar':'Contenido','activar':'Dimensiones','Proyecto':proyecto,
			'Permisos':permisos,'accion':'editar','Instrumento':instrumento,
			'Instrumentos':instrumentos
			}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def dimensioneditar(request,id_dimension):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"]:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_edit:
		try:dimension = Dimensiones_360.objects.filter(proyecto_id=proyecto.id).get(id=id_dimension)
		except:render_to_response('404.html')
		if request.method == 'POST':
			with transaction.atomic():
				dimension.nombre = request.POST['nombre']
				dimension.descripcion = request.POST['descripcion']
				dimension.posicion = request.POST['posicion']
				if(permisos.act_variables):
					try:
						if(request.POST['estado']):
							dimension.estado = True
					except:
							dimension.estado = False
				dimension.save()
				nom_log = request.user.first_name+' '+request.user.last_name
				Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,accion="Editó la dimension",descripcion=dimension.nombre)
				return HttpResponseRedirect(''.join(['/360/instrumento/',str(dimension.instrumento_id),'/dimensiones/']))
		return render_to_response('dimension.html',{
		'Activar':'Configuracion','activar':'Variables','Permisos':permisos,
		'Proyecto':proyecto,'Dimension':dimension,'accion':'editar','Instrumento_id':dimension.instrumento_id
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def variableditar_360(request,id_variable):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"]:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_edit:
		try:variable = Variables_360.objects.only('id','instrumento_id','dimension_id').filter(proyecto_id=proyecto.id).get(id=id_variable)
		except:render_to_response('404.html')
		if request.method == 'POST':
			with transaction.atomic():
				variable.nombre = request.POST['nombre']
				variable.descripcion = request.POST['descripcion']
				variable.posicion = request.POST['posicion']
				if(permisos.act_variables):
					try:
						if(request.POST['estado']):
							variable.estado = True
					except:
							variable.estado = False
				variable.save()
				nom_log = request.user.first_name+' '+request.user.last_name
				Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,accion="Editó la variable",descripcion=variable.nombre)
				return HttpResponseRedirect(''.join(['/360/dimension/',str(variable.dimension_id),'/variables/']))
		return render_to_response('variable.html',{
		'Activar':'Configuracion','activar':'Variables','Permisos':permisos,'Variable':variable,
		'Proyecto':proyecto,'Dimension_id':variable.dimension_id,'accion':'editar','Instrumento_id':variable.instrumento_id
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def preguntaeditar_360(request,id_pregunta):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"]:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_edit:
		try:
			pregunta = Preguntas_360.objects.filter(proyecto_id=proyecto.id,id=id_pregunta
						).prefetch_related('respuestas_360_set')[0]
			variable = Variables_360.objects.only('id','estado').get(id=pregunta.variable_id)
			num_respuestas = pregunta.respuestas_360_set.count()
		except:render_to_response('403.html')
		if request.method == 'POST':
			pregunta.texto = request.POST['texto']
			pregunta.posicion = request.POST['posicion']
			pregunta.puntaje = request.POST['puntaje']

			if(request.POST['tipo'] =="Abierta"):
				pregunta.abierta = True
				pregunta.numerica = False
				pregunta.multiple = False
			elif(request.POST['tipo'] =="Unica"):
				pregunta.abierta = False
				pregunta.numerica = False
				pregunta.multiple = False
			elif(request.POST['tipo'] =="Numerica"):
				pregunta.abierta = False
				pregunta.numerica = True
				pregunta.multiple = False
			elif(request.POST['tipo'] =="Multiple"):
				pregunta.abierta = False
				pregunta.numerica = False
				pregunta.multiple =True
			elif(request.POST['tipo'] =="MultipleNumerica"):
				pregunta.abierta = False
				pregunta.numerica = True
				pregunta.multiple =True
			else:
				return render_to_response('500.html')
			try:
				if(request.POST['estado']):
					if(variable.estado):
						pregunta.estado = True
					else:
						pregunta.estado = False
			except:
				pregunta.estado = False
			with transaction.atomic():
				pregunta.save()
				pregunta.respuestas_360_set.all().delete()
				if ((not  pregunta.abierta) and pregunta.numerica):
					for i in xrange(int(request.POST['contador'])):
						aux_texto = 'respuesta%s'%(i)
						respuesta = request.POST[aux_texto]
						aux_numerico = 'numerico%s'%(i)
						numerico = request.POST[aux_numerico]
						Respuestas_360.objects.create(texto = respuesta, numerico = numerico, pregunta = pregunta )

				elif not( pregunta.abierta or pregunta.numerica):
					for i in xrange(int(request.POST['contador'])):
						aux_texto = 'respuesta%s'%(i)
						respuesta = request.POST[aux_texto]
						R = Respuestas_360.objects.create( texto = respuesta, pregunta = pregunta )
				nom_log = request.user.first_name+' '+request.user.last_name
				Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,accion='Editó la pregunta',descripcion=pregunta.texto)

			return HttpResponseRedirect( ''.join(['/360/variable/',str(variable.id),'/preguntas/']) )
		return render_to_response('pregunta.html',{
		'Activar':'Configuracion','activar':'Variables','Permisos':permisos,
		'Proyecto':proyecto,'Variable':variable,'Pregunta':pregunta,
		'numero_respuestas':num_respuestas,'accion':'editar'
		}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('403.html')


#===============================================================================
# clonar
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def preguntaclonar_360(request,id_pregunta):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"]:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_add:
		try:
			pregunta = Preguntas_360.objects.prefetch_related('respuestas_360_set'
						).get(id = id_pregunta)
			variable = Variables_360.objects.filter(proyecto_id=proyecto.id
						).get(id=pregunta.variable_id)

			pregunta.id = None
			pregunta.texto = 'Copia de '+ pregunta.texto
			pregunta.posicion = variable.max_preguntas+1
			with transaction.atomic():
				pregunta.save()
				variable.max_preguntas += 1; variable.save()
				Instrumentos_360.objects.filter(id=variable.instrumento_id).update(max_preguntas = F('max_preguntas') + 1)
				respuestas_nuevas = []
				for respuesta in pregunta.respuestas_360_set.all():
					respuesta.id = None
					respuesta.pregunta = pregunta
					respuestas_nuevas.append(respuesta)
				Respuestas_360.objects.bulk_create(respuestas_nuevas)
				nom_log = request.user.first_name+' '+request.user.last_name
				Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,accion="Copió la pregunta",descripcion=pregunta.texto)
			return HttpResponseRedirect( ''.join(['/360/variable/',str(variable.id),'/preguntas/']) )
		except:
			return render_to_response('404.html')
	else:
		return HttpResponseRedirect('403.html')


#===============================================================================
# eliminar
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def preguntaeliminar_360(request,id_pregunta):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"]:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_del:
		try:pregunta = Preguntas_360.objects.filter(proyecto_id=proyecto.id).get(id=id_pregunta)
		except:return render_to_response('404.html')
		if request.method == 'POST':
			variable_id_old = str(pregunta.variable_id)
			with transaction.atomic():
				Variables_360.objects.filter(id=pregunta.variable_id).update(max_preguntas = F('max_preguntas') -1)
				Instrumentos_360.objects.filter(id=pregunta.instrumento_id).update(max_preguntas = F('max_preguntas') - 1)
				Streaming_360.objects.filter(pregunta_id=pregunta.id).update(proyecto_id=1)
				pregunta.variable_id = 1
				pregunta.dimension_id = 1
				pregunta.instrumento_id = 1
				pregunta.proyecto_id = 1
				pregunta.zdel = timezone.now()
				nom_log = request.user.first_name+' '+request.user.last_name
				pregunta.save()
				Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,accion="Eliminó la pregunta",descripcion=pregunta.texto)

			return HttpResponseRedirect(''.join(['/360/variable/',variable_id_old,'/preguntas/']) )

		return render_to_response('cue360_eliminar.html',{
		'Activar':'Contenido','activar':'Instrumentos','Permisos':permisos,
		'Proyecto':proyecto,'Pregunta':pregunta,'objeto':'Pregunta'
		}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def variableliminar_360(request,id_variable):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"]:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_del:
		try:variable = Variables_360.objects.filter(proyecto_id=proyecto.id).get(id=id_variable)
		except:return render_to_response('404.html')
		if request.method == 'POST':
			dimension_id_old = str(variable.dimension_id)
			with transaction.atomic():
				Dimensiones_360.objects.filter(id=variable.dimension_id).update(max_variables= F('max_variables') -1)
				Preguntas_360.objects.filter(variable=variable.id).update(proyecto_id = 1,instrumento_id=1,dimension_id = 1)
				variable.dimension_id = 1
				variable.instrumento_id = 1
				variable.proyecto_id = 1
				variable.zdel = timezone.now()
				nom_log = request.user.first_name+' '+request.user.last_name
				variable.save()
				Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,accion="Eliminó la variable",descripcion=variable.nombre)

			return HttpResponseRedirect(''.join(['/360/dimension/',dimension_id_old,'/variables/']) )

		return render_to_response('cue360_eliminar.html',{
		'Activar':'Contenido','activar':'Instrumentos','Permisos':permisos,
		'Proyecto':proyecto,'Variable':variable,'objeto':'Variable'
		}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def dimensioneliminar(request,id_dimension):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"]:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_del:
		try:dimension = Dimensiones_360.objects.filter(proyecto_id=proyecto.id).get(id=id_dimension)
		except:return render_to_response('404.html')
		if request.method == 'POST':
			instrumento_id_old = str(dimension.instrumento_id)
			with transaction.atomic():
				Instrumentos_360.objects.filter(id=dimension.instrumento_id).update(max_dimensiones= F('max_dimensiones') -1)
				Variables_360.objects.filter(dimension=dimension.id).update(proyecto_id = 1,instrumento_id=1)
				Preguntas_360.objects.filter(dimension=dimension.id).update(proyecto_id = 1,instrumento_id=1)
				dimension.instrumento_id = 1
				dimension.proyecto_id = 1
				dimension.zdel = timezone.now()
				nom_log = request.user.first_name+' '+request.user.last_name
				dimension.save()
				Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,accion="Eliminó la dimension",descripcion=dimension.nombre)

			return HttpResponseRedirect(''.join(['/360/instrumento/',instrumento_id_old,'/dimensiones/']) )

		return render_to_response('cue360_eliminar.html',{
		'Activar':'Contenido','activar':'Instrumentos','Permisos':permisos,
		'Proyecto':proyecto,'Dimension':dimension,'objeto':'Dimension'
		}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def instrumentoeliminar(request,id_instrumento):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa","360 unico"]:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_del:
		try:instrumento = Instrumentos_360.objects.filter(proyecto_id=proyecto.id).get(id=id_instrumento)
		except:return render_to_response('404.html')
		if request.method == 'POST':
			with transaction.atomic():
				Proyectos.objects.filter(id=proyecto.id).update(max_variables = F('max_variables') -1)
				Dimensiones_360.objects.filter(instrumento=instrumento.id).update(proyecto_id = 1)
				Variables_360.objects.filter(instrumento=instrumento.id).update(proyecto_id = 1)
				Preguntas_360.objects.filter(instrumento=instrumento.id).update(proyecto_id = 1)
				instrumento.proyecto_id = 1
				instrumento.zdel = timezone.now()
				nom_log = request.user.first_name+' '+request.user.last_name
				instrumento.save()
				Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,accion="Eliminó el instrumento",descripcion=instrumento.nombre)

			return HttpResponseRedirect( '/360/instrumentos/' )

		return render_to_response('cue360_eliminar.html',{
		'Activar':'Contenido','activar':'Instrumentos','Permisos':permisos,
		'Proyecto':proyecto,'Instrumento':instrumento,'objeto':'Instrumento'
		}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('403.html')


#===============================================================================
# Previsualizacion del cuestionario
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/login')
def previsualizacion_360(request,id_instrumento):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"]:
		return render_to_response('423.html')
	permisos = request.user.permisos
	instrumento = Instrumentos_360.objects.filter(id=id_instrumento,proyecto_id=proyecto.id).first()
	if permisos.consultor and instrumento:

		preguntas = Preguntas_360.objects.filter(
						proyecto_id = proyecto.id, instrumento_id = instrumento.id
					).select_related('variable','dimension').prefetch_related('respuestas_360_set')

		vector_orden = []

		for i in preguntas:
			vector_orden.append( (i.dimension.posicion,i.variable.posicion,i.posicion,i.id) )

		vector_orden.sort()

		return render_to_response('previsualizacion_360.html',{
		'Activar':'Contenido','activar':'Instrumentos','Permisos':permisos,
		'Proyecto':proyecto,'Preguntas':preguntas,'Orden':vector_orden
		}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def exportar_instrumento_360(request,id_instrumento):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa","360 unico"] :
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_see:
		import xlwt, string
		str_format = xlwt.easyxf(num_format_str="@")
		tit_format = xlwt.easyxf('font:bold on ;align:wrap on, vert centre, horz center;')
		response = HttpResponse(content_type='application/ms-excel')
		a = string.replace(proyecto.nombre,' ','')
		response['Content-Disposition'] = 'attachment; filename=%s.xls'%(a)
		wb = xlwt.Workbook(encoding='utf-8')
		ws = wb.add_sheet(a)

		preguntas = Preguntas_360.objects.filter(
						proyecto_id = proyecto.id, instrumento_id = id_instrumento
					).select_related('variable','dimension','instrumento').prefetch_related('respuestas_360_set')

		vector_orden = []

		for i in preguntas:
			vector_orden.append( ( 	i.dimension.posicion, i.variable.posicion, i.posicion,
									i.dimension.id, i.variable.id, i.id) )

		vector_orden.sort()

		ws.write(0,0,u"Instrumento (R)")
		ws.write(0,1,u"Dimensión (R)")
		ws.write(0,2,u"Dimensión Texto encuesta")
		ws.write(0,3,u"Variable (R)")
		ws.write(0,4,u"Variable Texto encuesta")
		ws.write(0,5,u"Pregunta (R)")
		ws.write(0,6,u"Puntaje")
		ws.write(0,7,u"Tipo (R)")
		ws.write(0,8,u"Respuesta")
		ws.write(0,9,u"Valor")

		if len(preguntas):
			ws.write(1,0,preguntas[0].instrumento.nombre)

		dimensiones = []
		variables = []
		preguntas_aux = []
		bandera = True
		i = 1

		for orden in vector_orden:
			for dim in preguntas:
				if dim.dimension.id == orden[3]:
					if not (dim.dimension.id in dimensiones):
						dimensiones.append(dim.dimension.id)
						ws.write(i,1,dim.dimension.nombre,str_format)
						ws.write(i,2,dim.dimension.descripcion,str_format)

					for var in preguntas:
						if var.variable.id == orden[4]:
							if not var.variable.id in variables:
								variables.append(var.variable.id)
								ws.write(i,3,var.variable.nombre,str_format)
								ws.write(i,4,var.variable.descripcion,str_format)

							for pre in preguntas:
								if pre.id == orden[5]:
									if not (pre.id in preguntas_aux):
										preguntas_aux.append(pre.id)
										ws.write(i,5,pre.texto,str_format)
										ws.write(i,6,pre.puntaje,str_format)

										if pre.abierta:
											ws.write(i,7,u"Abierta",str_format)
										elif pre.multiple:
											ws.write(i,7,u"Múltiple",str_format)
										else:
											ws.write(i,7,u"Única",str_format)

										for res in pre.respuestas_360_set.all():
											bandera = False
											ws.write(i,8,res.texto,str_format)
											ws.write(i,9,res.numerico,str_format)
											i += 1
										if pre.abierta or bandera:
											i += 1
		ws.write(i,0,u'FIN',tit_format)
		wb.save(response)
		return response
	else:
		render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def plantilla_instrumento_360(request):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"] :
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.col_add:
		import xlwt, string
		tit_format = xlwt.easyxf('font:bold on ;align:wrap on, vert centre, horz center;')
		response = HttpResponse(content_type='application/ms-excel')
		a = string.replace(proyecto.nombre,' ','')
		response['Content-Disposition'] = 'attachment; filename=%s.xls'%(a)
		wb = xlwt.Workbook(encoding='utf-8')
		ws = wb.add_sheet(proyecto.nombre)
		ws.write(0,0,u"Instrumento (R)",tit_format)
		ws.write(0,1,u"Dimensión (R)",tit_format)
		ws.write(0,2,u"Dimensión Texto encuesta",tit_format)
		ws.write(0,3,u"Variable (R)",tit_format)
		ws.write(0,4,u"Variable Texto encuesta",tit_format)
		ws.write(0,5,u"Pregunta (R)",tit_format)
		ws.write(0,6,u"Puntaje",tit_format)
		ws.write(0,7,u"Tipo (R)",tit_format)
		ws.write(0,8,u"Respuesta",tit_format)
		ws.write(0,9,u"Valor",tit_format)
		wb.save(response)
		return response


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def importar_instrumento_360(request):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa","360 unico"] :
		return render_to_response('423.html')
	error = ""
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_add:

		if request.method == 'POST':
			import xlrd, string
			input_excel = request.FILES['docfile']
			doc = xlrd.open_workbook(file_contents=input_excel.read())
			sheet = doc.sheet_by_index(0)

			with transaction.atomic():
				i = 1
				pos_dim = 0
				pos_var = 0
				pos_pre = 0

				while sheet.cell_value(i,0) != 'FIN':
					if sheet.cell_value(i,0) != '' :
						instrumento = Instrumentos_360.objects.create(nombre = sheet.cell_value(i,0), proyecto_id = proyecto.id)
						proyecto.max_variables += 1
						proyecto.save()
						pos_dim = 1

					if sheet.cell_value(i,1) != '' :
						dimension = Dimensiones_360(
										posicion = pos_dim,
										nombre = sheet.cell_value(i,1),
										proyecto_id = proyecto.id,
										instrumento_id = instrumento.id)
						if sheet.cell_value(i,2) != '' :
							dimension.descripcion = sheet.cell_value(i,2)
						instrumento.max_dimensiones += 1
						dimension.save()
						pos_dim += 1
						pos_var = 1

					if sheet.cell_value(i,3) != '' :
						variable =  Variables_360(
										posicion = pos_var,
										nombre = sheet.cell_value(i,3),
										proyecto_id = proyecto.id,
										instrumento_id = instrumento.id,
										dimension_id = dimension.id)
						if sheet.cell_value(i,4) != '' :
							variable.descripcion = sheet.cell_value(i,4)
						dimension.max_variables += 1
						dimension.save()
						variable.save()
						pos_var += 1
						pos_pre = 1

					if sheet.cell_value(i,5) != '' :
						pregunta = Preguntas_360(texto = sheet.cell_value(i,5),
												instrumento_id = instrumento.id ,
												dimension_id = dimension.id,
						 						variable_id = variable.id,
												proyecto_id = proyecto.id,
												posicion = pos_pre)
						pos_pre += 1
						if sheet.cell_value(i,6) != '':
							pregunta.puntaje = float( sheet.cell_value(i,6) )
						else:
							pregunta.puntaje = 1


						if sheet.cell_value(i,7).lower() == u'Abierta'.lower():
							pregunta.abierta = True
							pregunta.multiple = False
							pregunta.numerica = False

						elif sheet.cell_value(i,7).lower() == u'Múltiple'.lower():
							pregunta.abierta = False
							pregunta.multiple = True
							if sheet.cell_value(i,6) != '':
								pregunta.numerica = True
							else:
								pregunta.numerica = False

						elif sheet.cell_value(i,7).lower() == u'Única'.lower():
							pregunta.abierta = False
							pregunta.multiple = False
							if sheet.cell_value(i,6) != '':
								pregunta.numerica = True
							else:
								pregunta.numerica = False

						instrumento.max_preguntas += 1
						variable.max_preguntas += 1
						instrumento.save()
						variable.save()
						pregunta.save()

					if sheet.cell_value(i,8) != '' :
						respuesta = Respuestas_360(texto = sheet.cell_value(i,8),
										pregunta_id = pregunta.id)
						if sheet.cell_value(i,9) != '' :
							print "respuesta",sheet.cell_value(i,9)
							respuesta.numerico = float( sheet.cell_value(i,9) )
						respuesta.save()

					i += 1
			return HttpResponseRedirect('/360/instrumentos/')

		return render_to_response('instrumentos_xls_360.html',{
		'Activar':'Contenido','activar':'Instrumentos',
		'Proyecto':proyecto,'Permisos':permisos,'Error':error
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')
