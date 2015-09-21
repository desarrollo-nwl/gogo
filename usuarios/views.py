# -*- encoding: utf-8 -*-
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.cache import cache
# from django.db import connection
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_control
from usuarios.models import *
import random

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.utils
import smtplib
#===============================================================================
# Front end
#===============================================================================

@cache_control(no_store=True)
def index(request):

	chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
	captcha = ''.join(random.sample(chars, 5))

	if not request.user.is_anonymous():
		return HttpResponseRedirect('/home/')

	if request.method == 'POST':
		try:
			if( request.POST['variable'] == request.POST['captcha']):
				server=smtplib.SMTP('smtp.mandrillapp.com',587)
				server.ehlo()
				server.starttls()
				server.login('no-reply@gochangeanalytics.com','anVgUmTPhGyqT8J9D5yM1A')

				destinatario = ['ilgaleanos@gmail.com','ricardo.montoya@networkslab.co']
				msg=MIMEMultipart()
				msg["subject"]=  'Persona interesada Go Salud xD.'
				msg['To'] = email.utils.formataddr(('Respetado', destinatario))
				msg['From'] = email.utils.formataddr(('Go salud', 'no-reply@gochangeanalytics.com'))

				n = (request.POST['nombre']).encode('ascii','ignore')
				e = (request.POST['email']).encode('ascii','ignore')
				t = (request.POST['telefono']).encode('ascii','ignore')
				m = (request.POST['mensaje']).encode('ascii','ignore')
				html = '<b>NOMBRE:</b> '+ n +'<br>'
				html = html+'  <b>EMAIL:</b> '+str(e)+'<br>'
				html = html+'  <b>TELEFONO: </b>'+str(t)+'<br>'
				html = html+'  <b>MENSAJE: </b><br> '+ m

				parte2=MIMEText(html,"html")
				msg.attach(parte2)

				server.sendmail('no-reply@gochangeanalytics.com',destinatario,msg.as_string())
				server.quit()
				return HttpResponseRedirect('/index/')
		except:
			return HttpResponseRedirect('/index/#contact/')

	return render_to_response('index.html',{
	'captcha':captcha
	}, context_instance=RequestContext(request))

#===============================================================================
# login - logout
#===============================================================================

@cache_control(no_store=True)
def acceder(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/home/')
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
					return HttpResponseRedirect('/home/')
				else:
					error = 'Su usuario se encuentra desactivado'
		except:
			error = 'Los datos proporcionados son incorrectos.'
	return render_to_response('login.html',{
	'Error':error,
	}, context_instance=RequestContext(request))


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def home(request):
	if request.user.is_superuser:
		proyectos = Proyectos.objects.all().select_related('empresa__nombre')
	else:
		proyectos = Proyectos.objects.filter( usuarios = user.request).select_related('empresa__nombre')
	return render_to_response('home.html',{
	'Activar':'MisProyectos','Proyectos':proyectos
	}, context_instance=RequestContext(request))


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def menu(request,id_proyecto):
	try:
		if request.user.is_superuser:
			proyecto = Proyectos.objects.get(id=int(id_proyecto)
						).select_related('empresa__nombre')
		else:
			proyecto = Proyectos.objects.filter(
			usuarios = user.request).select_related('empresa__nombre'
			).get(id=int(id_proyecto))
		cache.set(request.user.username,proyecto,86400)
		return HttpResponseRedirect('/home2/')
	except:
			return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def home2(request):
	permisos = request.user.permisos
	if permisos.consultor:
		proyecto = cache.get(request.user.username)
		return render_to_response('home2.html',{
		'Activar':'home2','Permisos':permisos,'Proyecto':proyecto
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def salir(request):
	cache.delete(request.user)
	logout(request)
	return HttpResponseRedirect('/acceder/')


#===============================================================================
#    Páginas de recuperar usuario
#===============================================================================


@cache_control(no_store=True)
def recuperar(request):
	aviso = None
	if request.method == 'POST':
		ema = request.POST['email']
		try:
			u = User.objects.get(email = ema)
			envio,_ = Envio.objects.get_or_create( email = ema )
			hora_local = timezone.now()
			hora_envio = envio.fregistro
			delta = hora_local - hora_envio

			if(delta.days >= 1 or (delta.seconds>=3600 or 2 >= delta.seconds)):
				chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
				serie = ''.join(random.sample(chars, 32))
				u.set_password(serie)
				u.save()
				aviso = enviar2(ema,serie)
			else:
				aviso = 'Ya se ha enviado el correo, verifique su correo.'

		except:
			aviso = 'Error en el requerimiento'

	return render_to_response('recuperar.html',{
	'Aviso':aviso
	}, context_instance=RequestContext(request))

#===============================================================================
#   Empresas
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def empresas(request):
	permisos = request.user.permisos
	if permisos.consultor:
		empresas = Empresas.objects.filter(usuario=request.user)
		return render_to_response('empresas.html',{
		'Activar':'Configuracion','activar':'Empresas','Empresas':empresas
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def empresaeditar(request,id_empresa):
	permisos = request.user.permisos
	if permisos.consultor:
		empresas = Empresas.objects.filter(usuario=request.user)
		return render_to_response('empresaeditar.html',{
		'Activar':'Configuracion','activar':'Empresas','Empresas':empresas
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def empresaeliminar(request,id_empresa):
	permisos = request.user.permisos
	if permisos.consultor:
		empresas = Empresas.objects.filter(usuario=request.user)
		return render_to_response('empresas.html',{
		'Activar':'Configuracion','activar':'Empresas','Empresas':empresas
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def empresanueva(request):
	permisos = request.user.permisos
	if permisos.consultor:
		empresas = Empresas.objects.filter(usuario=request.user)
		return render_to_response('empresanueva.html',{
		'Activar':'Configuracion','activar':'Empresas','Empresas':empresas
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')

#===============================================================================
#   Proyecto
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def proyectonuevo(request):
	permisos = request.user.permisos
	if permisos.consultor:
		empresas = Empresas.objects.filter(usuario=request.user)
		return render_to_response('proyectonuevo.html',{
		'Activar':'MisProyectos'
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def proyectoeditar(request,id_proyecto):
	permisos = request.user.permisos
	if permisos.consultor:
		empresas = Empresas.objects.filter(usuario=request.user)
		return render_to_response('empresas.html',{
		'Activar':'Configuracion','activar':'Empresas','Empresas':empresas
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def proyectoeliminar(request,id_proyecto):
	permisos = request.user.permisos
	if permisos.consultor:
		empresas = Empresas.objects.filter(usuario=request.user)
		return render_to_response('empresas.html',{
		'Activar':'Configuracion','activar':'Empresas','Empresas':empresas
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


#===============================================================================
#   Usuarios
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def usuarios(request):
	permisos = request.user.permisos
	if permisos.consultor:
		empresas = Empresas.objects.filter(usuario=request.user)
		return render_to_response('usuarios.html',{
		'Activar':'Configuracion','activar':'Usuarios','Empresas':empresas
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def usuarioeditar(request,id_usuario):
	permisos = request.user.permisos
	if permisos.consultor:
		usuarios = Empresas.objects.filter(usuario=request.user)
		return render_to_response('usuarioeditar.html',{
		'Activar':'Configuracion','activar':'Usuarios','Empresas':empresas
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def usuarioeliminar(request,id_usuario):
	permisos = request.user.permisos
	if permisos.consultor:
		usuarios = Empresas.objects.filter(usuario=request.user)
		return render_to_response('usuarios.html',{
		'Activar':'Configuracion','activar':'Usuarios','Empresas':usuarios
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def usuarionuevo(request):
	permisos = request.user.permisos
	if permisos.consultor:
		usuarios = Empresas.objects.filter(usuario=request.user)
		return render_to_response('usuarionuevo.html',{
		'Activar':'Configuracion','activar':'Usuarios','Empresas':usuarios
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')

#===============================================================================
#   Usuarios
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def licencia(request):
	permisos = request.user.permisos
	if permisos.consultor:
		empresas = Empresas.objects.filter(usuario=request.user)
		return render_to_response('licencia.html',{
		'Activar':'Configuracion','activar':'GestionarCuenta','activarp':'Licencia'
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def cuenta(request):
	acceso = None
	cambio = None
	if request.method == 'POST':
		usuario = request.user
		P = request.POST['cpassword']
		clave = request.POST['password']
		clave2 = request.POST['password2']
		acceso = authenticate(username=usuario, password=P)
		if ((acceso is not None) and (clave == clave2)):
			usuario.set_password(clave)
			usuario.save()
			cambio= "Se ha cambiado la contraseña exitosamente."
		else:
			cambio= "credenciales incorrectas, intente nuevamente."

	return render_to_response('cuenta.html',{
	'Activar':'Configuracion','activar':'GestionarCuenta','activarp':'Cuenta',
	'cambio':cambio
	}, context_instance=RequestContext(request))

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
