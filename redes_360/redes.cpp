#include "aux.hpp"


string ver_personas(string id_proyecto) {
	string sql = "SELECT "
					"colaboradores_360_colaboradores.id, "
					"colaboradores_360_colaboradores.apellido, "
					"colaboradores_360_colaboradores.nombre "
				"FROM "
					"colaboradores_360_colaboradores "
				"WHERE "
					"colaboradores_360_colaboradores.proyecto_id ="+ id_proyecto +";";

	result R = leer(sql);

	string output = "";
	string aux;
	for (result::size_type i = 0; i != R.size(); ++i){
		output += "<option value='";
		output += R[i]["id"].as<string>()+"'>";
		aux = R[i]["nombre"].as<string>(); escape(aux);
		output += aux+" ";
		aux = R[i]["apellido"].as<string>(); escape(aux);
		output += aux;
		output += "</option>";
	}

	return output;
}

static PyObject* ver_personas( PyObject *self, PyObject *args ){
	const char * id_proyecto;
	if(!PyArg_ParseTuple(args,"s",&id_proyecto)) return NULL;
	return Py_BuildValue("s",ver_personas(id_proyecto).c_str());
}


string ver_redes(string id_proyecto) {
	string sql = "SELECT "
					"Redes_360_Redes.id, "
					"Redes_360_Redes.rol_idn, "
					"Redes_360_Redes.estado, "
					"Redes_360_Redes.instrumento_id, "
					"Redes_360_Redes.evaluado_id, "
					"Redes_360_Redes.colaborador_id, "
					"cuestionarios_360_instrumentos.id, "
					"cuestionarios_360_instrumentos.nombre, "
					"colaboradores_360_colaboradores.id, "
					"colaboradores_360_colaboradores.apellido, "
					"colaboradores_360_colaboradores.nombre "
				"FROM "
					"Redes_360_Redes "
				"INNER JOIN "
					"cuestionarios_360_instrumentos "
				"ON "
					"( Redes_360_Redes.instrumento_id = cuestionarios_360_instrumentos.id ) "
				"INNER JOIN "
					"colaboradores_360_colaboradores "
				"ON "
					"( Redes_360_Redes.colaborador_id = colaboradores_360_colaboradores.id ) "
				"WHERE "
					"Redes_360_Redes.proyecto_id = "+ id_proyecto +";";

	result R = leer(sql);

	string output = "";
	string aux;
	for (result::size_type i = 0; i != R.size(); ++i){
		output += "<option value='";
		output += R[i]["id"].as<string>()+"'>";
		aux = R[i]["nombre"].as<string>(); escape(aux);
		output += aux+" ";
		aux = R[i]["apellido"].as<string>(); escape(aux);
		output += aux;
		output += "</option>";
	}

	return output;
}

static PyObject* ver_redes( PyObject *self, PyObject *args ){
	const char * id_proyecto;
	if(!PyArg_ParseTuple(args,"s",&id_proyecto)) return NULL;
	return Py_BuildValue("s",ver_redes(id_proyecto).c_str());
}


static PyMethodDef redes_metodos[]={
	{"ver_personas",(PyCFunction)ver_personas,METH_VARARGS},
	{"ver_redes",(PyCFunction)ver_redes,METH_VARARGS},
	{NULL,NULL,0,NULL}
};

PyMODINIT_FUNC initredes(void){
	Py_InitModule("redes",redes_metodos);
}
