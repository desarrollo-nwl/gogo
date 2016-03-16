#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os,django
import sys
sys.path.append('/home/ubuntu/gogo/')
sys.path.append('/home/ubuntu/gogo/gogo/')
sys.path.append('/home/suidi/workspace/gogo/')
sys.path.append('/home/suidi/workspace/gogo/gogo/')
os.environ["DJANGO_SETTINGS_MODULE"] ="gogo.settings"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '+xtgn6s8(15e#nv)1v5ta7n)*fpt=xq7+gt5o_28$8lzg3=ccm'
django.setup()

from colaboradores.models import Colaboradores
from cuestionarios.models import Preguntas,Variables
from cuestionarios_360.models import Instrumentos_360,Dimensiones_360,Preguntas_360,Variables_360
from usuarios.models import Proyectos
from django.db import transaction
from datetime import datetime,timedelta
from django.utils import timezone
from django.db import models

if '__main__':
	antiguo = timezone.now()# - timedelta(61)
	Colaboradores.objects.filter(zdel__lt = antiguo).delete()
	Variables.objects.filter(zdel__lt = antiguo).delete()
	Preguntas.objects.filter(zdel__lt = antiguo).delete()
	Proyectos.objects.filter(zdel__lt = antiguo).delete()
	# Colaboradores.objects.filter(zdel__lt = antiguo).delete()
	Instrumentos_360.objects.filter(zdel__lt = antiguo).delete()
	Dimensiones_360.objects.filter(zdel__lt = antiguo).delete()
	Variables_360.objects.filter(zdel__lt = antiguo).delete()
	Preguntas_360.objects.filter(zdel__lt = antiguo).delete()
