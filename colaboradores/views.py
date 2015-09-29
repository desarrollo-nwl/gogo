# -*- encoding: utf-8 -*-
from colaboradores.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_control
from usuarios.models import Proyectos, Logs
from datetime import datetime as DT
#===============================================================================
# indices
#===============================================================================


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def colaboradores(request):
	proyecto = cache.get(request.user.username)
	if not proyecto:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.col_see:
		participantes = Colaboradores.objects.filter(proyecto=proyecto
						).only('nombre','apellido','email','colaboradoresdatos__cargo'
						).select_related('colaboradoresdatos')
		return render_to_response('colaboradores.html',{
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
	permisos = request.user.permisos
	if permisos.consultor and permisos.col_add:
		if request.method == 'POST':
			participante = Colaboradores(
				nombre = request.POST['nombre'],
				apellido = request.POST['apellido'],
				email = request.POST['email'],
				proyecto = proyecto)
			try:
				if(request.POST['estado']):
					participante.estado = True
			except:
				participante.estado = False
			datos = ColaboradoresDatos(
				id = participante,
				area = request.POST['area'],
				cargo = request.POST['cargo'],
				ciudad = request.POST['ciudad'],
				fec_ingreso = DT.strptime(str(request.POST['fec_ingreso']),'%d/%m/%Y'),
				genero = request.POST['genero'],
				niv_academico = request.POST['niv_academico'],
				profesion = request.POST['profesion'],
				regional = request.POST['regional'],)
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
			with transaction.atomic():
				participante.save()
				datos.save()
				nom_log = request.user.first_name+' '+request.user.last_name
				Logs.objects.create(usuario=nom_log,usuario_username=request.user.username,
				accion="Creó al participante",descripcion=participante.nombre+' '+participante.apellido)
			return HttpResponseRedirect('/participantes/individual')
		return render_to_response('colaboradornuevo.html',{
		'Activar':'Configuracion','activar':'Participantes','activarp':'Individual',
		'Proyecto':proyecto,'Permisos':permisos,
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def colaboradoreditar(request,id_colaborador):
	proyecto = cache.get(request.user.username)
	if not proyecto:
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.col_edit:
		try:participante = Colaboradores.objects.filter(proyecto=proyecto
							).select_related('colaboradoresdatos').get(id=int(id_colaborador))
		except:return render_to_response('403.html')
		if request.method == 'POST':
			participante.nombre = request.POST['nombre']
			participante.apellido = request.POST['apellido']
			participante.email = request.POST['email']
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
		'Proyecto':proyecto,'Permisos':permisos,'Participante':participante
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def colaboradoractivar(request,id_colaborador):
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
		return HttpResponseRedirect('/participantes/individual')
	else:
		return render_to_response('403.html')
