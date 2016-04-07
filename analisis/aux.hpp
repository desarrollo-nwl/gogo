#include <Python.h>
#include <iostream>
#include <pqxx/pqxx>
#include <ctemplate/template.h>

using namespace std;
using namespace pqxx;

// string CREDENCIALES = "dbname=gogo user=usuariodb_gogo password='W#y2d@uV4+eSPuwrEc$UTrE4eCruTHas' hostaddr=127.0.0.1 port=5432";
string CREDENCIALES = "dbname=gogo user=suidi password=Su1357*- hostaddr=127.0.0.1 port=5432";

// char raiz[150] = "/home/ubuntu/gogo/";
char raiz[50] = "/home/suidi/workspace/gogo/";


void escape(string& data) {
    string buffer;
    buffer.reserve(data.size());
    for(size_t pos = 0; pos != data.size(); ++pos) {
        switch(data[pos]) {
            case '&':  buffer.append("&amp;");       break;
            case '\"': buffer.append("&quot;");      break;
            case '\'': buffer.append("&apos;");      break;
            case '<':  buffer.append("&lt;");        break;
            case '>':  buffer.append("&gt;");        break;
            default:   buffer.append(&data[pos], 1); break;
        }
    }
    data.swap(buffer);
}

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
	out += ")";
	return out;
}

int insertar( string sql )
{
   try{
	   connection C( CREDENCIALES );
	  if ( !C.is_open() ){
		 cout << "conexion fallida" << endl;
		 return 1;
	  }

	  /* Creacion de un objeto transaccional. */
	  work W(C);

	  /* Ejecutamos el SQL query */
	  W.exec( sql );
	  W.commit();

	  C.disconnect ();
   }catch (const exception &e){
	  cerr << e.what() << endl;
	  return 1;
   }

   return 0;
}

result leer( string sql )
{
   try{
	   connection C( CREDENCIALES );
	  if ( !C.is_open() ){
		 cout << "conexion fallida" << endl;
		 result R;
		 return R;
	  }

	  /* Creacion de un objeto notransaccional */
	  nontransaction N(C);

	  /* Ejecutamos SQL query */
	  result R( N.exec( sql ) );
	  C.disconnect ();
	  return R;

   } catch (const exception &e){
	  cerr << e.what() << endl;
	  result R;
	  return R;
   }

}


int actualizar(string sql)
{
	try{
	 	connection C( CREDENCIALES );

		if ( !C.is_open() ){
			cout << "conexion fallida" << endl;
			return 1;
		}

		/* Creacion de un objeto transaccional. */
		work W(C);

		/* Ejectamos SQL query */
		W.exec( sql );

		W.commit();

		C.disconnect ();

	} catch (const exception &e){
	  cerr << e.what() << endl;
	  return 1;
	}

   return 0;
}

struct Proyecto {
	bool activo ;
	bool interna ;
	float total ;
	int tot_preguntas ;
	int tot_respuestas ;
	string ffin ;
	string finicio ;
	string max_variables ;
	string nombre ;
	string opcional1 ;
	string opcional2 ;
	string opcional3 ;
	string opcional4 ;
	string opcional5 ;
	string tipo ;
	string tot_aresponder ;
	string tot_participantes ;
};

struct Permisos {
	bool col_add ;
	bool col_see ;
	bool consultor ;
	bool res_exp ;
	bool var_add ;
	bool var_see ;
};
