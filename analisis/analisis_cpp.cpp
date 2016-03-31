#include "aux.hpp"


string participacion(string id_proyecto,string id_user,string human) {
	// connection C("dbname=gogo user=usuariodb_gogo password='W#y2d@uV4+eSPuwrEc$UTrE4eCruTHas' hostaddr=127.0.0.1 port=5432");
	string sql =	"SELECT "
						"cuestionarios_proyectos.id, "
						"cuestionarios_proyectos.activo, "
						"cuestionarios_proyectos.interna, "
						"cuestionarios_proyectos.max_variables, "
						"cuestionarios_proyectos.nombre, "
						"cuestionarios_proyectos.tipo, "
						"cuestionarios_proyectos.tot_aresponder, "
						"cuestionarios_proyectos.tot_participantes, "
						"cuestionarios_proyectos.tot_preguntas, "
						"cuestionarios_proyectos.tot_preguntas, "
						"cuestionarios_proyectos.tot_respuestas, "
						"cuestionarios_proyectos.tot_respuestas, "
						"cuestionarios_proyectos.total, "
						"usuarios_proyectosdatos.ffin, "
						"usuarios_proyectosdatos.finicio, "
						"usuarios_proyectosdatos.id_id, "
						"usuarios_proyectosdatos.opcional1, "
						"usuarios_proyectosdatos.opcional2, "
						"usuarios_proyectosdatos.opcional3, "
						"usuarios_proyectosdatos.opcional4, "
						"usuarios_proyectosdatos.opcional5 "
					"FROM "
						"cuestionarios_proyectos "
					"JOIN "
						"usuarios_proyectosdatos "
					"ON "
						"(cuestionarios_proyectos.id = usuarios_proyectosdatos.id_id ) "
					"WHERE "
						"cuestionarios_proyectos.id ="+ id_proyecto +";";

	// ejecutamos el analisis_cppdores
	result R = leer(sql);

	Proyecto pro;
	string auxiliar;

	pro.activo = R[0]["activo"].as<bool>() ;
	pro.interna = R[0]["interna"].as<bool>() ;
	pro.total = R[0]["total"].as<float>() ;
	pro.ffin = R[0]["ffin"].as<string>() ;
	pro.finicio = R[0]["finicio"].as<string>() ;
	pro.max_variables = R[0]["max_variables"].as<string>() ;
	auxiliar = R[0]["nombre"].as<string>(); escape(auxiliar);
	pro.nombre = auxiliar ;
	auxiliar = R[0]["opcional1"].as<string>() ; escape(auxiliar);
	pro.opcional1 = auxiliar ;
	auxiliar = R[0]["opcional2"].as<string>() ; escape(auxiliar);
	pro.opcional2 = auxiliar ;
	auxiliar = R[0]["opcional3"].as<string>() ; escape(auxiliar);
	pro.opcional3 = auxiliar ;
	auxiliar = R[0]["opcional4"].as<string>() ; escape(auxiliar);
	pro.opcional4 = auxiliar ;
	auxiliar = R[0]["opcional5"].as<string>() ; escape(auxiliar);
	pro.opcional5 = auxiliar ;
	pro.tot_aresponder = R[0]["tot_aresponder"].as<string>() ;
	pro.tot_participantes = R[0]["tot_participantes"].as<string>() ;
	pro.tot_preguntas = R[0]["tot_preguntas"].as<int>() ;
	pro.tot_respuestas = R[0]["tot_respuestas"].as<int>() ;

			sql =	"SELECT "
						"usuarios_permisos.col_add, "
						"usuarios_permisos.col_see, "
						"usuarios_permisos.consultor, "
						"usuarios_permisos.res_exp, "
						"usuarios_permisos.var_add, "
						"usuarios_permisos.var_see "
					"FROM "
						"usuarios_permisos "
					"WHERE "
						"usuarios_permisos.id_id ="+ id_user +";";
	R = leer(sql);

	Permisos permisos;
	permisos.col_add = R[0]["col_add"].as<bool>() ;
	permisos.col_see = R[0]["col_see"].as<bool>() ;
	permisos.consultor = R[0]["consultor"].as<bool>() ;
	permisos.res_exp = R[0]["res_exp"].as<bool>() ;
	permisos.var_add = R[0]["var_add"].as<bool>() ;
	permisos.var_see = R[0]["var_see"].as<bool>() ;

		sql = "SELECT "
					"mensajeria_streaming.colaborador_id, "
					"mensajeria_streaming.respuesta, "
					"mensajeria_streaming.fecharespuesta "
				"FROM "
					"mensajeria_streaming "
				"WHERE "
					"mensajeria_streaming.proyecto_id = "+id_proyecto+";";

	R = leer(sql);

	string datos ="[ ";
	for (result::size_type i = 0; i != R.size(); ++i){
		datos += "[ "+ R[i]["colaborador_id"].as<string>();
		try {
			R[i]["respuesta"].as<string>();
			datos += ",1,";
		}
			catch (const exception &e){ datos += ",0,"; }
		try {
			datos += fecha(R[i]["fecharespuesta"].as<string>());
		}
			catch (const exception &e){ datos += "0"; }
		datos+= "],";
	}
	datos+= "]";


			sql = 	"SELECT "
						"colaboradores_colaboradores.id, "
						"colaboradores_datos.id_id, "
						"colaboradores_datos.area, "
						"colaboradores_datos.cargo, "
						"colaboradores_datos.genero, "
						"colaboradores_datos.niv_academico, "
						"colaboradores_datos.opcional1, "
						"colaboradores_datos.opcional2, "
						"colaboradores_datos.opcional3, "
						"colaboradores_datos.opcional4, "
						"colaboradores_datos.opcional5, "
						"colaboradores_datos.ciudad, "
						"colaboradores_datos.profesion, "
						"colaboradores_datos.regional "
					"FROM "
						"colaboradores_colaboradores "
					"LEFT OUTER JOIN "
						"colaboradores_datos "
					"ON "
						"( colaboradores_colaboradores.id = colaboradores_datos.id_id ) "
					"WHERE "
						"colaboradores_colaboradores.proyecto_id = "+ id_proyecto +";";

	R = leer(sql);
	string participantes ="{ ";
	for (result::size_type i = 0; i != R.size(); ++i){
		participantes += R[i]["id"].as<string>() +": { " ;
		try {
			auxiliar = R[i]["area"].as<string>() ; escape(auxiliar);
			participantes += "'area':`"+R[i]["area"].as<string>() ;
		}
			catch (const exception &e){}
		try {
			auxiliar = R[i]["cargo"].as<string>() ; escape(auxiliar);
			participantes += "`,'cargo':`"+R[i]["cargo"].as<string>() ;
		}
			catch (const exception &e){}
		try {
			auxiliar = R[i]["ciudad"].as<string>() ; escape(auxiliar);
			participantes += "`,'ciudad':`"+R[i]["ciudad"].as<string>() ;
		}
			catch (const exception &e){}
		try {
			auxiliar = R[i]["genero"].as<string>() ; escape(auxiliar);
			participantes += "`,'genero':`"+R[i]["genero"].as<string>() ;
		}
			catch (const exception &e){}
		try {
			auxiliar = R[i]["niv_academico"].as<string>() ; escape(auxiliar);
			participantes += "`,'niv_academico':`"+R[i]["niv_academico"].as<string>() ;
		}
			catch (const exception &e){}
		try {
			auxiliar = R[i]["opcional1"].as<string>() ; escape(auxiliar);
			participantes += "`,'opcional1':`"+R[i]["opcional1"].as<string>() ;
		}
			catch (const exception &e){}
		try {
			auxiliar = R[i]["opcional2"].as<string>() ; escape(auxiliar);
			participantes += "`,'opcional2':`"+R[i]["opcional2"].as<string>() ;
		}
			catch (const exception &e){}
		try {
			auxiliar = R[i]["opcional3"].as<string>() ; escape(auxiliar);
			participantes += "`,'opcional3':`"+R[i]["opcional3"].as<string>() ;
		}
			catch (const exception &e){}
		try {
			auxiliar = R[i]["opcional4"].as<string>() ; escape(auxiliar);
			participantes += "`,'opcional4':`"+R[i]["opcional4"].as<string>() ;
		}
			catch (const exception &e){}
		try {
			auxiliar = R[i]["opcional5"].as<string>() ; escape(auxiliar);
			participantes += "`,'opcional5':`"+R[i]["opcional5"].as<string>() ;
		}
			catch (const exception &e){}
		try {
			auxiliar = R[i]["profesion"].as<string>() ; escape(auxiliar);
			participantes += "`,'profesion':`"+R[i]["profesion"].as<string>() ;
		}
			catch (const exception &e){}
		try {
			auxiliar = R[i]["regional"].as<string>() ; escape(auxiliar);
			participantes += "`,'regional':`"+R[i]["regional"].as<string>() +"` }," ;
		}
			catch (const exception &e){}
	}
	participantes += "}";

	// RegisterTemplateFilename(MyTmpl, "/home/suidi/workspace/gogo/analisis/plantillas/participacion_cpp.html");
	RegisterTemplateFilename(MyTmpl, "/home/ubuntu/gogo/analisis/plantillas/participacion_cpp.html");


	ctemplate::TemplateDictionary dict("contexto");

	if(pro.interna) dict.ShowSection("PROYECTO_INTERNA");
	if(pro.opcional1 != "") {
		dict.ShowSection("PDATOS_OPCIONAL1");
		dict.SetValue("PDATOS_NOM_OPCIONAL_1",pro.opcional1);
	}
	if(pro.opcional2 != "") {
		dict.ShowSection("PDATOS_OPCIONAL2");
		dict.SetValue("PDATOS_NOM_OPCIONAL_2",pro.opcional2);
	}
	if(pro.opcional3 != "") {
		dict.ShowSection("PDATOS_OPCIONAL3");
		dict.SetValue("PDATOS_NOM_OPCIONAL_3",pro.opcional3);
	}
	if(pro.opcional4 != "") {
		dict.ShowSection("PDATOS_OPCIONAL4");
		dict.SetValue("PDATOS_NOM_OPCIONAL_4",pro.opcional4);
	}
	if(pro.opcional5 != "") {
		dict.ShowSection("PDATOS_OPCIONAL5");
		dict.SetValue("PDATOS_NOM_OPCIONAL_5",pro.opcional5);
	}

	dict.SetValue("PROYECTO_MAX_VARIABLES",pro.max_variables);
	dict.SetValue("PROYECTO_TOT_PREGUNTAS",to_string(pro.tot_preguntas));
	dict.SetValue("PROYECTO_TOT_PARTICIPANTES",pro.tot_participantes);
	dict.SetValue("PROYECTO_TOT_ARESPONDER",pro.tot_aresponder);
	dict.SetValue("PROYECTO_TOT_RESPUESTAS",to_string(pro.tot_respuestas));
	dict.SetValue("PROYECTO_TOTAL",to_string((int)pro.total));
	dict.SetValue("FINICIO",fecha(pro.finicio));
	dict.SetValue("FFIN",fecha(pro.ffin));

	if(pro.activo) dict.SetValue("PROYECTO_ACTIVO","Activo");
	else dict.SetValue("PROYECTO_ACTIVO","Inactivo");
	if(pro.tot_respuestas && pro.tot_preguntas) {
		 int finalizados = pro.tot_respuestas/pro.tot_preguntas;
		 dict.SetValue("FINALIZADOS",to_string(finalizados));
	} else {
		dict.SetValue("FINALIZADOS",to_string(0));
	}

	if(permisos.col_add) dict.ShowSection("PERMISOS_COL_ADD");
	if(permisos.col_see) dict.ShowSection("PERMISOS_COL_SEE");
	if(permisos.consultor) dict.ShowSection("PERMISOS_CONSULTOR");
	if(permisos.res_exp) dict.ShowSection("PERMISOS_RES_EXP");
	if(permisos.var_add) dict.ShowSection("PERMISOS_VAR_ADD");
	if(permisos.var_see) dict.ShowSection("PERMISOS_VAR_SEE");

	dict.SetValue("PROYECTO_NOMBRE", pro.nombre);
	dict.SetValue("DATOS", datos);
	dict.SetValue("PARTICIPANTES", participantes);
	dict.SetValue("HUMANIZE", human);

	string contexto;

	ctemplate::ExpandTemplate(MyTmpl, ctemplate::DO_NOT_STRIP, &dict, &contexto);
	return contexto;
}


static PyObject* participacion( PyObject *self, PyObject *args ){
	const char * id_proyecto;
	const char * id_user;
	const char * human;
	if(!PyArg_ParseTuple(args,"sss",&id_proyecto,&id_user,&human)) return NULL;
	return Py_BuildValue("s",participacion(id_proyecto,id_user,human).c_str());
}

static PyMethodDef analisis_cpp_metodos[]={
	{"participacion",(PyCFunction)participacion,METH_VARARGS},
	{NULL,NULL,0,NULL}
};

PyMODINIT_FUNC initanalisis_cpp(void){
	Py_InitModule("analisis_cpp",analisis_cpp_metodos);
}
