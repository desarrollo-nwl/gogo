# -*- encoding: utf-8 -*-
from colaboradores_360.models import Colaboradores_360
from colaboradores_360.models import ColaboradoresMetricas_360
from colaboradores_360.models import Roles_360
from cuestionarios_360.models import Instrumentos_360,Preguntas_360
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import transaction
from django.db.models import F
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_control
from mensajeria_360.models import Streaming_360
from redes_360.models import Redes_360
from usuarios.models import Proyectos, Logs
import json
import random
import redes as redes_cpp
import xlrd,xlwt,ujson

#===============================================================================
# indices
#===============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def redes_360(request):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa","360 unico"] :
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.red_see:

		roles = Roles_360.objects.filter(proyecto_id=proyecto.id)

		instrumentos = Instrumentos_360.objects.only('nombre').filter(proyecto_id=proyecto.id)

		personas = redes_cpp.ver_personas(str(proyecto.id))

		redes = redes_cpp.ver_redes(str(proyecto.id),permisos.red_edit,permisos.red_del)

		return render_to_response('redes_ind.html',{
		'Activar':'Contenido','activar':'RedesIndividual',
		'Proyecto':proyecto,'Permisos':permisos,
		'Personas':personas,'Roles':roles,'Instrumentos':instrumentos,
		'Redes':redes
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def rednueva_360(request):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa","360 unico"] :
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.red_add:
		if request.method == 'POST':
			if not Redes_360.objects.filter(
				colaborador_id=request.POST['colaborador'],
				evaluado_id=request.POST['evaluado'],
				proyecto_id=proyecto.id).exists():

				rol = Roles_360.objects.filter(proyecto_id=proyecto.id).get(id=request.POST['rol'])

				instrumento = Instrumentos_360.objects.filter(
														id=request.POST['instrumento'],
														proyecto_id=proyecto.id).first()
				if Colaboradores_360.objects.filter(
						id=request.POST['evaluado'],
						proyecto_id=proyecto.id).exists() and instrumento:

					vec_st_360 = []
					with transaction.atomic():
						colaborador = Colaboradores_360.objects.filter(
							proyecto_id=proyecto.id).get(id=request.POST['colaborador'])

						red = Redes_360.objects.create(
							colaborador_id = request.POST['colaborador'],
							evaluado_id = request.POST['evaluado'],
							instrumento_id = request.POST['instrumento'],
							rol_idn = request.POST['rol'],
							rol = rol.nombre,
							proyecto_id=proyecto.id)

						col_met = ColaboradoresMetricas_360.objects.only('ord_instrumentos'
									).get( id = colaborador )
						ord_instrumentos = json.loads( col_met.ord_instrumentos )
						ord_instrumentos.append( red.id )
						ColaboradoresMetricas_360.objects.filter(id=col_met.id
									).update( ord_instrumentos = ord_instrumentos )

						preguntas = Preguntas_360.objects.filter(
										proyecto_id = proyecto.id,
										instrumento_id = red.instrumento_id)

						for i in preguntas:
							vec_st_360.append( Streaming_360(
									colaborador_id = red.colaborador_id,
									evaluado_id = red.evaluado_id,
									rol = red.rol,
									instrumento_id =  red.instrumento_id,
									pregunta_id = i.id,
									proyecto_id = proyecto.id,
									red_id = red.id	) )

						Streaming_360.objects.bulk_create(vec_st_360)
						if instrumento.max_preguntas:
							total = 100 * colaborador.pre_respuestas/(colaborador.pre_aresponder+instrumento.max_preguntas)
							Colaboradores_360.objects.filter(id=colaborador.id
								).update(
									pre_aresponder = F('pre_aresponder')+instrumento.max_preguntas,
									tot_avance = total,
									)
							total = 100 * proyecto.tot_respuestas/(proyecto.tot_aresponder+instrumento.max_preguntas)
							Proyectos.objects.filter(id=proyecto.id).update(
								tot_aresponder = F('tot_aresponder')+instrumento.max_preguntas,
								total = total,
								)
							cache.set(request.user.username,proyecto,86400)

				red = Redes_360.objects.only(
						'colaborador_id','evaluado_id','instrumento_id',
						'colaborador__nombre','colaborador__apellido','instrumento__nombre',
						'evaluado__nombre','evaluado__apellido','rol','rol_idn'
						).filter(id=red.id,proyecto_id=proyecto.id).select_related(
						'colaborador','evaluado','instrumento')[0]

				return JsonResponse({
							'id':red.id,
							'id_col':red.colaborador_id,
							'nom_col':' '.join([red.colaborador.nombre,red.colaborador.apellido]),
							'id_eval':red.evaluado_id,
							'nom_eval':' '.join([red.evaluado.nombre,red.evaluado.apellido]),
							'id_inst':red.instrumento_id,
							'nom_inst':red.instrumento.nombre,
							'rol':red.rol,
							'rol_idn':red.rol_idn,
							})
		return render_to_response('403.html')
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def reditar_360(request,id_red):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa","360 unico"] :
		return render_to_response('423.html')
	permisos = request.user.permisos

	if permisos.consultor and permisos.red_edit:
		if request.method == 'POST':

			if not Redes_360.objects.filter(
				colaborador_id=request.POST['colaborador'],
				evaluado_id=request.POST['evaluado'],
				proyecto_id=proyecto.id).exclude(id=id_red).exists():

				rol = Roles_360.objects.filter(proyecto_id=proyecto.id).get(id=request.POST['rol'])

				instrumento = Instrumentos_360.objects.filter(id = request.POST['instrumento'],proyecto_id=proyecto.id ).first()

				if  Colaboradores_360.objects.filter(
						id=request.POST['evaluado'],
						proyecto_id=proyecto.id).exists() and instrumento:

					vec_st_360 = []
					with transaction.atomic():
						colaborador = Colaboradores_360.objects.filter(
										proyecto_id=proyecto.id,
										id=request.POST['colaborador']
										).select_related(
										'colaboradoresmetricas_360')[0]

						red = Redes_360.objects.get(id=id_red)
						if colaborador.id != red.colaborador_id:
							colaborador_old = Colaboradores_360.objects.filter(id=red.colaborador_id
												).select_related('colaboradoresmetricas_360')[0]
							ord_instrumentos = colaborador_old.colaboradoresmetricas_360.ord_instrumentos
							ord_instrumentos = json.loads(ord_instrumentos)
							ord_instrumentos.remove(red.id)
							if red.id == colaborador_old.colaboradoresmetricas_360.ins_actual :
								try:
									ins_actual = ord_instrumentos[ord_instrumentos.index(red.id) - 1]
								except:
									ins_actual = 0
							else:
								ins_actual = colaborador_old.colaboradoresmetricas_360.ins_actual

							ord_instrumentos = json.dumps(ord_instrumentos)

							total = 0
							pre_respuestas_red = 0
							if colaborador_old.pre_aresponder - instrumento.max_preguntas != 0 :
								total = 100 * colaborador_old.pre_respuestas/(colaborador_old.pre_aresponder - instrumento.max_preguntas )
								pre_respuestas_red = Streaming_360.objects.filter(red_id = red.id,respuesta__isnull=False).count()

							Colaboradores_360.objects.filter(id=red.colaborador_id
								).update(
									pre_aresponder = F('pre_aresponder') - instrumento.max_preguntas,
									pre_respuestas = F('pre_respuestas') - pre_respuestas_red,
									tot_avance = total,
									)

							ColaboradoresMetricas_360.objects.filter(id_id = colaborador_old.id
								).update(
									ord_instrumentos = ord_instrumentos,
									ins_actual=ins_actual,
									)
							if instrumento.max_preguntas:
								col_met = colaborador.colaboradoresmetricas_360
								ord_instrumentos = json.loads( col_met.ord_instrumentos )
								ord_instrumentos.append( int(id_red) )
								ord_instrumentos = json.dumps(ord_instrumentos)

								ColaboradoresMetricas_360.objects.filter(id=col_met.id_id
									).update( ord_instrumentos = ord_instrumentos )

								total = 100 * colaborador.pre_respuestas/(colaborador.pre_aresponder+instrumento.max_preguntas)
								Colaboradores_360.objects.filter(id=colaborador.id
									).update(
										pre_aresponder = F('pre_aresponder')+instrumento.max_preguntas,
										tot_avance = total,
										)

						Streaming_360.objects.filter(red_id=id_red).delete()

						Redes_360.objects.filter(id=id_red).update(
							colaborador_id = request.POST['colaborador'],
							evaluado_id = request.POST['evaluado'],
							instrumento_id = request.POST['instrumento'],
							rol_idn = request.POST['rol'],
							rol = rol.nombre,
							pre_respuestas = 0,
							tot_procentaje = 0,
							proyecto_id = proyecto.id )

						preguntas = Preguntas_360.objects.filter(
										proyecto_id = proyecto.id,
										instrumento_id = request.POST['instrumento'])

						muestra = Streaming_360.objects.filter(colaborador_id = request.POST['colaborador']).first()
						if muestra:
							fcache = muestra.fec_controlenvio
							for i in preguntas:
								vec_st_360.append(
									Streaming_360(
										colaborador_id = request.POST['colaborador'],
										evaluado_id = request.POST['evaluado'],
										instrumento_id = request.POST['instrumento'],
										pregunta_id = i.id,
										proyecto_id = proyecto.id,
										red_id = id_red,
										fec_controlenvio = fcache ) )
						else:
							for i in preguntas:
								vec_st_360.append(
									Streaming_360(
										colaborador_id = request.POST['colaborador'],
										evaluado_id = request.POST['evaluado'],
										instrumento_id = request.POST['instrumento'],
										pregunta_id = i.id,
										proyecto_id = proyecto.id,
										red_id = id_red	) )

						Streaming_360.objects.bulk_create(vec_st_360)



				red = Redes_360.objects.only(
						'colaborador_id','evaluado_id','instrumento_id',
						'colaborador__nombre','colaborador__apellido','instrumento__nombre',
						'evaluado__nombre','evaluado__apellido','rol','rol_idn'
						).filter(id=id_red,proyecto_id=proyecto.id).select_related(
						'colaborador','evaluado','instrumento')[0]

				return JsonResponse({
							'id':red.id,
							'id_col':red.colaborador_id,
							'nom_col':' '.join([red.colaborador.nombre,red.colaborador.apellido]),
							'id_eval':red.evaluado_id,
							'nom_eval':' '.join([red.evaluado.nombre,red.evaluado.apellido]),
							'id_inst':red.instrumento_id,
							'nom_inst':red.instrumento.nombre,
							'rol':red.rol,
							'rol_idn':red.rol_idn,
							})
			return JsonResponse({'id':0})
		return render_to_response('403.html')
	else:
		return render_to_response('403.html')


@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def redeliminar_360(request,id_red):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa","360 unico"] :
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.red_add:

		red = Redes_360.objects.filter(id=id_red,proyecto_id=proyecto.id).first()
		if red:
			num_preguntas = Instrumentos_360.objects.only('max_preguntas'
								).get(id=red.instrumento_id).max_preguntas
			colaborador = Colaboradores_360.objects.only('pre_aresponder','pre_respuestas'
							).filter(id=red.colaborador_id).select_related('colaboradoresmetricas_360')[0]

			colaboradoresmetricas = colaborador.colaboradoresmetricas_360
			ord_instrumentos = colaboradoresmetricas.ord_instrumentos
			ord_instrumentos = json.loads(ord_instrumentos)
			ord_instrumentos.remove(red.id)

			if red.id == colaboradoresmetricas.ins_actual :
				try:
					ins_actual = ord_instrumentos[ord_instrumentos.index(red.id) - 1]
				except:
					ins_actual = 0
			else:
				ins_actual = colaborador.colaboradoresmetricas_360.ins_actual

			ord_instrumentos = json.dumps(ord_instrumentos)

			total = 0
			pre_respuestas_red = 0
			if colaborador.pre_aresponder - num_preguntas != 0 :
				total = 100 * colaborador.pre_respuestas/(colaborador.pre_aresponder - num_preguntas )
				pre_respuestas_red = Streaming_360.objects.filter(red_id = red.id,respuesta__isnull=False).count()

			with transaction.atomic():
				Colaboradores_360.objects.filter(id=red.colaborador_id
					).update(
						pre_aresponder = F('pre_aresponder') - num_preguntas,
						pre_respuestas = F('pre_respuestas') - pre_respuestas_red,
						tot_avance = total,
						)
				total = 0
				if proyecto.tot_aresponder - num_preguntas != 0:
					total = 100 * proyecto.tot_respuestas/(proyecto.tot_aresponder - num_preguntas )

				proyecto.tot_aresponder -=  num_preguntas
				proyecto.tot_respuestas -= pre_respuestas_red
				proyecto.tot_avance = total

				Proyectos.objects.filter(id=proyecto.id
					).update(
						tot_aresponder = proyecto.tot_aresponder,
						tot_respuestas = proyecto.tot_respuestas,
						total = proyecto.total,
						)
				ColaboradoresMetricas_360.objects.filter(id_id = colaborador.id
					).update(
						ord_instrumentos = ord_instrumentos,
						ins_actual=ins_actual,
						)
				Redes_360.objects.filter(id=id_red).delete()

			cache.set(request.user.username,proyecto,86400)
			return JsonResponse({'id':id_red})
		else:
			return JsonResponse({'id':0})

	else:
		return render_to_response('403.html')



# ==============================================================================
#    Archivo excel
# ==============================================================================

@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def redes_archivo_generar(request):
	tit_format = xlwt.easyxf('font:bold on ;align:wrap on, vert centre, horz center;')
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa","360 unico"] :
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.red_add:
		response = HttpResponse(content_type='application/ms-excel')
		import string
		a ='Respuestas'
		response['Content-Disposition'] = 'attachment; filename=%s.xls'%(a)
		wb = xlwt.Workbook(encoding='utf-8')
		ws = wb.add_sheet(a)
		datos = proyecto.proyectosdatos
		ws.write(0,0,u"Nombre del evaluador",tit_format)
		ws.write(0,1,u"Apellido del evalador",tit_format)
		ws.write(0,2,u"Rol",tit_format)
		ws.write(0,3,u"Nombre del evaluado",tit_format)
		ws.write(0,4,u"Apellido del evaluado",tit_format)
		ws.write(0,5,u"Instrumento",tit_format)
		wb.save(response)
		return response



@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def redes_xls_360(request):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa","360 unico"] :
		return render_to_response('423.html')
	proyecto = Proyectos.objects.get(id=proyecto.id)
	permisos = request.user.permisos
	if permisos.consultor and permisos.col_add:

		if request.method == 'POST':

			input_excel = request.FILES['docfile']
			doc = xlrd.open_workbook(file_contents=input_excel.read())
			sheet = doc.sheet_by_index(0)
			filas = sheet.nrows

			personas = {}
			instrumentos = {}
			roles = {}
			colaborador_str = None
			evaluado_str = ""

			verifica = []

			personas_404 = []
			roles_404 = []
			instrumentos_404 = []
			redes_500 = []

			with transaction.atomic():
				for i in xrange(1,filas):
					vect_st_360 = []
					preguntas_contador = 0
					colaborador_str = " ".join([sheet.cell_value(i,0), sheet.cell_value(i,1)])
					evaluado_str = " ".join([sheet.cell_value(i,3), sheet.cell_value(i,4)])
					if not (colaborador_str,evaluado_str) in verifica:
						verifica.append((colaborador_str,evaluado_str))

						try:
							colaborador = personas[colaborador_str]
						except:
							colaborador = Colaboradores_360.objects.filter(
								proyecto_id = proyecto.id,
								nombre = sheet.cell_value(i,0),
								apellido =  sheet.cell_value(i,1),
								).select_related('colaboradoresmetricas_360').first()
							if colaborador:
								personas[colaborador_str] = colaborador

						if colaborador:
							try:
								rol = roles[sheet.cell_value(i,2)]
							except:
								rol = Roles_360.objects.filter(
									proyecto_id = proyecto.id,
									nombre = sheet.cell_value(i,2),
									).first()
								if rol:
									roles[rol.nombre] = rol

							if rol:
								try:
									evaluado = personas[evaluado_str]
								except:
									evaluado = Colaboradores_360.objects.filter(
										proyecto_id = proyecto.id,
										nombre = sheet.cell_value(i,3),
										apellido =  sheet.cell_value(i,4),
										).first()
									if evaluado:
										personas[evaluado_str] = evaluado

								if evaluado:
									try:
										instrumento = instrumentos[sheet.cell_value(i,5)]
									except:
										instrumento = Instrumentos_360.objects.filter(
											proyecto_id = proyecto.id,
											nombre = sheet.cell_value(i,5),
											).first()
										if instrumento:
											instrumentos[instrumento.nombre] = instrumento

									if instrumento:
										if not Redes_360.objects.filter(
													proyecto_id = proyecto.id,
													colaborador_id = colaborador.id,
													evaluado_id = evaluado.id).exists():

											red = Redes_360.objects.create(
												colaborador_id = colaborador.id,
												evaluado_id = evaluado.id,
												instrumento_id = instrumento.id,
												rol_idn = rol.id,
												rol = rol.nombre,
												proyecto_id=proyecto.id)

											col_met = colaborador.colaboradoresmetricas_360
											ord_instrumentos = json.loads( col_met.ord_instrumentos )
											ord_instrumentos.append( red.id )
											ord_instrumentos = json.dumps( ord_instrumentos )
											ColaboradoresMetricas_360.objects.filter(id=col_met.id
														).update( ord_instrumentos = ord_instrumentos )
											colaborador.colaboradoresmetricas_360.ord_instrumentos = ord_instrumentos

											preguntas = Preguntas_360.objects.filter(
															proyecto_id = proyecto.id,
															instrumento_id = red.instrumento_id)

											for i in preguntas:
												vect_st_360.append( Streaming_360(
														colaborador_id = red.colaborador_id,
														evaluado_id = red.evaluado_id,
														instrumento_id =  red.instrumento_id,
														pregunta_id = i.id,
														proyecto_id = proyecto.id,
														red_id = red.id	) )
												preguntas_contador += 1
											if colaborador.pre_aresponder:
												total = 100 * colaborador.pre_respuestas/(colaborador.pre_aresponder+preguntas_contador)
											else:
												total = 0
											Colaboradores_360.objects.filter(id=colaborador.id).update(
												pre_aresponder = F('pre_aresponder') + preguntas_contador,
												tot_avance = total)
											colaborador.pre_aresponder += preguntas_contador
											colaborador.tot_avance = total

										else:
											redes_500.append(" ".join([
															colaborador_str,
															sheet.cell_value(i,2),
															evaluado_str,
															sheet.cell_value(i,5)]))
									else:
										instrumentos_404.append(sheet.cell_value(i,5))
								else:
									personas_404.append(evaluado_str)
							else:
								roles_404.append(sheet.cell_value(i,2))
						else:
							personas_404.append(colaborador_str)
					else:
						redes_500.append(" ".join([
										colaborador_str,
										sheet.cell_value(i,2),
										evaluado_str,
										sheet.cell_value(i,5)]))

					if vect_st_360:
						Streaming_360.objects.bulk_create(vect_st_360)
						proyecto.tot_aresponder += preguntas_contador

				Proyectos.objects.filter(id=proyecto.id).update(
							tot_aresponder = proyecto.tot_aresponder)
				cache.set(request.user.username,proyecto,86400)
				if any([personas_404,roles_404,instrumentos_404,redes_500]):
					return render_to_response('redes_xls_360.html',{
						'Activar':'Contenido','activar':'AcrhivoPlano',
						'Proyecto':proyecto,'Permisos':permisos,'Personas':personas_404,
						'Roles':roles_404,'Instrumentos':instrumentos_404,'Redes':redes_500
						}, context_instance=RequestContext(request))
			return HttpResponseRedirect('/360/redes/')

		return render_to_response('redes_xls_360.html',{
		'Activar':'Contenido','activar':'AcrhivoPlano',
		'Proyecto':proyecto,'Permisos':permisos,
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('403.html')



@cache_control(no_store=True)
@login_required(login_url='/acceder/')
def redes_activar_360(request,id_red):
	proyecto = cache.get(request.user.username)
	if not proyecto or proyecto.tipo in ["Completa","Fragmenta","Externa","360 unico"] :
		return render_to_response('423.html')
	permisos = request.user.permisos
	if permisos.consultor and permisos.red_edit:

		red = Redes_360.objects.only('id','estado').filter(id = id_red, proyecto_id = proyecto).first()

		if red and red.estado:
			estado = False
			Redes_360.objects.filter(id = id_red).update(estado=False)
		elif red:
			estado = True
			Redes_360.objects.filter(id = id_red).update(estado=True)
		else:
			id_red = 0
		return HttpResponse(ujson.dumps({'id':id_red,'estado':estado}),content_type='application/json')
	else:
		return HttpResponse(ujson.dumps({'id':0}),content_type='application/json')
