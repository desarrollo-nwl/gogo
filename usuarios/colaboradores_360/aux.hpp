#include <Python.h>
#include <iostream>
#include <pqxx/pqxx>

using namespace std;
using namespace pqxx;

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

int insertar( string sql )
{
   try{
	  connection C( "dbname=testdb "
	  				"user=suidi "
					"password=Su1357*- "
	  				"hostaddr=127.0.0.1 port=5432"
					);
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
	   connection C( "dbname=gogo "
  				   "user=suidi "
  				   "password=Su1357*- "
  				   "hostaddr=127.0.0.1 port=5432"
  				   );
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
	   connection C( "dbname=gogo "
 				  "user=suidi "
 				  "password=Su1357*- "
 				  "hostaddr=127.0.0.1 port=5432"
 				  );

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
