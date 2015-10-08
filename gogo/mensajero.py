#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '+xtgn6s8(15e#nv)1v5ta7n)*fpt=xq7+gt5o_28$8lzg3=ccm'
DEBUG = False
INSTALLED_APPS = ('analisis','colaboradores','cuestionarios','mensajeria','usuarios','mptt',)
DATABASES = {'default': {'ENGINE': 'django.db.backends.mysql','NAME': 'gogo','USER': 'suidi','PASSWORD':'Su1357*-','HOST':'nwl.co3mxnuop6eu.us-east-1.rds.amazonaws.com','PORT':'3306'}}
LANGUAGE_CODE = 'es-CO'
TIME_ZONE = 'America/Bogota'
USE_TZ = True
import sys
sys.path.append('/home/suidi/codigo/gogo/')
sys.path.append('/home/suidi/codigo/gogo/gogo/')

from colaboladores.models import *
from corrector import tildes,tildes2
from mensajeria.models import *
from usuarios.strings import *

from datetime import datetime,timedelta
from django.utils import timezone
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.utils
import smtplib

server=smtplib.SMTP('smtp.mandrillapp.com',587)
server.ehlo()
server.starttls()
server.login('Team@goanalytics.com','pR6yG1ztNHT7xW6Y8yigfw')

def sendmail(stream_i):
	# try
	desde="Team@goanalytics.com"
	destinatario = stream_i.colaborador.email
	url = 'http://www.lavozdemisclientes.com/encuesta/'+str(stream_i.proyecto.id)+'/'+stream_i.colaborador.key
	msg=MIMEMultipart()
	urlimg = 'http://www.lavozdemisclientes.com'+stream_i.proyecto.proyectosdatos.logo.url
	cuerpo_correo = tildes(stream_i.proyecto.proyectosdatos.cue_correo)
	Nombre = tildes(stream_i.colaborador.nombre)
	msg["subject"]=  tildes2(stream_i.proyecto.tit_encuesta)
	msg['To'] = email.utils.formataddr(('Respetado (a)', destinatario))
	msg['From'] = email.utils.formataddr(('GoAnalitycs', 'Team@goanalytics.com'))
	html = correo_standar(urlimg,nombre,titulo,texto_correo,url)
	parte2=MIMEText(html,"html")
	msg.attach(parte2)
	server.sendmail('Team@goanalytics.com',D,msg.as_string())
	print 'Enviando.'
	# except:
	# 	pass

def actualizar(i,stream,tiempo):
	for j in stream:
		if j.colaborador_id == i.colaborador_id:
			j.fec_controlenvio = tiempo
	Streaming.objects.filter(colaborador=i.colaborador,proyecto=i.proyecto).update(fec_controlenvio=tiempo)
	return stream

def enviar():
	stream = Streaming.objects.select_related('colaborador','proyecto__proyectosdatos'
		).filter(fecharespuesta__isnull=True)
	lens = stream = Streaming.objects.only('id').filter(fecharespuesta__isnull=True).count()
	tiempo = timezone.now()
	for i in xrange(lens):
		if not stream[i].fec_controlenvio:#no se ha enviado?
			if stream[i].proyecto.activo:#El proyecto esta activo?
				if stream[i].pregunta.estado:#La pregunta esta activa para este proyecto?
					sendmail(i.colaborador.email)
					actualizar(stream(i),stream,tiempo)
					print 'A:',i.colaborador.email,' se le ha enviado por primera vez'

		elif stream[i].proyecto.activo:#El proyecto esta activo?
			if stream[i].pregunta.estado:#La pregunta esta activa para este proyecto?
				delta = tiempo - stream[i].fec_controlenvio
				if stream[i].colaborador.propension:
					propension = stream[i].colaborador.propension - 0.83 #calibrador para que no se mueva a derecha
					if ( delta.days >= stream[i].proyecto.prudenciamin and delta.days >= propension ):  # x > p > m
						sendmail(stream[i])
						stream = actualizar(stream[i],stream,tiempo)
						print stream[i].colaborador.email,' respondio se le ha enviado nuevamente'
					elif ( delta.days <= stream[i].proyecto.prudenciamax and delta.days >= propension ): # M > x > p
						sendmail(stream[i])
						stream = actualizar(stream[i],stream,tiempo)
						print stream[i].colaborador.email,' respondio se le ha enviado nuevamente'
					elif delta.days >= stream[i].proyecto.prudenciamax: # x > M con propension
						sendmail(stream[i])
						stream = actualizar(stream[i],stream,tiempo)
						print stream[i].colaborador.email,' respondio se le ha enviado nuevamente'
				elif delta.days >= stream[i].proyecto.prudenciamax: # x > M sin propension
						sendmail(stream[i])
						stream = actualizar(stream[i],stream,tiempo)
						print stream[i].colaborador.email,' respondio se le ha enviado nuevamente'
enviar()
server.quit()
print 'Finalizado'
