import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '+xtgn6s8(15e#nv)1v5ta7n)*fpt=xq7+gt5o_28$8lzg3=ccm'
DEBUG = False
INSTALLED_APPS = (
	'analisis',
	'colaboradores',
	'cuestionarios',
	'mensajeria',
	'usuarios',
	'mptt',
)
DATABASES = {
	'default': {
			'ENGINE':'django.db.backends.sqlite3',
			'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
			# 'ENGINE': 'django.db.backends.mysql',
			# 'NAME': 'gogo',
			# 'USER': 'suidi',
			# 'PASSWORD':'Su1357*-',
			# 'HOST':'nwl.co3mxnuop6eu.us-east-1.rds.amazonaws.com',
			# 'PORT':'3306',
	}
}
LANGUAGE_CODE = 'es-CO'
TIME_ZONE = 'America/Bogota'
USE_TZ = True

import sys
sys.path.append('/home/suidi/codigo/gogo/')
sys.path.append('/home/suidi/codigo/gogo/gogo/')
from mensajeria.models import *

for i in Streaming.objects.all():
    print i.colaborador, i.pregunta ,i.colaborador.email, i.proyecto.prudenciamin
