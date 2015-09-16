from django.conf import settings
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf.urls import handler400,handler403,handler404, handler500
from usuarios.views import e400,e403,e404,e500

#===============================================================================
# urls de usuarios y varias
#===============================================================================
urlpatterns = patterns('usuarios.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'index', name='index'),
    url(r'^index/$', 'index'),
    url(r'^home/$', 'home'),
    url(r'^acceder/$', 'acceder'),
    url(r'^salir/$', 'salir'),
    url(r'^menu/$', 'menu'),
    url(r'^menu2/(?P<id_proyecto>[0-9]{1,10})/$', 'menu2'),

)

#===============================================================================
# urls de errores
#===============================================================================
handler400 = e400
handler403 = e403
handler404 = e404
handler500 = e500

#===============================================================================
# urls de media en modo debug
#===============================================================================
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT,}),
	)
