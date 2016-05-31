# -*- encoding: utf-8 -*-
from datetime import datetime
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
import ujson
# Create your views here.

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def cuerpoHumano(request):
    return render_to_response('cuerpoHumano.html',{'Activar':'Contenido','activar':'Instrumentos',},context_instance=RequestContext(request))
