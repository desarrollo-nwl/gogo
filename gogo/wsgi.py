import os
import sys
os.environ["DJANGO_SETTINGS_MODULE"] ="gogo.settings"
os.environ['HTTPS'] = "on"
os.environ['wsgi.url_scheme'] = 'https'
sys.path.append('/home/ubuntu/gogo/')
sys.path.append('/home/ubuntu/gogo/gogo/')
sys.path.append('/home/ubuntu/gogo/static/')
sys.path.append('/home/ubuntu/gogo/media/')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
