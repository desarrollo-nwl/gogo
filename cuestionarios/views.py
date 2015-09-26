# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.cache import cache
# from django.db import connection
from cuestionarios.models import *
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_control
from usuarios.models import Empresas, Proyectos, Logs


#===============================================================================
# indices
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def variables(request):
	proyecto = cache.get(request.user.username)
	if not proyecto:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_see:
		variables = proyecto.variables_set.all()
		return render_to_response('variables.html',{
		'Activar':'Configuracion','activar':'Variables','Variables':variables,
		'Proyecto':proyecto,'Permisos':permisos,
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def indicepreguntas(request,id_variable):
	proyecto = cache.get(request.user.username)
	permisos = request.user.permisos
	if permisos.consultor and permisos.per_see:
		preguntas = Preguntas.objects.filter(id=int(id_variable))
		return render_to_response('varadd.html',{
		'activarG':'1','activar':'biblio'
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


#===============================================================================
# nuevos
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def variablenueva(request):
	proyecto = cache.get(request.user.username)
	if not proyecto:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_add:
		if request.method == 'POST':
			with transaction.atomic():
				variable = Variables(
					nombre = request.POST['nombre'],
					descripcion = request.POST['descripcion'],
					posicion = request.POST['posicion'],
					proyecto = proyecto)
				try:
					if(request.POST['estado']):
						variable.estado = True
				except:
						variable.estado = False
				variable.save()
				proyecto.max_variables += 1
				proyecto.save()
				Logs.objects.create(usuario=request.user,accion="Creó la variable",descripcion=variable.nombre)
				cache.set(request.user.username,proyecto,86400)
			if(proyecto.max_variables == 1 ):
				return HttpResponseRedirect('/pregunta/nueva/')
			else:
				return HttpResponseRedirect('/variables/')
		return render_to_response('variablenueva.html',{
		'Activar':'Configuracion','activar':'Variables','Permisos':permisos,
		'Poyecto':proyecto
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def variableactivar(request,id_variable):
	proyecto = cache.get(request.user.username)
	if not proyecto:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.act_variables:
		try:variable = Variables.objects.only('estado').get(id=int(id_variable))
		except:return HttpResponseRedirect('/variables/')
		if(variable.estado):
			variable.estado = False
		else:
			variable.estado = True
		variable.save
		variable.save()
		return HttpResponseRedirect('/variables/')
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def nuevapregunta(request,id_variable):
	proyecto = cache.get(request.user.username)
	permisos = request.user.permisos
	if permisos.consultor and permisos.pre_add:
		variable = Variables.objects.get(id = int(id_variable))
		if request.method == 'POST':
			pregunta = Preguntas(
						texto = request.POST['pregunta'],
						posicion = request.POST['posicion'],
						variable = variable)
			pregunta.abierta = bool(int(request.POST['abierta']))
			pregunta.multiple = bool(int(request.POST['multiple']))
			pregunta.numerica = bool(int(request.POST['numerica']))
			pregunta.save()
			if not ( pregunta.abierta ):
				for i in xrange(int(request.POST['respuestas'])):
					respuesta = request.POST[str(i)]
					if(respuesta):
						aux_numerico = '%s%s'%(i,i)
						numerico = request.POST[aux_numerico]
						if(numerico):
							Respuestas.objects.create(
							texto = respuesta, numerico = numerico, pregunta = pregunta )
						else:
							R = Respuestas.objects.create( texto = respuesta, pregunta = pregunta )
			variable.max_preguntas += 1
			variable.save()
			return HttpResponseRedirect( '/cuestionario/variables/'+id_variable )
		return render_to_response('create3.html',{
		'activarG':'1','activar':'biblio','idbp':idbp
		}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('403.html')

#===============================================================================
# editar
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def variableditar(request,id_variable):
	proyecto = cache.get(request.user.username)
	if not proyecto:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_edit:
		try:variable = Variables.objects.get(id=int(id_variable))
		except:render_to_response('403.html')
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
				Logs.objects.create(usuario=request.user,accion="Editó la variable",descripcion=variable.nombre)
				return HttpResponseRedirect('/variables/')
		return render_to_response('variableditar.html',{
		'Activar':'Configuracion','activar':'Variables','Permisos':permisos,
		'Proyecto':proyecto,'Variable':variable
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def editarpregunta(request,id_pregunta):
	proyecto = cache.get(request.user.username)
	permisos = request.user.permisos
	if permisos.consultor and permisos.pre_edit:
		pregunta = Preguntas.objects.get(id = int(id_pregunta)
					).prefetch_related('respuestas_set')
		if request.method == 'POST':
			pregunta.texto = request.POST['pregunta'],
			pregunta.posicion = request.POST['posicion'],
			pregunta.abierta = bool(int(request.POST['abierta']))
			pregunta.multiple = bool(int(request.POST['multiple']))
			pregunta.numerica = bool(int(request.POST['numerica']))
			pregunta.save()
			if not ( pregunta.abierta ):
				pregunta.respuestas_set.delete()
				for i in xrange(int(request.POST['respuestas'])):
					respuesta = request.POST[str(i)]
					if(respuesta):
						aux_numerico = '%s%s'%(i,i)
						numerico = request.POST[aux_numerico]
						if(numerico):
							Respuestas.objects.create(
							texto = respuesta, numerico = numerico, pregunta = pregunta )
						else:
							R = Respuestas.objects.create( texto = respuesta, pregunta = pregunta )
			return HttpResponseRedirect( '/cuestionario/variables/'+str(pregunta.variable_id) )
		return render_to_response('create3.html',{
		'activarG':'1','activar':'biblio','idbp':idbp
		}, context_instance=RequestContext(request))

	else:
		return HttpResponseRedirect('403.html')

#===============================================================================
# clonar
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def clonarproyecto(request,id_proyecto):
	permisos = request.user.permisos
	if permisos.consultor and permisos.pro_add:
		return render_to_response('create1.html',{
		'activarG':'1','activar':'biblio'
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def clonarvariable(request,id_variable):
	proyecto = cache.get(request.user.username)
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_add:
		variable = Variables.objects.get(id=int(id_variable)
					).select_related('proyecto__max_variables'
					).prefetch_related('preguntas_set__respuestas_set')
		try:
			variable.id = None
			variable.posicion = variable.proyecto.max_variables+1
			with transaction.atomic():
				variable.save()
				variable.proyecto.max_variables += 1; proyecto.save()
				preguntas_nuevas = []
				respuestas_nuevas = []
				for j in variable.preguntas_set.all():
					j.id = None
					j.variable = variable
					preguntas_nuevas.append(j)
					for k in j.respuestas_set.all():
						k.id = None
						k.pregunta = j
						respuestas_nuevas.append(k)
				Preguntas.objects.bulk_create(preguntas_nuevas)
				Respuestas.objects.bulk_create(respuestas_nuevas)
		except IntegrityError:
			handle_exception()
		return HttpResponseRedirect('/cuestionario/variables/')
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def clonarpregunta(request,id_pregunta):
	proyecto = cache.get(request.user.username)
	permisos = request.user.permisos
	if permisos.consultor and permisos.pre_edit:
		pregunta = Preguntas.objects.get(id = int(id_pregunta)
					).select_related('variable__max_preguntas').prefetch_related('respuestas_set')
		try:
			pregunta.id = None
			pregunta.posicion = pregunta.variable.max_preguntas+1
			with transaction.atomic():
				pregunta.save()
				pregunta.variable.max_preguntas += 1; variable.save()
				respuestas_nuevas = []
				for k in pregunta.respuestas_set.all():
					k.id = None
					k.pregunta = pregunta
					respuestas_nuevas.append(k)
				Respuestas.objects.bulk_create(respuestas_nuevas)
		except IntegrityError:
			handle_exception()
		return HttpResponseRedirect( '/cuestionario/variables/'+str(pregunta.variable_id) )
	else:
		return HttpResponseRedirect('403.html')

#===============================================================================
# eliminar
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def variableliminar(request,id_variable):
	proyecto = cache.get(request.user.username)
	if not proyecto:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_del:
		try:
			variable = Variables.objects.get(id=int(id_variable))
		except:
			return render_to_response('403')
		if request.method == 'POST':
			with transaction.atomic():
				Variables.objects.filter(id=int(id_variable)).update(proyecto_id=1)
				proyecto.max_variables -= 1
				proyecto.save()
				cache.set(request.user.username,proyecto,86400)
				Logs.objects.create(usuario=request.user,accion="Eliminó la variable",descripcion=variable.nombre)
			return HttpResponseRedirect('/variables/')
		return render_to_response('cue_eliminar.html',{
		'Activar':'Configuracion','activar':'Variables','Permisos':permisos,
		'Variable':variable,'objeto':'Variable'
		}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def eliminarpregunta(request,id_variable):
	proyecto = cache.get(request.user.username)
	permisos = request.user.permisos
	if permisos.consultor and permisos.pre_del:
		if request.method == 'POST':
			Variables.objects.filter(id=1).update(proyecto_id=1)
			return HttpResponseRedirect('/cuestionario/variables/')
		return render_to_response('cue_eliminar.html',{
		'activarG':'1','activar':'biblio'
		}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('403.html')

#===============================================================================
# Previsualizacion del cuestionario
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/login')
def preencuesta(request):
	proyecto = cache.get(request.user.username)
	permisos = request.user.permisos
	if permisos.consultor and permisos.pro_see and permisos.var_see and permisos.pre_see:
		cuestionario = Proyectos.objects.prefetch_related(
		'variables_set__preguntas_set__respuestas_set').get(id=proyecto.id)
		return render_to_response('preencuesta.html',{
		'Cuestionario':cuestionario
		},	context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('403.html')
