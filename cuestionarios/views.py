# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.cache import cache
# from django.db import connection
from cuestionarios.models import *
from django.db import IntegrityError, transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_control
from usuarios.models import Empresas, Proyectos
#===============================================================================
# vistas de edicion de preguntas y variables
#===============================================================================

@cache_control(no_store=True,no_cache=True,must_revalite=True)
@login_required(login_url='/acceder/')
def biblio(request):
    permisos = request.user.permisos
    if permisos.consultor:
    	biblio = Bibliotecas.objects.all()
    	return render_to_response('biblio.html',{
    	'activarG':'1','activar':'biblio','Biblio':biblio,
    	}, context_instance=RequestContext(request))
    else:
        return render_to_response('403.html')

#===============================================================================
# indices
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def indicevariables(request):
    proyecto = cache.get(request.user.username)
    permisos = request.user.permisos
    if permisos.consultor and permisos.var_see:
        variables = proyecto.variables_set.all()
        return render_to_response('varadd.html',{
    	'activarG':'1','activar':'biblio'
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
def nuevoproyecto(request):
    permisos = request.user.permisos
    if permisos.consultor and permisos.pro_add:
        empresas = Empresas.objects.filter( usuario = request.user )
        usuarios = request.user.IndiceUsuarios.get_descendants(include_self=False)
		if request.method == 'POST':
            empresa = Empresas.objects.get(id = int(request.POST['empresa']))
            if(int(request.POST['prudenciamin']) < int(request.POST['prudenciamax'])):
                prudenciamax = int(request.POST['prudenciamax'])
                prudenciamin = int(request.POST['prudenciamin'])
            else:
                if(int(request.POST['prudenciamin']) == int(request.POST['prudenciamax'])):
                    prudenciamin = int(request.POST['prudenciamin'])
                    prudenciamax = int(request.POST['prudenciamax'])+1
                else:
                    prudenciamax = int(request.POST['prudenciamin'])
                    prudenciamin = int(request.POST['prudenciamax'])
            try:
                with transaction.atomic():
        			proyecto = Proyectos.objects.create(
                    	can_envio = request.POST['can_envio'],
                    	descripcion = request.POST['descripcion'],
                    	empresa = empresa,
                    	nombre =  request.POST['nombre'],
                    	prudenciamax = prudenciamax,
                    	prudenciamin = prudenciamax)
                    datos = ProyectosDatos(
                        id = proyecto,
                        cue_correo = request.POST['cue_correo'],
                        tit_encuesta = request.POST['tit_encuesta'],
                        int_encuesta = request.POST['int_encuesta'],
                        logo = request.FILES['logo'],
                        tipo = request.POST['tipo'])
                    if(request.POST['senso'])
                        proyecto.senso = bool(int(request.POST['senso']))
                    if(request.FILES['logoenc']):
                        proyecto.logoenc = request.FILES['logoenc']
                    datos.save()
                    asociados = request.POST.getlist('asociados')
                    for i in usuarios:
                        if( str(i.id) in asociados): ###validar metodo
                            proyecto.usuarios.add(i)
            except IntegrityError:
                handle_exception()
            cache.set(request.user.username,proyecto,86400)
			return HttpResponseRedirect('/cuestionario/nueva/variable/')
    	return render_to_response('create1.html',{
    	'activarG':'1','activar':'biblio'
    	}, context_instance=RequestContext(request))
    else:
        return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def nuevavariable(request):
    proyecto = cache.get(request.user.username)
    permisos = request.user.permisos
    if permisos.consultor and permisos.var_add:
		if request.method == 'POST':
			variable = Variables(
                        nombre = request.POST['nombre'],
                        posicion = request.POST['posicion'],
                        proyecto = proyecto)
            if(request.POST['descripcion']):
                variable.descripcion = request.POST['descripcion']
            variable.save()
            proyecto.max_variables += 1
            proyecto.save()
            cache.set(request.user.username,proyecto,86400)
            if(proyecto.max_variables == 1 ):
                return HttpResponseRedirect('/cuestionario/nueva/pregunta/')
            else:
                return HttpResponseRedirect('/cuestionario/variables/')
        return render_to_response('varadd.html',{
    	'activarG':'1','activar':'biblio',
    	}, context_instance=RequestContext(request))
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
def editarproyecto(request):
    permisos = request.user.permisos
    proyecto = cache.get(request.user.username)
    if permisos.consultor and permisos.pro_edit:
        asociados = proyecto.usuarios.all()
        datos = proyecto.proyectosdatos
        empresas = Empresas.objects.filter( usuario = request.user )
        usuarios = request.user.IndiceUsuarios.get_descendants(include_self=False)
		if request.method == 'POST':
            empresa = Empresas.objects.filter(id = int(request.POST['empresa']))
            if(int(request.POST['prudenciamin']) < int(request.POST['prudenciamax'])):
                prudenciamax = int(request.POST['prudenciamax'])
                prudenciamin = int(request.POST['prudenciamin'])
            else:
                if(int(request.POST['prudenciamin']) == int(request.POST['prudenciamax'])):
                    prudenciamin = int(request.POST['prudenciamin'])
                    prudenciamax = int(request.POST['prudenciamax'])+1
                else:
                    prudenciamax = int(request.POST['prudenciamin'])
                    prudenciamin = int(request.POST['prudenciamax'])
            try:
                with transaction.atomic():
                    proyecto.can_envio = request.POST['can_envio']
                    proyecto.descripcion = request.POST['descripcion']
                    proyecto.empresa = empresa
                    proyecto.nombre =  request.POST['nombre']
                    proyecto.prudenciamax = prudenciamax
                    proyecto.prudenciamin = prudenciamin
                    proyecto.save()
                    datos.id = proyecto
                    datos.cue_correo = request.POST['cue_correo']
                    datos.tit_encuesta = request.POST['tit_encuesta']
                    datos.int_encuesta = request.POST['int_encuesta']
                    datos.tipo = request.POST['tipo'])
                    if(request.POST['senso'])
                        datos.senso = bool(int(request.POST['senso']))
                    if(request.FILES['logo']):
                        import os
                        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                        try:
        					command = 'rm '+BASE_DIR+'/media/%s' %(pro.logo) ###validar ruta
        					os.system(command)
                        except:pass
                        datos.logo = request.FILES['logo']
                    if(request.FILES['logoenc']):
                        try:
        					command = 'rm '+BASE_DIR+'/media/%s' %(pro.logoenc) ###validar ruta
        					os.system(command)
                        except:pass
                        datos.logoenc = request.FILES['logoenc']
                    datos.save()
                    nuevos_asociados = request.POST.getlist('asociados')
                    for i in usuarios:
                        if( str(i.id) in nuevos_asociados): ###validar metodo
                            proyecto.usuarios.add(i)
                        else:
                            proyecto.usuarios.remove(i)
            except IntegrityError:
                handle_exception()
            cache.set(request.user.username,proyecto,86400)
			return HttpResponseRedirect('/home/')
    	return render_to_response('create1.html',{
    	'activarG':'1','activar':'biblio'
    	}, context_instance=RequestContext(request))
    else:
        return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def editarvariable(request,id_variable):
    proyecto = cache.get(request.user.username)
    permisos = request.user.permisos
    if permisos.consultor and permisos.var_edit:
        variable = Variables.objects.get(id=int(id_variable))
		if request.method == 'POST':
            variable.nombre = request.POST['nombre']
            variable.posicion = request.POST['posicion']
            variable.proyecto = proyecto
            if(request.POST['descripcion']):
                variable.descripcion = request.POST['descripcion']
            variable.save()
            return HttpResponseRedirect('/cuestionario/variables/')
        return render_to_response('varadd.html',{
    	'activarG':'1','activar':'biblio',
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
        ori_proyecto = Proyectos.objects.get(int(id_proyecto))
        asociados = ori_proyecto.usuarios.all()
        datos = ori_proyecto.proyectosdatos
        empresas = Empresas.objects.filter( usuario = request.user )
        usuarios = request.user.IndiceUsuarios.get_descendants(include_self=False)
		if request.method == 'POST':
            empresa = Empresas.objects.get(id = int(request.POST['empresa']))
            if(int(request.POST['prudenciamin']) < int(request.POST['prudenciamax'])):
                prudenciamax = int(request.POST['prudenciamax'])
                prudenciamin = int(request.POST['prudenciamin'])
            else:
                if(int(request.POST['prudenciamin']) == int(request.POST['prudenciamax'])):
                    prudenciamin = int(request.POST['prudenciamin'])
                    prudenciamax = int(request.POST['prudenciamax'])+1
                else:
                    prudenciamax = int(request.POST['prudenciamin'])
                    prudenciamin = int(request.POST['prudenciamax'])
            try:
                with transaction.atomic():
        			proyecto = Proyectos.objects.create(
                    	can_envio = request.POST['can_envio'],
                    	descripcion = request.POST['descripcion'],
                    	empresa = empresa,
                    	nombre =  request.POST['nombre'],
                    	prudenciamax = prudenciamax,
                    	prudenciamin = prudenciamax)
                    datos = ProyectosDatos(
                        id = proyecto,
                        cue_correo = request.POST['cue_correo'],
                        tit_encuesta = request.POST['tit_encuesta'],
                        int_encuesta = request.POST['int_encuesta'],
                        logo = request.FILES['logo'],
                        tipo = request.POST['tipo'])
                    if(request.POST['senso'])
                        proyecto.senso = bool(int(request.POST['senso']))
                    if(request.FILES['logoenc']):
                        proyecto.logoenc = request.FILES['logoenc']
                    datos.save()
                    asociados = request.POST.getlist('asociados')
                    for i in usuarios:
                        if( str(i.id) in asociados): ###validar metodo
                            proyecto.usuarios.add(i)
                    variables = Variables.objects.filter(proyecto=ori_proyecto
                                ).prefetch_related('preguntas_set__respuestas_set')
                    variables_nuevas = []
                    preguntas_nuevas = []
                    respuestas_nuevas = []
                    for i in variables:
                        i.id = None
                        i.proyecto = proyecto
                        variables_nuevas.append(i)
                        for j in i.preguntas_set.all():
                            j.id = None
                            j.variable = i
                            preguntas_nuevas.append(j)
                            for k in j.respuestas_set.all():
                                k.id = None
                                k.pregunta = j
                                respuestas_nuevas.append(k)
                    Variables.objects.bulk_create(variables_nuevas)
                    Preguntas.objects.bulk_create(preguntas_nuevas)
                    Respuestas.objects.bulk_create(respuestas_nuevas)
            except IntegrityError:
                handle_exception()
            # cache.set(request.user.username,proyecto,86400)
			return HttpResponseRedirect('/menu/') ###validar redireccionamiento
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
                    ).select_related('proyecto__max_variables')
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
def eliminarproyecto(request):
    proyecto = cache.get(request.user.username)
    permisos = request.user.permisos
    if permisos.consultor and permisos.pro_del:
        if request.method == 'POST':
            proyecto.usuarios.clear()
            return HttpResponseRedirect('/menu/')
        return render_to_response('cue_eliminar.html',{
    	'activarG':'1','activar':'biblio'
    	}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def eliminarvariable(request,id_variable):
    proyecto = cache.get(request.user.username)
    permisos = request.user.permisos
    if permisos.consultor and permisos.var_del:
        if request.method == 'POST':
            Variables.objects.filter(id=1).update(proyecto_id=1)
            return HttpResponseRedirect('/cuestionario/variables/')
    return render_to_response('cue_eliminar.html',{
	'activarG':'1','activar':'biblio'
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
