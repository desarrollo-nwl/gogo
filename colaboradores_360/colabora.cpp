#include "aux.hpp"

string ver_colaboradores(string id_proyecto, bool editar, bool eliminar) {
	// connection C("dbname=gogo user=usuariodb_gogo password='W#y2d@uV4+eSPuwrEc$UTrE4eCruTHas' hostaddr=127.0.0.1 port=5432");
	string sql =	"SELECT "
						"colaboradores_360_colaboradores.id, "
						"colaboradores_360_colaboradores.apellido, "
						"colaboradores_360_colaboradores.email, "
						"colaboradores_360_colaboradores.estado, "
						"colaboradores_360_colaboradores.nombre, "
						"colaboradores_360_colaboradores.externo, "
						"colaboradores_360_colaboradores.descripcion, "
						"colaboradores_360_datos.id_id, "
						"colaboradores_360_datos.cargo "
					"FROM "
						"colaboradores_360_colaboradores "
					"LEFT OUTER JOIN "
						"colaboradores_360_datos "
					"ON "
						"( colaboradores_360_colaboradores.id = colaboradores_360_datos.id_id ) "
					"WHERE "
						"colaboradores_360_colaboradores.proyecto_id ="+ id_proyecto +";";

	// ejecutamos el colaboradores
	result R = leer(sql);

	string output = "";
	string auxiliar;
	string id;
	for (result::size_type i = 0; i != R.size(); ++i){
		output += "<tr><td>";
		auxiliar = R[i]["nombre"].as<string>();
		escape(auxiliar);
		output += auxiliar + "</td><td>";
		auxiliar = R[i]["apellido"].as<string>();
		escape(auxiliar);
		output += auxiliar + "</td><td>";
		try{
			if(  R[i]["externo"].as<bool>() ){
				auxiliar = R[i]["descripcion"].as<string>();
				escape(auxiliar);
				output += auxiliar + "</td><td>";
			} else {
				auxiliar = R[i]["cargo"].as<string>();
				escape(auxiliar);
				output += auxiliar + "</td><td>";
			}
		} catch( const exception &e ){
			output += "</td><td>";
		}
		id = R[i]["id"].as<string>();
		auxiliar = R[i]["email"].as<string>();
		escape(auxiliar);
		output += auxiliar + "</td><td id='e"+id+"'>";

		if( R[i]["estado"].as<bool>() )
			output += "<span style='color:#1d9d73'>Activo</span></td><td>";
		else
			output += "<span style='color:#cd1e21'>Inactivo</span></td><td>";
		if( editar )
			output += "<span style='cursor:pointer;color:#1d9d73' onclick=\"actualizar("+id+")\" ><i class='fa fa-retweet m-r' title='Activar/Desactivar'></i></span><a href='/360/participante/editar/"+id+"/'><i class='fa fa-edit m-r' title='editar'></i></a>";
		if( eliminar )
			output += "<a href='/360/participante/eliminar/"+id+"/'><i class='fa fa-trash m-r' title='eliminar'></i></a></td></tr>";
		else
			output += "<td></tr>";

	}

	return output;
}


static PyObject* ver_colaboradores( PyObject *self, PyObject *args ){
	const char * id_proyecto;
	bool editar=false;
	bool eliminar=false;
	if(!PyArg_ParseTuple(args,"sbb",&id_proyecto,&editar,&eliminar)) return NULL;
	return Py_BuildValue("s",ver_colaboradores(id_proyecto,editar,eliminar).c_str());
}

static PyMethodDef colabora_metodos[]={
	{"ver_colaboradores",(PyCFunction)ver_colaboradores,METH_VARARGS},
	{NULL,NULL,0,NULL}
};

PyMODINIT_FUNC initcolabora(void){
	Py_InitModule("colabora",colabora_metodos);
}
