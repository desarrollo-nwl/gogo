#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os,django,time
import sys
sys.path.append('/home/ubuntu/gogo/')
sys.path.append('/home/ubuntu/gogo/gogo/')
sys.path.append('/home/suidi/codigo/gogo/')
sys.path.append('/home/suidi/codigo/gogo/gogo/')
os.environ["DJANGO_SETTINGS_MODULE"] ="gogo.settings"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '+xtgn6s8(15e#nv)1v5ta7n)*fpt=xq7+gt5o_28$8lzg3=ccm'
django.setup()

from colaboradores.models import *
from mensajeria.corrector import salvar_html
from mensajeria.models import *
from usuarios.strings import *
from django.db import transaction
from datetime import datetime,timedelta,date
from django.utils import timezone
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.utils
import smtplib,cgi,unicodedata
import datetime
from django.db import models

# server=smtplib.SMTP('smtp.mandrillapp.com',587)
server=smtplib.SMTP('email-smtp.us-east-1.amazonaws.com',587)
server.ehlo()
server.starttls()
# server.login('Team@goanalytics.com','pR6yG1ztNHT7xW6Y8yigfw')
server.login('AKIAIIG3SGXTWBK23VEQ','AtDj4P2QhDWTSIpkVv9ySRsz50KUFnusZ1cjFt+ZsdHC')

def sendmail(stream_i,stream,tiempo,indice):
	try:
		with transaction.atomic():
			colaborador = stream_i.colaborador
			desde="Team@goanalytics.com"
			destinatario = colaborador.email
			msg=MIMEMultipart()
			urlimg = 'http://www.changelabtools.com'+stream_i.proyecto.proyectosdatos.logo.url
			if colaborador.colaboradoresdatos.genero.lower() == "femenino" :
				genero = "a"
			else:
				genero = "o"
			nombre = (colaborador.nombre).encode("ascii", "xmlcharrefreplace")#cgi.escape(colaborador.nombre).decode("utf-8").encode("ascii", "xmlcharrefreplace")
			titulo = (stream_i.proyecto.proyectosdatos.tit_encuesta).encode("ascii", "xmlcharrefreplace")
			url = 'http://www.changelabtools.com/encuesta/'+str(stream_i.proyecto.id)+'/'+colaborador.key
			texto_correo = salvar_html(cgi.escape(stream_i.proyecto.proyectosdatos.cue_correo).encode("ascii", "xmlcharrefreplace"))
			msg["subject"]=  stream_i.proyecto.proyectosdatos.asunto
			# msg['From'] = email.utils.formataddr(((stream_i.proyecto.nombre).encode("ascii", "xmlcharrefreplace"), 'Team@goanalytics.com'))
			msg['From'] = email.utils.formataddr(((stream_i.proyecto.nombre).encode("ascii", "xmlcharrefreplace"), 'team@bigtalenter.com'))
			html = correo_standar(urlimg,genero,nombre,titulo,texto_correo,url)
			parte2=MIMEText(html,"html")
			msg.attach(parte2)
			colaborador.enviados +=1
			if( colaborador.propension == -1):
				colaborador.propension = 0
			colaborador.save()
			Streaming.objects.filter(colaborador=colaborador,proyecto=stream_i.proyecto).update(fec_controlenvio=tiempo)
			# server.sendmail('Team@goanalytics.com',destinatario,msg.as_string())
			server.sendmail('team@bigtalenter.com',destinatario,msg.as_string())
			# print 'Enviado.'
			stream_i.fec_controlenvio = tiempo
			time.sleep(.036)

		return stream
	except:
		return stream

def enviar():
	#solo postgresql soporta el distinct() de django
	tiempo = timezone.now()
	stream = Streaming.objects.select_related('colaborador__colaboradoresdatos',
			'proyecto__proyectosdatos').filter(
			fecharespuesta__isnull=True,proyecto__activo =True,
			proyecto__proyectosdatos__finicio__lte=tiempo,
			proyecto__proyectosdatos__ffin__gte=tiempo,
			colaborador__estado=True,pregunta__estado=True).distinct('colaborador')
	lens = len(stream)
	# print lens
	for i in xrange(lens):
		if not stream[i].fec_controlenvio:#no se ha enviado?
			stream = sendmail(stream[i],stream,tiempo,i)
			# print 'A:',stream[i].colaborador.email,' se le ha enviado por primera vez'
		else:
			delta = tiempo - stream[i].fec_controlenvio
			if stream[i].colaborador.propension > 0:
				propension = stream[i].colaborador.propension - 1 # nos movemos 1 hora a la derecha
				# delta2 = tiempo - Streaming.objects.only('fecharespuesta').filter(colaborador_id=stream[i].colaborador_id).latest('fecharespuesta').fecharespuesta

				if delta.days >= stream[i].proyecto.prudenciamin and (24*delta.days + delta.seconds/3600.0) >= propension:
					stream = sendmail(stream[i],stream,tiempo,i)
					delta = tiempo - stream[i].fec_controlenvio
					# print stream[i].colaborador.email,' respondio se le ha enviado nuevamente en A'

				elif delta.days >= stream[i].proyecto.prudenciamax:
					stream = sendmail(stream[i],stream,tiempo,i)
					delta = tiempo - stream[i].fec_controlenvio
					# print stream[i].colaborador.email,' respondio se le ha enviado nuevamente en B'

			elif delta.days >= stream[i].proyecto.prudenciamax: # x > M sin propension
				stream = sendmail(stream[i],stream,tiempo,i)
				delta = tiempo - stream[i].fec_controlenvio
				# print stream[i].colaborador.email,' respondio se le ha enviado nuevamente en alto lapsus'
enviar()
server.quit()
# print 'Finalizado'
