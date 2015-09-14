# -*- encoding: utf-8 -*-
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_control
from usuarios.models import *
from django.db import connection
#===============================================================================
# Front end
#===============================================================================

@cache_control(no_store=True)
def index(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/menu/')
	else:
		return render_to_response('index.html',context_instance=RequestContext(request))

#===============================================================================
# login - logout
#===============================================================================

@cache_control(no_store=True)
def acceder(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/menu/')
	error = None
	if request.method == 'POST':
		acceso = False
		try:
			acceso = authenticate(
			username = User.objects.only('username').get(email = request.POST['email']),
			password = request.POST['clave'])
			if acceso is None:
				error = 'Los datos proporcionados son incorrectos.'
			else:
				if acceso.is_active:
					login(request,acceso)
					return HttpResponseRedirect('/menu/')
				else:
					error = 'Su usuario se encuentra desactivado'
		except:
			error = 'Los datos proporcionados son incorrectos.'
	return render_to_response('login.html',{
	'Error':error,
	}, context_instance=RequestContext(request))


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def menu(request):
	try:
		empresas = request.user.usuario.empresas.all()
		if len(empresas) == 1:
			if empresas[0].activa:

				cache.set(request.user.username,empresas[0],86400)
				return HttpResponseRedirect('/home/')
			else:
				error = empresas[0].nombre +' se encuentra desactivada.'
				return render_to_response('menu.html',{
				'Empresas':empresas,'Error':error
				}, context_instance=RequestContext(request))
		else:
			return render_to_response('menu.html',{
			'Empresas':empresas,
			}, context_instance=RequestContext(request))
	except:
		Errores.objects.create(
			usuario=request.user,
			registro='No tiene empresas asociadas y no se pudo loguear!')
		return render_to_response('500.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def menu2(request,id_empresa):
	try:
		empresa = request.user.usuario.empresas.get(id=int(id_empresa))
		if empresa.activa:
			cache.set(request.user.username,empresa,86400)
			return HttpResponseRedirect('/home/')
		else:
			return render_to_response('403.html')
	except:
			return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def home(request):
	empresa = cache.get(request.user)
	return render_to_response('home.html',{
	'Empresa':empresa,
	}, context_instance=RequestContext(request))


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def salir(request):
	cache.delete(request.user)
	logout(request)
	return HttpResponseRedirect('/acceder/')

#===============================================================================
#    Páginas de errores
#===============================================================================

@cache_control(no_store=True)
def e400(request):
	return render_to_response('400.html')

@cache_control(no_store=True)
def e403(request):
	return render_to_response('403.html')

@cache_control(no_store=True)
def e404(request):
	return render_to_response('404.html')

@cache_control(no_store=True)
def e500(request):
	return render_to_response('500.html')
