# -*- encoding: utf-8 -*-
from django.shortcuts import render
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

# Create your views here.


def planesAccion(request):
    return render_to_response('planesAccion.html',{
        'Activar':'Contenido','activar':'Instrumentos',
        },context_instance=RequestContext(request))

def puntosTalenter(request):
    return render_to_response('puntosTalenter.html',{
        'Activar':'Contenido','activar':'Instrumentos',
        },context_instance=RequestContext(request))

def miLiderazgo(request):
    return render_to_response('miLiderazgo.html',{
        'Activar':'Contenido','activar':'Instrumentos',
        },context_instance=RequestContext(request))

def dashBoard(request):
    return render_to_response('dashBoard.html',{
        'Activar':'Contenido','activar':'Instrumentos',
        },context_instance=RequestContext(request))
