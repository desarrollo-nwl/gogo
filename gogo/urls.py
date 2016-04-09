from django.conf import settings
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf.urls import handler400,handler403,handler404, handler500
from usuarios.views import e400,e403,e404,e500

#===============================================================================
# urls de usuarios y varias
#===============================================================================

urlpatterns = patterns('usuarios.views',
	url(r'^$', 'index', name='index'),
	url(r'^index/$', 'index'),
	url(r'^acceder/$', 'acceder'),
	url(r'^recuperar/$', 'recuperar'),
	url(r'^home/$', 'home'),
	url(r'^menu/(?P<id_proyecto>[0-9]{1,10})/$', 'menu'),
	url(r'^home2/$', 'home2'),
	url(r'^logs/$', 'logs'),
	url(r'^terminos/$', 'terminos'),
	url(r'^privacidad/$', 'privacidad'),
	url(r'^reportar/$', 'reportarerror'),
	url(r'^faq/$', 'faq'),
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
)

#===============================================================================
# urls de participantes
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
	url(r'^externa/(?P<id_proyecto>[0-9]{1,10})/(?P<key>[0-9a-zA-Z]{1,65})/$', 'encuestaexterna'),
	url(r'^externa2/(?P<id_proyecto>[0-9]{1,10})/(?P<key>[0-9a-zA-Z]{1,65})/$', 'encuestaexterna2'),
	url(r'^respuestas/detalladas/$', 'detalladas'),
    url(r'^respuestas/metricas/$', 'metricas'),
    url(r'^respuestas/forzar/(?P<id_colaborador>[0-9]{1,10})/$', 'colaboradoreenviar'),
	url(r'^participante/activar2/(?P<id_colaborador>[0-9]{1,10})/$', 'colaboradoractivarmensajeria'),
    url(r'^respuestas/exportar/interna/$', 'exportarinterna'),
	url(r'^respuestas/exportar/externa/$', 'exportarexterna'),
	url(r'^respuestas/importar/exportar/$', 'importarespuestas_exportar'),
	url(r'^respuestas/importar/$', 'importarespuestas_preguntas'),
)

#===============================================================================
# urls de AnalisisResultados
#===============================================================================

urlpatterns += patterns('analisis.views',
	url(r'^analisis/participacion/$', 'participacion'),
	url(r'^analisis/focalizado/$', 'focalizado'),
	url(r'^analisis/general/$', 'general'),
	url(r'^analisis/wordanalytics/$', 'wordanalytics'),
)


#===============================================================================
# urls de cuestionarios 360
#===============================================================================

urlpatterns += patterns('cuestionarios_360.views',
	url(r'^360/instrumento/eliminar/(?P<id_instrumento>[0-9]{1,10})/$', 'instrumentoeliminar'),
	url(r'^360/pregunta/activar/(?P<id_pregunta>[0-9]{1,10})/$', 'preguntactivar_360'),
	url(r'^360/pregunta/clonar/(?P<id_pregunta>[0-9]{1,10})/$', 'preguntaclonar_360'),
	url(r'^360/variable/activar/(?P<id_variable>[0-9]{1,10})/$', 'variableactivar_360'),
	url(r'^360/instrumento/activar/(?P<id_instrumento>[0-9]{1,10})/$', 'instrumentoactivar'),
	url(r'^360/dimension/activar/(?P<id_dimension>[0-9]{1,10})/$', 'dimensionactivar'),
	url(r'^360/dimension/(?P<id_dimension>[0-9]{1,10})/variable/nueva/$', 'variablenueva_360'),
	url(r'^360/dimension/(?P<id_dimension>[0-9]{1,10})/variables/$', 'variables_360'),
	url(r'^360/dimension/editar/(?P<id_dimension>[0-9]{1,10})/$', 'dimensioneditar'),
	url(r'^360/dimension/eliminar/(?P<id_dimension>[0-9]{1,10})/$', 'dimensioneliminar'),
	url(r'^360/instrumento/(?P<id_instrumento>[0-9]{1,10})/dimension/nueva/$', 'dimensionueva'),
	url(r'^360/instrumento/(?P<id_instrumento>[0-9]{1,10})/dimensiones/$', 'dimensiones'),
	url(r'^360/instrumento/editar/(?P<id_instrumento>[0-9]{1,10})/$', 'instrumentoeditar'),
	url(r'^360/instrumento/nuevo/$', 'instrumentonuevo'),
	url(r'^360/instrumentos/$', 'instrumentos'),
	url(r'^360/pregunta/(?P<id_pregunta>[0-9]{1,10})/$', 'preguntaeditar_360'),
	url(r'^360/pregunta/eliminar/(?P<id_pregunta>[0-9]{1,10})/$', 'preguntaeliminar_360'),
	url(r'^360/variable/(?P<id_variable>[0-9]{1,10})/pregunta/nueva/$', 'preguntanueva_360'),
	url(r'^360/variable/(?P<id_variable>[0-9]{1,10})/preguntas/$', 'preguntas_360'),
	url(r'^360/variable/editar/(?P<id_variable>[0-9]{1,10})/$', 'variableditar_360'),
	url(r'^360/variable/eliminar/(?P<id_variable>[0-9]{1,10})/$', 'variableliminar_360'),
	url(r'^360/previsualizacion/(?P<id_instrumento>[0-9]{1,10})/$', 'previsualizacion_360'),
)


#===============================================================================
# urls de participantes_360
#===============================================================================

urlpatterns += patterns('colaboradores_360.views',
	url(r'^360/participante/eliminar/(?P<id_colaborador>[0-9]{1,10})/$', 'colaboradoreliminar_360'),
	url(r'^360/participantes/individual/$', 'colaboradores_ind_360'),
	url(r'^360/participantes/archivo/$', 'colaboradores_xls_360'),
	url(r'^360/participante/nuevo/$', 'colaboradornuevo_360'),
	url(r'^360/participante/editar/(?P<id_colaborador>[0-9]{1,10})/$', 'colaboradoreditar_360'),
	url(r'^360/participante/activar/(?P<id_colaborador>[0-9]{1,10})/$', 'colaboradoractivar_360'),
	url(r'^360/archivo/$', 'archivo_360'),
	url(r'^360/roles/$', 'roles_360'),
	url(r'^360/rol/editar/(?P<id_rol>[0-9]{1,10})/$', 'roleditar_360'),
	url(r'^360/rol/eliminar/(?P<id_rol>[0-9]{1,10})/$', 'roleliminar_360'),
	url(r'^360/rol/nuevo/$', 'rolnuevo_360'),
)

#===============================================================================
# urls de redes_360
#===============================================================================

urlpatterns += patterns('redes_360.views',
	# url(r'^360/archivo/$', 'archivo_360'),
	url(r'^360/redes/$', 'redes_360'),
	url(r'^360/red/editar/(?P<id_red>[0-9]{1,10})/$', 'reditar_360'),
	url(r'^360/red/eliminar/(?P<id_red>[0-9]{1,10})/$', 'redeliminar_360'),
	url(r'^360/red/nueva/$', 'rednueva_360'),
	url(r'^360/redes/archivo/$', 'redes_xls_360'),
	url(r'^360/redes/archivo/generar/$', 'redes_archivo_generar'),
)

#===============================================================================
# urls de mensajeria
#===============================================================================

urlpatterns += patterns('mensajeria_360.views',
	url(r'^360/gosurvey/$', 'gosurvey_360'),
	url(r'^360/encuesta/(?P<id_proyecto>[0-9]{1,10})/(?P<key>[0-9a-zA-Z]{1,65})/$', 'encuesta_360'),
	url(r'^360/respuestas/detalladas/$', 'detalladas_360'),
    url(r'^360/respuestas/metricas/$', 'metricas_360'),
    # url(r'^respuestas/forzar/(?P<id_colaborador>[0-9]{1,10})/$', 'colaboradoreenviar'),
	# url(r'^participante/activar2/(?P<id_colaborador>[0-9]{1,10})/$', 'colaboradoractivarmensajeria'),
	url(r'^360/respuestas/exportar/interna/$', 'exportarinterna_360'),
	# url(r'^respuestas/importar/exportar/$', 'importarespuestas_exportar'),
	# url(r'^respuestas/importar/$', 'importarespuestas_preguntas'),
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
		url(r'^admin/', include(admin.site.urls)),
	)
