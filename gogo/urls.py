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
    url(r'^acceder/$', 'acceder'),
    url(r'^home/$', 'home'),
    url(r'^menu/(?P<id_proyecto>[0-9]{1,10})/$', 'menu'),
    url(r'^home2/$', 'home2'),
    url(r'^logs/$', 'logs'),
    url(r'^salir/$', 'salir')
)

#===============================================================================
# urls de proyectos, empresas y usuarios
#===============================================================================

urlpatterns += patterns('usuarios.views',
    url(r'^cuenta/$', 'cuenta'),
    url(r'^empresas/$', 'empresas'),
    url(r'^empresa/editar/(?P<id_empresa>[0-9]{1,10})/$', 'empresaeditar'),
    url(r'^empresa/eliminar/(?P<id_empresa>[0-9]{1,10})/$', 'empresaeliminar'),
    url(r'^empresa/nueva/$', 'empresanueva'),
    url(r'^licencia/$', 'licencia'),
    url(r'^proyecto/editar/$', 'proyectoeditar'),
    url(r'^proyecto/eliminar/$', 'proyectoeliminar'),
    url(r'^proyecto/nuevo/$', 'proyectonuevo'),
    url(r'^usuarios/$', 'usuarios'),
    url(r'^activar/([A-Za-z0-9]{1,97})','usuarioactivar'),
    url(r'^usuario/reenviar/(?P<id_usuario>[0-9]{1,10})/$','usuarioreenviar'),
    url(r'^usuario/editar/(?P<id_usuario>[0-9]{1,10})/$', 'usuarioeditar'),
    url(r'^usuario/eliminar/(?P<id_usuario>[0-9]{1,10})/$', 'usuarioeliminar'),
    url(r'^usuario/nuevo/$', 'usuarionuevo'),
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
