#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os,django
import sys
sys.path.append('/home/ubuntu/gogo/')
sys.path.append('/home/ubuntu/gogo/gogo/')
sys.path.append('/home/suidi/Documentos/gogo/')
sys.path.append('/home/suidi/Documentos/gogo/gogo/')
os.environ["DJANGO_SETTINGS_MODULE"] ="gogo.settings"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '+xtgn6s8(15e#nv)1v5ta7n)*fpt=xq7+gt5o_28$8lzg3=ccm'
django.setup()

from cuestionarios_360.models import Instrumentos_360,Dimensiones_360,Preguntas_360,Variables_360
from colaboradores_360.models import Colaboradores_360,ColaboradoresDatos_360
from colaboradores.models import Colaboradores,ColaboradoresDatos
from usuarios.models import Proyectos, Logs
from django.db import transaction
from datetime import datetime,timedelta
from django.utils import timezone
from django.db import models
from django.db.models import Q
import json

if '__main__':

	proyectos = Proyectos.objects.only('id','ciclico','ciclos')#.filter( Q(tipo = '360 redes') | Q(tipo = '360 unico') )

	for proyecto in proyectos:
		colaboradores = Colaboradores.objects.only('id').filter(proyecto_id = proyecto.id )

		col_datos = ColaboradoresDatos.objects.only('regional','ciudad','area','cargo').filter(id__in = colaboradores)

		arbol_cargos = {}
		arbol_areas = {}
		arbol_ciudades = {}
		arbol_regionales = {}

		for i in col_datos:

			try:
				if arbol_cargos[i.cargo]:
					pass
			except:
				arbol_cargos[i.cargo] = { 'regional': i.regional, 'ciudad': i.ciudad, 'area':i.area}

			try:
				if arbol_areas[i.area]:
					if i.cargo not in arbol_areas[i.area]['cargos']:
						arbol_areas[i.area]['cargos'].append(i.cargo)
			except:
				arbol_areas[i.area] = { 'regional': i.regional, 'ciudad': i.ciudad, 'cargos':[i.cargo] }

			try:
				if arbol_ciudades[i.ciudad]:
					if i.cargo not in arbol_ciudades[i.ciudad]['cargos']:
						arbol_ciudades[i.cargo]['cargos'].append(i.cargo)
					if i.area not in arbol_ciudades[i.ciudad]['areas']:
						arbol_ciudades[i.ciudad]['areas'].append(i.area)
			except:
				arbol_ciudades[i.ciudad] = { 'regional': i.regional, 'areas': [i.area], 'cargos':[i.cargo] }

			try:
				if arbol_regionales[i.regional]:
					if i.cidudad not in arbol_regionales[i.regional]['ciudades']:
						arbol_regionales[i.regional]['ciudades'].append(i.ciudad)
					if i.area not in arbol_regionales[i.regional]['areas']:
						arbol_regionales[i.regional]['areas'].append(i.area)
					if i.cargo not in arbol_regionales[i.regional]['cargos']:
						arbol_regionales[i.regional]['cargos'].append(i.cargo)
			except:
				arbol_regionales[i.regional] = { 'ciudades':[i.ciudad], 'areas':[i.area], 'cargo':[i.cargo] }

		print json.dumps(arbol_regionales,ensure_ascii = False)
		print json.dumps(arbol_ciudades,ensure_ascii = False)
		print json.dumps(arbol_areas,ensure_ascii = False)
		print json.dumps(arbol_cargos,ensure_ascii = False)
		break
