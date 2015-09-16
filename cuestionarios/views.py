from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.cache import cache
# from django.db import connection
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_control
from cuestionarios.models import *

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
