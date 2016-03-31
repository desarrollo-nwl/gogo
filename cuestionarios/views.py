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
from django.utils import timezone
from django.views.decorators.cache import cache_control
from usuarios.models import Empresas, Proyectos, Logs


#===============================================================================
# indices
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def variables(request):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["360 redes","360 unico"]:
		return render_to_response('423.html')
	proyecto = Proyectos.objects.get(id=proyecto.id)
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
def preguntas(request,id_variable):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["360 redes","360 unico"]:
		return render_to_response('423.html')
	proyecto = Proyectos.objects.get(id=proyecto.id)
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_see:
		try:variable = Variables.objects.prefetch_related('preguntas_set'
						).get(id=id_variable)
		except:return render_to_response('403.html')
		return render_to_response('preguntas.html',{
		'Activar':'Configuracion','activar':'Variables','Variable':variable,
		'Proyecto':proyecto,'Permisos':permisos,
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
	if not proyecto or proyecto.tipo in ["360 redes","360 unico"]:
		return render_to_response('423.html')
	proyecto = Proyectos.objects.get(id=proyecto.id)
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
				nom_log = request.user.first_name+' '+request.user.last_name
				Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,accion="Creó la variable",descripcion=variable.nombre)
				cache.set(request.user.username,proyecto,86400)
			if(proyecto.max_variables == 1 ):
				return HttpResponseRedirect('/variable/'+str(variable.id)+'/pregunta/nueva/')
			else:
				return HttpResponseRedirect('/variables/')
		return render_to_response('variablenueva.html',{
		'Activar':'Configuracion','activar':'Variables','Permisos':permisos,
		'Proyecto':proyecto
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def variableactivar(request,id_variable):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["360 redes","360 unico"]:
		return render_to_response('423.html')
	proyecto = Proyectos.objects.get(id=proyecto.id)
	permisos = request.user.permisos
	if permisos.consultor and permisos.act_variables:
		try:
			variable = Variables.objects.only('estado').filter(proyecto_id=proyecto.id).get(id=int(id_variable))
		except:
			return HttpResponseRedirect('/variables/')
		if(variable.estado):
			variable.estado = False
		else:
			variable.estado = True
		with transaction.atomic():
			variable.save()
			Preguntas.objects.filter(variable=variable).update(estado=variable.estado)
		return HttpResponseRedirect('/variables/')
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def preguntanueva(request,id_variable):
	proyecto = cache.get(request.user.username)
	if not proyecto:
		return render_to_response('423.html')
	proyecto = Proyectos.objects.get(id=proyecto.id)
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_add:
		try:variable = Variables.objects.filter(proyecto_id=proyecto.id).get(id = int(id_variable))
		except:return render_to_response('403.html')
		if request.method == 'POST':
			pregunta = Preguntas(
						texto = request.POST['texto'],
						posicion = request.POST['posicion'],
						variable = variable)

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
						Respuestas.objects.create(texto = respuesta, numerico = numerico, pregunta = pregunta )

				elif not( pregunta.abierta or pregunta.numerica):
					for i in xrange(int(request.POST['contador'])):
						aux_texto = 'respuesta%s'%(i)
						respuesta = request.POST[aux_texto]
						R = Respuestas.objects.create( texto = respuesta, pregunta = pregunta )
				proyecto.tot_preguntas += 1
				proyecto.save()
				variable.max_preguntas += 1
				variable.save()
				nom_log = request.user.first_name+' '+request.user.last_name
				Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,accion='Creó la pregunta',descripcion=pregunta.texto)
			cache.set(request.user.username,proyecto,86400)
			return HttpResponseRedirect( '/variable/'+id_variable+'/preguntas/' )
		return render_to_response('preguntanueva.html',{
		'Activar':'Configuracion','activar':'Variables','Permisos':permisos,
		'Proyecto':proyecto,'Variable':variable
		}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def preguntactivar(request,id_pregunta):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["360 redes","360 unico"]:
		return render_to_response('423.html')
	proyecto = Proyectos.objects.get(id=proyecto.id)
	permisos = request.user.permisos
	if permisos.consultor and permisos.act_variables and permisos.var_edit:
		try:
			pregunta = Preguntas.objects.get(id=int(id_pregunta))
			variable = Variables.objects.filter(proyecto_id=proyecto.id).get(id=pregunta.variable_id)
		except:
			return HttpResponseRedirect('/variables/')
		if(pregunta.estado):
			pregunta.estado = False
		else:
			variable.estado = True
			pregunta.estado = True
		with transaction.atomic():
			variable.save()
			pregunta.save()
		return HttpResponseRedirect('/variable/'+str(variable.id)+'/preguntas/')
	else:
		return render_to_response('403.html')

#===============================================================================
# editar
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def variableditar(request,id_variable):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["360 redes","360 unico"]:
		return render_to_response('423.html')
	proyecto = Proyectos.objects.get(id=proyecto.id)
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_edit:
		try:variable = Variables.objects.filter(proyecto_id=proyecto.id).get(id=int(id_variable))
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
				nom_log = request.user.first_name+' '+request.user.last_name
				Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,accion="Editó la variable",descripcion=variable.nombre)
				return HttpResponseRedirect('/variables/')
		return render_to_response('variableditar.html',{
		'Activar':'Configuracion','activar':'Variables','Permisos':permisos,
		'Proyecto':proyecto,'Variable':variable
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def preguntaeditar(request,id_pregunta):
	proyecto = cache.get(request.user.username)
	if not proyecto:
		return render_to_response('423.html')
	proyecto = Proyectos.objects.get(id=proyecto.id)
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_edit:
		try:
			pregunta = Preguntas.objects.get(id=int(id_pregunta))
			variable = Variables.objects.filter(proyecto_id=proyecto.id).get(id=pregunta.variable_id)
			num_respuestas = pregunta.respuestas_set.count()
		except:render_to_response('403.html')
		if request.method == 'POST':
			pregunta.texto = request.POST['texto']
			pregunta.posicion = request.POST['posicion']
			pregunta.variable = variable

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
				pregunta.respuestas_set.all().delete()
				if ((not  pregunta.abierta) and pregunta.numerica):
					for i in xrange(int(request.POST['contador'])):
						aux_texto = 'respuesta%s'%(i)
						respuesta = request.POST[aux_texto]
						aux_numerico = 'numerico%s'%(i)
						numerico = request.POST[aux_numerico]
						Respuestas.objects.create(texto = respuesta, numerico = numerico, pregunta = pregunta )

				elif not( pregunta.abierta or pregunta.numerica):
					for i in xrange(int(request.POST['contador'])):
						aux_texto = 'respuesta%s'%(i)
						respuesta = request.POST[aux_texto]
						R = Respuestas.objects.create( texto = respuesta, pregunta = pregunta )
				nom_log = request.user.first_name+' '+request.user.last_name
				Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,accion='Editó la pregunta',descripcion=pregunta.texto)
			cache.set(request.user.username,proyecto,86400)
			return HttpResponseRedirect( '/variable/'+str(variable.id)+'/preguntas/' )
		return render_to_response('preguntaeditar.html',{
		'Activar':'Configuracion','activar':'Variables','Permisos':permisos,
		'Proyecto':proyecto,'Variable':variable,'Pregunta':pregunta,
		'numero_respuestas':num_respuestas
		}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('403.html')



#===============================================================================
# clonar
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def variableclonar(request,id_variable):
	proyecto = cache.get(request.user.username)
	if not proyecto:
		return render_to_response('423.html')
	proyecto = Proyectos.objects.get(id=proyecto.id)
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_add:
		try:
			variable = Variables.objects.select_related('proyecto__max_variables'
						).prefetch_related('preguntas_set__respuestas_set'
						).get(id=int(id_variable))
		except:
			return render_to_response('403.html')
		variable.id = None
		variable.posicion = variable.proyecto.max_variables+1
		with transaction.atomic():
			variable.save()
			proyecto.max_variables += 1; proyecto.save()
			respuestas_nuevas = []
			for pregunta in variable.preguntas_set.all():
				pregunta.id = None
				pregunta.variable = variable
				proyecto.tot_preguntas += 1
				proyecto.save()
				pregunta.save()
				for respuesta in pregunta.respuestas_set.all():
					respuesta.id = None
					respuesta.pregunta = pregunta
					respuestas_nuevas.append(respuesta)
			Respuestas.objects.bulk_create(respuestas_nuevas)
			nom_log = request.user.first_name+' '+request.user.last_name
			Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,accion="Clonó la variable",descripcion=variable.nombre)
		cache.set(request.user.username,proyecto,86400)

		return HttpResponseRedirect('/variables/')
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def preguntaclonar(request,id_pregunta):
	proyecto = cache.get(request.user.username)
	if not proyecto:
		return render_to_response('423.html')
	proyecto = Proyectos.objects.get(id=proyecto.id)
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_add:
		try:
			pregunta = Preguntas.objects.prefetch_related('respuestas_set'
						).get(id = int(id_pregunta))
			variable = Variables.objects.filter(proyecto_id=proyecto.id
						).get(id=pregunta.variable_id)

			pregunta.id = None
			pregunta.posicion = variable.max_preguntas+1
			with transaction.atomic():
				pregunta.save()
				proyecto.tot_preguntas += 1; proyecto.save()
				variable.max_preguntas += 1; variable.save()
				respuestas_nuevas = []
				for respuesta in pregunta.respuestas_set.all():
					respuesta.id = None
					respuesta.pregunta = pregunta
					respuestas_nuevas.append(respuesta)
				Respuestas.objects.bulk_create(respuestas_nuevas)
				nom_log = request.user.first_name+' '+request.user.last_name
				Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,accion="Clonó la pregunta",descripcion=pregunta.texto)
			cache.set(request.user.username,proyecto,86400)
		except:
			return render_to_response('403.html')
		return HttpResponseRedirect( '/variable/'+str(variable.id)+'/preguntas/')
	else:
		return HttpResponseRedirect('403.html')

#===============================================================================
# eliminar
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def variableliminar(request,id_variable):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["360 redes","360 unico"]:
		return render_to_response('423.html')
	proyecto = Proyectos.objects.get(id=proyecto.id)
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_del:
		try:
			variable = Variables.objects.filter(proyecto_id=proyecto.id).get(id=int(id_variable))
		except:
			return render_to_response('403')
		if request.method == 'POST':
			maestro = Proyectos.objects.get(id=1)
			with transaction.atomic():
				variable = Variables.objects.get(id=id_variable)
				variable.proyecto=maestro
				variable.zdel=timezone.now()
				variable.save()
				proyecto.max_variables -= 1
				proyecto.tot_preguntas -= variable.max_preguntas;
				proyecto.save()
				nom_log = request.user.first_name+' '+request.user.last_name
				Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,accion="Eliminó la variable",descripcion=variable.nombre)
			cache.set(request.user.username,proyecto,86400)
			return HttpResponseRedirect('/variables/')
		return render_to_response('cue_eliminar.html',{
		'Activar':'Configuracion','activar':'Variables','Permisos':permisos,
		'Variable':variable,'objeto':'Variable'
		}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def preguntaeliminar(request,id_pregunta):
	proyecto = cache.get(request.user.username)
	if not proyecto:
		return render_to_response('423.html')
	proyecto = Proyectos.objects.get(id=proyecto.id)
	permisos = request.user.permisos
	if permisos.consultor and permisos.var_del:
		try:
			pregunta = Preguntas.objects.get(id=int(id_pregunta))
			variable = Variables.objects.filter(proyecto_id=proyecto.id).get(id=pregunta.variable_id)
		except:
			return HttpResponseRedirect('/variables/')
		if request.method == 'POST':
			pregunta.variable_id = 1
			variable.max_preguntas -= 1
			proyecto.tot_preguntas -= 1
			pregunta.zdel = timezone.now()
			nom_log = request.user.first_name+' '+request.user.last_name
			with transaction.atomic():
				pregunta.save()
				variable.save()
				proyecto.save()
				Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,accion="Eliminó la pregunta",descripcion=pregunta.texto)
			cache.set(request.user.username,proyecto,86400)
			return HttpResponseRedirect('/variable/'+str(variable.id)+'/preguntas/')

		return render_to_response('cue_eliminar.html',{
		'Activar':'Configuracion','activar':'Variables','Permisos':permisos,
		'Proyecto':proyecto,'Variable':variable,'Pregunta':pregunta,'objeto':'Pregunta'
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
	if permisos.consultor and permisos.pro_see and permisos.var_see:
		cuestionario = Proyectos.objects.prefetch_related(
		'variables_set__preguntas_set__respuestas_set').get(id=proyecto.id)
		return render_to_response('preencuesta.html',{
		'Cuestionario':cuestionario
		},	context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('403.html')
