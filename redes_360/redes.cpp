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


string ver_redes(string id_proyecto, bool editar, bool borrar) {
	string sql =
				"SELECT "
					"redes_360_Redes.id AS id, "
					"redes_360_Redes.colaborador_id, "
					"redes_360_Redes.evaluado_id, "
					"redes_360_Redes.instrumento_id, "
					"redes_360_Redes.rol, "
					"redes_360_Redes.rol_idn, "
					"colaboradores_360_colaboradores.id, "
					"colaboradores_360_colaboradores.apellido, "
					"colaboradores_360_colaboradores.nombre, "
					"T4.id, T4.apellido AS ape_eval, T4.nombre AS nom_eval, "
					"cuestionarios_360_instrumentos.id, "
					"cuestionarios_360_instrumentos.nombre AS nom_inst "
				"FROM "
					"redes_360_Redes "
				"INNER JOIN "
					"colaboradores_360_colaboradores "
				"ON "
					"( redes_360_Redes.colaborador_id = colaboradores_360_colaboradores.id ) "
				"INNER JOIN "
					"colaboradores_360_colaboradores T4 "
				"ON "
					"( redes_360_Redes.evaluado_id = T4.id )"
				"INNER JOIN "
					"cuestionarios_360_instrumentos "
				"ON "
					"( redes_360_Redes.instrumento_id = cuestionarios_360_instrumentos.id ) "
				"WHERE "
					"redes_360_Redes.proyecto_id = "+ id_proyecto +";";

	result R = leer(sql);

	string output = "";
	string aux;
	string id,nombre,apellido,rol,nom_eval,ape_eval,nom_inst;
	for (result::size_type i = 0; i != R.size(); ++i){
		id = R[i]["id"].as<string>();
		output += "<tr id=tr"+ id +"><td id=td"+id+">";
		nombre = R[i]["nombre"].as<string>(); escape(nombre);
		output += nombre + " ";
		apellido = R[i]["apellido"].as<string>(); escape(apellido);
		output += apellido +"</td><td >";
		rol = R[i]["rol"].as<string>(); escape(rol);
		output += rol +"</td><td >";
		nom_eval = R[i]["nom_eval"].as<string>(); escape(nom_eval);
		output += nom_eval +" ";
		ape_eval = R[i]["ape_eval"].as<string>(); escape(ape_eval);
		output += ape_eval +"</td><td>";
		nom_inst = R[i]["nom_inst"].as<string>(); escape(nom_inst);
		output += nom_inst +"</td><td style='min-width:210px' id='"+id+"' >";

		if ( editar ){
			output += "<span id='act"+id+"' style='cursor:pointer;color:#0bacd3' onclick=\"acciones.actualizar("+id+",'"+nombre+" "+apellido+"','"+rol+"','"+R[i]["rol_idn"].as<string>()+"','"+nom_eval+" "+ape_eval+"','"+nom_inst+"','"+R[i]["colaborador_id"].as<string>()+"','"+R[i]["evaluado_id"].as<string>()+"','"+R[i]["instrumento_id"].as<string>()+"')\"><i class='fa fa-edit mr20' title='Editar'></i></span>";
		}
		if ( borrar ){
			output += "<span id=d"+id+" style='cursor:pointer;color:#0bacd3' onclick=\"acciones.eliminar("+id+")\"><i class='fa fa-trash ml20' title='Eliminar'></i></span>";
		}

		output += "<span id='del"+id+"' style='display:none' class='btn btn-danger ml20' onclick=\"acciones.confirmado("+id+")\">Confirmar</span>";
		output += "<span id='can"+id+"' style='display:none' class='btn btn-warning ml20' onclick=\"acciones.cancelar("+id+",'"+nombre+" "+apellido+"','"+rol+"','"+R[i]["rol_idn"].as<string>()+"','"+nom_eval+" "+ape_eval+"','"+nom_inst+"','"+R[i]["colaborador_id"].as<string>()+"','"+R[i]["evaluado_id"].as<string>()+"','"+R[i]["instrumento_id"].as<string>()+"')\">Cancelar</span>";
		output += "<span id='env"+id+"' style='display:none' class='btn btn-success ml20' onclick=\"acciones.enviar("+id+")\">Confirmar</span></td></tr>";
	}

	return output;
}

static PyObject* ver_redes( PyObject *self, PyObject *args ){
	const char * id_proyecto;
	bool editar;
	bool borrar;
	if(!PyArg_ParseTuple(args,"sbb",&id_proyecto,&editar,&borrar)) return NULL;
	return Py_BuildValue("s",ver_redes(id_proyecto,editar,borrar).c_str());
}


static PyMethodDef redes_metodos[]={
	{"ver_personas",(PyCFunction)ver_personas,METH_VARARGS},
	{"ver_redes",(PyCFunction)ver_redes,METH_VARARGS},
	{NULL,NULL,0,NULL}
};

PyMODINIT_FUNC initredes(void){
	Py_InitModule("redes",redes_metodos);
}
