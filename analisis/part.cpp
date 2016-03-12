// x86_64-linux-gnu-gcc -pthread -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -fPIC -I/usr/include/python2.7 -I/usr/include/postgresql -lpqxx -lpq -march=corei7-avx -c part.cpp -o part.o && c++ -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -D_FORTIFY_SOURCE=2 -g -fstack-protector --param=ssp-buffer-size=4 -Wformat -Werror=format-security -march=corei7-avx -lpqxx -lpq -o part.so -O3
#include <Python.h>
#include <iostream>
#include <pqxx/pqxx>

using namespace std;
using namespace pqxx;

string fecha(string entrada){
	string out;
	out.reserve(23);
	string anio = entrada.substr (0,4);
	string mes = entrada.substr (5,2);
	string dia = entrada.substr (8,2);
	out += "new Date(";
	out += anio;
	out += ",";
	out +=  mes;
	out += "-1,";
	out +=  dia;
	out += "),`";
	return out;
}


string query(string id_proyecto) {
	string output ="[ ";
	try {
		// connection C("dbname=gogo user=usuariodb_gogo password='W#y2d@uV4+eSPuwrEc$UTrE4eCruTHas' hostaddr=127.0.0.1 port=5432");
		connection C("dbname=gogo user=suidi password='Su1357*-' hostaddr=127.0.0.1 port=5432");
		if (C.is_open()) {

			try {
                nontransaction N(C);
                string sql = "SELECT "
								"mensajeria_streaming.colaborador_id, "
								"mensajeria_streaming.proyecto_id, "
								"mensajeria_streaming.fecharespuesta, "
								"mensajeria_streaming.respuesta, "
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
								"colaboradores_datos.regional, "
								"cuestionarios_proyectos.id, "
								"usuarios_proyectosdatos.id_id, "
								"usuarios_proyectosdatos.opcional1 AS popcional1, "
								"usuarios_proyectosdatos.opcional2 AS popcional2, "
								"usuarios_proyectosdatos.opcional3 AS popcional3, "
								"usuarios_proyectosdatos.opcional4 AS popcional4, "
								"usuarios_proyectosdatos.opcional5 AS popcional5 "
							"FROM  mensajeria_streaming "
							"INNER JOIN cuestionarios_proyectos "
								"ON ( mensajeria_streaming.proyecto_id = cuestionarios_proyectos.id ) "
							"INNER JOIN colaboradores_colaboradores "
								"ON ( mensajeria_streaming.colaborador_id = colaboradores_colaboradores.id ) "
							"LEFT OUTER JOIN colaboradores_datos "
								"ON ( colaboradores_colaboradores.id = colaboradores_datos.id_id ) "
							"LEFT OUTER JOIN usuarios_proyectosdatos "
								"ON ( cuestionarios_proyectos.id = usuarios_proyectosdatos.id_id ) "
							"WHERE mensajeria_streaming.proyecto_id = "+id_proyecto+";";
				result R( N.exec( sql ));


				for (result::size_type i = 0; i != R.size(); ++i){
					output += "[ `";
					try { output += R[i]["regional"].as<string>()+"`,`"; }
						catch (const exception &e){ output += "`,`"; }
					try { output += R[i]["ciudad"].as<string>()+"`,`"; }
						catch (const exception &e){ output += "`,`"; }
					try { output += R[i]["area"].as<string>()+"`,`"; }
						catch (const exception &e){ output += "`,`"; }
					try { output += R[i]["cargo"].as<string>()+"`,`"; }
						catch (const exception &e){ output += "`,`"; }
					try { output += R[i]["genero"].as<string>()+"`,`"; }
						catch (const exception &e){ output += "`,`"; }
					try { output += R[i]["niv_academico"].as<string>()+"`,`"; }
						catch (const exception &e){ output += "`,`"; }
					try { output += R[i]["profesion"].as<string>()+"`,"; }
						catch (const exception &e){ output += "`,"; }
					try {
						R[i]["respuesta"].as<string>();
						output += "true,";
					}
						catch (const exception &e){ output += "false,"; }
					try {
						output += fecha(R[i]["fecharespuesta"].as<string>());
					}
						catch (const exception &e){ output += "0,`"; }
					try { output += R[i]["opcional1"].as<string>()+"`,`"; }
						catch (const exception &e){ output += "`,`"; }
					try { output += R[i]["opcional2"].as<string>()+"`,`"; }
						catch (const exception &e){ output += "`,`"; }
					try { output += R[i]["opcional3"].as<string>()+"`,`"; }
						catch (const exception &e){ output += "`,`"; }
					try { output += R[i]["opcional4"].as<string>()+"`,`"; }
						catch (const exception &e){ output += "`,`"; }
					try { output += R[i]["opcional5"].as<string>()+"`],"; }
						catch (const exception &e){ output += "`],"; }
				}
				output += "]";

			} catch (const exception &e) {
			   cerr << e.what() << endl;
            }
            //fin del codigo del programa

			C.disconnect();

		} else {
			cout << "No se pudo conectar la BD." << endl;;
		}
		//fin if conexion abierta


	} catch (const exception &e){
		cerr << e.what() << endl;
	}
	// fin try principal

	// const char *C = output.c_str();
	// cout << output.c_str() << endl;
	return output;
}


static PyObject* query( PyObject *self, PyObject *args ){
	const char * id_proyecto;
	if(!PyArg_ParseTuple(args,"s",&id_proyecto)) return NULL;
	return Py_BuildValue("s",query(id_proyecto).c_str());
}


static PyMethodDef part_metodos[]={
	{"query",(PyCFunction)query,METH_VARARGS},
	{NULL,NULL,0,NULL}
};

PyMODINIT_FUNC initpart(void){
	Py_InitModule("part",part_metodos);
}
