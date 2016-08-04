# -*- encoding: utf-8 -*-
from colaboradores_360.models import *
from cuestionarios_360.models import *
from datetime import datetime as DT
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.cache import cache
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.views.decorators.cache import cache_control
from mensajeria_360.models import Streaming_360
from usuarios.models import Proyectos
from redes_360.models import Redes_360
from analisis_360.models import *


# ==============================================================================
# 		pantalla inicial
# ==============================================================================


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def participacion_360(request):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa"] :
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.res_see:

		try:
			participacion = Participacion_360.objects.get(id_id=proyecto.id)
		except:
			participacion = []

		return render_to_response('participacion_360.html',{
		'Activar':'Contenido','activar':'Individual',
		'Proyecto':proyecto,'Permisos':permisos,'Participacion':participacion
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')
