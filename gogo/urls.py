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
	url(r'^recuperar/$', 'recuperar'),
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
	url(r'^proyecto/editar/(?P<id_proyecto>[0-9]{1,10})/$', 'proyectoeditar'),
	url(r'^proyecto/eliminar/(?P<id_proyecto>[0-9]{1,10})/$', 'proyectoeliminar'),
	url(r'^proyecto/nuevo/$', 'proyectonuevo'),
	url(r'^usuarios/$', 'usuarios'),
	url(r'^activar/([A-Za-z0-9]{1,97})','usuarioactivar'),
	url(r'^recuperar/([A-Za-z0-9]{1,97})','usuariorecuperar'),
	url(r'^usuario/reenviar/(?P<id_usuario>[0-9]{1,10})/$','usuarioreenviar'),
	url(r'^usuario/editar/(?P<id_usuario>[0-9]{1,10})/$', 'usuarioeditar'),
	url(r'^usuario/eliminar/(?P<id_usuario>[0-9]{1,10})/$', 'usuarioeliminar'),
	url(r'^usuario/nuevo/$', 'usuarionuevo'),
)

#===============================================================================
# urls de cuestionarios
#===============================================================================

urlpatterns += patterns('cuestionarios.views',
	url(r'^pregunta/activar/(?P<id_pregunta>[0-9]{1,10})/$', 'preguntactivar'),
	url(r'^variable/(?P<id_variable>[0-9]{1,10})/preguntas/$', 'preguntas'),
	url(r'^variable/(?P<id_variable>[0-9]{1,10})/pregunta/nueva/$', 'preguntanueva'),
	url(r'^pregunta/(?P<id_pregunta>[0-9]{1,10})/$', 'preguntaeditar'),
	url(r'^pregunta/clonar/(?P<id_pregunta>[0-9]{1,10})/$', 'preguntaclonar'),
	url(r'^pregunta/eliminar/(?P<id_pregunta>[0-9]{1,10})/$', 'preguntaeliminar'),
	url(r'^variables/$', 'variables'),
	url(r'^variable/nueva/$', 'variablenueva'),
	url(r'^variable/clonar/(?P<id_variable>[0-9]{1,10})/$', 'variableclonar'),
	url(r'^variable/editar/(?P<id_variable>[0-9]{1,10})/$', 'variableditar'),
	url(r'^variable/eliminar/(?P<id_variable>[0-9]{1,10})/$', 'variableliminar'),
	url(r'^variable/activar/(?P<id_variable>[0-9]{1,10})/$', 'variableactivar'),
	url(r'^proyecto/clonar/(?P<id_proyecto>[0-9]{1,10})/$', 'proyectoclonar'),
)

#===============================================================================
# urls de errores
#===============================================================================

urlpatterns += patterns('colaboradores.views',
	url(r'^participante/eliminar/(?P<id_colaborador>[0-9]{1,10})/$', 'colaboradoreliminar'),
	url(r'^participantes/individual/$', 'colaboradores_ind'),
	url(r'^participantes/archivo/$', 'colaboradores_xls'),
	url(r'^participante/nuevo/$', 'colaboradornuevo'),
	url(r'^participante/editar/(?P<id_colaborador>[0-9]{1,10})/$', 'colaboradoreditar'),
	url(r'^participante/activar/(?P<id_colaborador>[0-9]{1,10})/$', 'colaboradoractivar'),
	url(r'^archivo/$', 'archivo'),

)

#===============================================================================
# urls de mensajeria
#===============================================================================

urlpatterns += patterns('mensajeria.views',
	url(r'^gosurvey/$', 'gosurvey'),
	url(r'^encuesta/(?P<id_proyecto>[0-9]{1,10})/(?P<key>[0-9a-zA-Z]{1,65})/$', 'encuesta'),
	url(r'^respuestas/detalladas/$', 'detalladas'),
    url(r'^respuestas/metricas/$', 'metricas'),
    url(r'^respuestas/forzar/(?P<id_colaborador>[0-9]{1,10})/$', 'colaboradoreenviar'),
	url(r'^participante/activar2/(?P<id_colaborador>[0-9]{1,10})/$', 'colaboradoractivarmensajeria'),
    url(r'^respuestas/exportar/$', 'exportar'),
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
