#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import time
import django
import sys
import ujson
sys.path.append('/home/webapps/gogo/')
sys.path.append('/home/webapps/gogo/gogo/')
# sys.path.append('/home/suidi/Documentos/gogo/')
# sys.path.append('/home/suidi/Documentos/gogo/gogo/')
os.environ["DJANGO_SETTINGS_MODULE"] = "gogo.settings"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '+xtgn6s8(15e#nv)1v5ta7n)*fpt=xq7+gt5o_28$8lzg3=ccm'
django.setup()

import sendgrid
from sendgrid.helpers.mail import *

from colaboradores.models import *
from mensajeria.corrector import salvar_html
from mensajeria.models import *
from usuarios.strings import *

from colaboradores_360.models import *
from mensajeria_360.models import *

from django.db import transaction
from datetime import datetime, timedelta, date
from django.utils import timezone
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.utils
import smtplib,cgi,unicodedata
import datetime
from django.db import models



# server=smtplib.SMTP('email-smtp.us-east-1.amazonaws.com',587)
# server.ehlo()
# server.starttls()
# server.login('AKIAIIG3SGXTWBK23VEQ','AtDj4P2QhDWTSIpkVv9ySRsz50KUFnusZ1cjFt+ZsdHC')

sg = sendgrid.SendGridAPIClient(apikey='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')


def sendmail(stream_i, stream, tiempo, indice):
    try:
        with transaction.atomic():
            colaborador = stream_i.colaborador
            desde="Team@goanalytics.com"
            destinatario = colaborador.email
            msg=MIMEMultipart()
            urlimg = 'http://159.203.190.248'+stream_i.proyecto.proyectosdatos.logo.url
            if colaborador.colaboradoresdatos.genero.lower() == "femenino" :
                genero = "a"
            else:
                genero = "o"
            nombre = (colaborador.nombre).encode("ascii", "xmlcharrefreplace")#cgi.escape(colaborador.nombre).decode("utf-8").encode("ascii", "xmlcharrefreplace")
            titulo = (stream_i.proyecto.proyectosdatos.tit_encuesta).encode("ascii", "xmlcharrefreplace")
            url = 'http://159.203.190.248/encuesta/'+str(stream_i.proyecto.id)+'/'+colaborador.key
            texto_correo = salvar_html(cgi.escape(stream_i.proyecto.proyectosdatos.cue_correo).encode("ascii", "xmlcharrefreplace"))
            msg["subject"]=  stream_i.proyecto.proyectosdatos.asunto
            msg['From'] = email.utils.formataddr(((stream_i.proyecto.nombre).encode("ascii", "xmlcharrefreplace"), 'team@bigtalenter.com'))
            html = correo_standar(urlimg,genero,nombre,titulo,texto_correo,url)
            parte2=MIMEText(html,"html")
            msg.attach(parte2)
            colaborador.enviados +=1
            if( colaborador.propension == -1):
                colaborador.propension = 0
            colaborador.save()
            Streaming.objects.filter(colaborador=colaborador,proyecto=stream_i.proyecto).update(fec_controlenvio=tiempo)

            # server.sendmail('team@bigtalenter.com',destinatario,msg.as_string())
            content = Content("text/html", html)
            print '####################################################################'
            mail = Mail(Email('team@bigtalenter.com'), msg["subject"], Email(destinatario), content)
            mail.set_template_id('09dd518c-04a1-45e1-8fea-b635274a02e2')
            response = sg.client.mail.send.post(request_body=mail.get())
            print response
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


# ==============================================================================
# Involucro el algoritmo de envio 360 en el mismo script para serializar el envio
# ==============================================================================

def sendmail_360(stream_i,stream,tiempo,indice):
    # try:
    with transaction.atomic():
        colaborador = stream_i.colaborador
        col_met = colaborador.colaboradoresmetricas_360

        red = col_met.ins_actual
        reds = ujson.loads(col_met.ord_instrumentos)

        if not red or reds.index(red) == (len(reds)-1):
            print "ENTRAMOS"
            if proyecto.tipo == "360 redes":
                red = reds[0]
        else:
            red = reds[ reds.index(red) +1 ]
        red = Redes_360.objects.only('evaluado__nombre','evaluado__apellido','rol'
                                        ).select_related('evaluado').filter(id = red )[0]
        desde="Team@goanalytics.com"
        destinatario = colaborador.email
        msg=MIMEMultipart()
        urlimg = 'http://159.203.190.248'+stream_i.proyecto.proyectosdatos.logo.url
        if colaborador.genero.lower() == "femenino" :
            genero = "a"
        else:
            genero = "o"
        # nombre = (colaborador.nombre).encode("ascii", "xmlcharrefreplace")#cgi.escape(colaborador.nombre).decode("utf-8").encode("ascii", "xmlcharrefreplace")
        nombre = (colaborador.nombre+' estas evaluando a ' +'<strong>'+red.evaluado.nombre+ '</strong>'+' con el rol '+'<strong>'+red.rol+'</strong>').encode("ascii", "xmlcharrefreplace")
        titulo = (stream_i.proyecto.proyectosdatos.tit_encuesta).encode("ascii", "xmlcharrefreplace")
        url = 'http://159.203.190.248/360/encuesta/'+str(stream_i.proyecto.id)+'/'+colaborador.key
        texto_correo = salvar_html(cgi.escape(stream_i.proyecto.proyectosdatos.cue_correo).encode("ascii", "xmlcharrefreplace"))
        msg["subject"]=  stream_i.proyecto.proyectosdatos.asunto
        msg['From'] = email.utils.formataddr(((stream_i.proyecto.nombre).encode("ascii", "xmlcharrefreplace"), 'team@bigtalenter.com'))
        html = correo_standar(urlimg,genero,nombre,titulo,texto_correo,url)
        parte2=MIMEText(html,"html")
        msg.attach(parte2)
        colaborador.enviados +=1
        if( colaborador.propension == -1):
            colaborador.propension = 0
        colaborador.save()
        Streaming_360.objects.filter(colaborador=colaborador,proyecto=stream_i.proyecto).update(fec_controlenvio=tiempo)
        # server.sendmail('team@bigtalenter.com',destinatario,msg.as_string())
        content = Content("text/html", html)
        print '####################################################################'
        mail = Mail(Email('team@bigtalenter.com'), msg["subject"], Email(destinatario), content)
        mail.set_template_id('09dd518c-04a1-45e1-8fea-b635274a02e2')
        response = sg.client.mail.send.post(request_body=mail.get())
        print response
        stream_i.fec_controlenvio = tiempo
        time.sleep(.036)

    return stream
    # except:
    #   return stream

def enviar_360():
    #solo postgresql soporta el distinct() de django
    tiempo = timezone.now()
    stream = Streaming_360.objects.select_related('proyecto__proyectosdatos').filter(
            fecharespuesta__isnull=True,proyecto__activo =True,
            proyecto__proyectosdatos__finicio__lte=tiempo,
            proyecto__proyectosdatos__ffin__gte=tiempo,
            colaborador__estado=True,pregunta__estado=True).distinct('colaborador')
    lens = len(stream)
    print '#############################################'
    print lens
    for i in xrange(lens):
        if not stream[i].fec_controlenvio:#no se ha enviado?
            stream = sendmail_360(stream[i],stream,tiempo,i)
            print 'A:',stream[i].colaborador.email,' se le ha enviado por primera vez'
        else:
            delta = tiempo - stream[i].fec_controlenvio
            print 'DELTAAAAA'
            print delta
            if stream[i].colaborador.propension > 0:
                print 'ENTRO AL 1ER IFFFFFFFFFFFFFFFFFFF'
                propension = stream[i].colaborador.propension - 1 # nos movemos 1 hora a la derecha
                # delta2 = tiempo - Streaming.objects.only('fecharespuesta').filter(colaborador_id=stream[i].colaborador_id).latest('fecharespuesta').fecharespuesta

                if delta.days >= stream[i].proyecto.prudenciamin and (24*delta.days + delta.seconds/3600.0) >= propension:
                    print 'ENTRO AL 2DO IFFFFFFFFFFFFFFFFFFF'
                    stream = sendmail_360(stream[i],stream,tiempo,i)
                    delta = tiempo - stream[i].fec_controlenvio
                    print stream[i].colaborador.email,' respondio se le ha enviado nuevamente en A'

                elif delta.days >= stream[i].proyecto.prudenciamax:
                    print 'ENTRO AL ELIF DEL 2DO IFFFFFFFFFFFFFFFFFFF'
                    stream = sendmail_360(stream[i],stream,tiempo,i)
                    delta = tiempo - stream[i].fec_controlenvio
                    print stream[i].colaborador.email,' respondio se le ha enviado nuevamente en B'

            elif delta.days >= stream[i].proyecto.prudenciamax: # x > M sin propension
                print 'ENTRO AL ELIF DEL 1ER IFFFFFFFFFFFFFFFFFFF'
                stream = sendmail_360(stream[i],stream,tiempo,i)
                delta = tiempo - stream[i].fec_controlenvio
                print stream[i].colaborador.email,' respondio se le ha enviado nuevamente en alto lapsus'

enviar()
enviar_360()
server.quit()
# print 'Finalizado'
