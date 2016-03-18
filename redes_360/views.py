# -*- encoding: utf-8 -*-
from colaboradores_360.models import Colaboradores_360, Roles_360
from cuestionarios_360.models import Instrumentos_360
from redes_360.models import Redes_360
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import transaction
from django.db.models import F
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_control
from mensajeria_360.models import Streaming_360
from usuarios.models import Proyectos, Logs
import random
import redes as redes_cpp

#===============================================================================
# indices
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def redes_360(request):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"] :
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.red_see:
		redes = Redes_360.objects.only(
				'colaborador__nombre','colaborador__apellido','rol_idn',
				'evaluado__nombre','evaluado__apellido','instrumento__nombre'
				).filter(proyecto_id = proyecto.id
				).select_related('colaborador','instrumento')
		roles = Roles_360.objects.filter(proyecto_id=proyecto.id)
		instrumentos = Instrumentos_360.objects.only('nombre').filter(proyecto_id=proyecto.id)
		personas = redes_cpp.ver_personas(str(proyecto.id))
		return render_to_response('redes_ind.html',{
		'Activar':'Contenido','activar':'RedesIndividual',
		'Proyecto':proyecto,'Permisos':permisos,
		'Personas':personas,'Roles':roles,'Instrumentos':instrumentos,
		'Redes':redes
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def rednueva_360(request):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"] :
		return render_to_response('423.html')
	permisos = request.user.permisos
	if all([permisos.consultor, permisos.red_add]):
		if request.method == 'POST':
			if not Redes_360.objects.filter(
				colaborador_id=request.POST['colaborador'],
				evaluado_id=request.POST['evaluado'],
				proyecto_id=proyecto.id).exists():
				print 'rol',request.POST['rol']
				rol = Roles_360.objects.filter(proyecto_id=proyecto.id).get(id=request.POST['rol'])

				red = Redes_360.objects.create(
					colaborador_id=request.POST['colaborador'],
					evaluado_id=request.POST['evaluado'],
					instrumento_id=request.POST['instrumento'],
					rol_idn = request.POST['rol'],
					rol = rol.nombre,
					proyecto_id=proyecto.id)
				print 'rrol',red
				red = Redes_360.objects.only(
						'colaborador__nombre','colaborador__apellido','instrumento__nombre'
						'evaluador__nombre','evaluador__apellido','rol','rol_idn'
						).filter(id=red.id).select_related(
						'colaborador','evaluado','instrumento')
				return JsonResponse({
							'id':red.id,
							'col_nombre':red.colaborador.nombre,
							'col_apellido':red.colaborador.apellido,
							'eva_nombre':red.evaluador.nombre,
							'eva_apellido':red.evaluador.apellido,
							'rol':red.rol,
							'rol_idn':red.rol_idn,
							'estado':1})
		return render_to_response('403.html')
	else:
		return render_to_response('403.html')
