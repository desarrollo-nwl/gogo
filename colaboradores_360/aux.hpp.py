#include <Python.h>
#include <iostream>
#include <pqxx/pqxx>

using namespace std
using namespace pqxx

# CREDENCIALES = "dbname=gogo user=usuariodb_gogo password='W#y2d@uV4+eSPuwrEc$UTrE4eCruTHas' hostaddr=127.0.0.1 port=5432"
CREDENCIALES = "dbname=gogo user=suidi password=Su1357*- hostaddr=127.0.0.1 port=5432"

# char raiz[150] = "/home/ubuntu/gogo/"
char raiz[50] = "/home/suidi/Documentos/gogo/"


def escape(self, data):    string buffer
    buffer.reserve(data.size())
    for(pos = 0; pos != data.size(); ++pos)        switch(data[pos])            case '&':  buffer.append("&amp;");       break
            case '\"': buffer.append("&quot;");      break
            case '\'': buffer.append("&apos;");      break
            case '<':  buffer.append("&lt;");        break
            case '>':  buffer.append("&gt;");        break
            default:   buffer.append(&data[pos], 1); break


    data.swap(buffer)


def fecha(self, entrada):	string out
	out.reserve(23)
	anio = entrada.substr (0,4)
	mes = entrada.substr (5,2)
	dia = entrada.substr (8,2)
	out += "new Date("
	out += anio
	out += ","
	out +=  mes
	out += "-1,"
	out +=  dia
	out += ")"
	return out


def insertar(self, sql ):
   try	   connection C( CREDENCIALES )
	  if  not C.is_open() :		 cout << "conexion fallida" << endl
		 return 1


	  ''' Creacion de un objeto transaccional. '''
	  work W(C)

	  ''' Ejecutamos el SQL query '''
	  W.exec( sql )
	  W.commit()

	  C.disconnect ()
   }catch ( exception &e)	  cerr << e.what() << endl
	  return 1


   return 0


def leer(self, sql ):
   try	   connection C( CREDENCIALES )
	  if  not C.is_open() :		 cout << "conexion fallida" << endl
		 result R
		 return R


	  ''' Creacion de un objeto notransaccional '''
	  nontransaction N(C)

	  ''' Ejecutamos SQL query '''
	  result R( N.exec( sql ) )
	  C.disconnect ()
	  return R

   } catch ( exception &e)	  cerr << e.what() << endl
	  result R
	  return R





def actualizar(self, sql):
	try	 	connection C( CREDENCIALES )

		if  not C.is_open() :			cout << "conexion fallida" << endl
			return 1


		''' Creacion de un objeto transaccional. '''
		work W(C)

		''' Ejectamos SQL query '''
		W.exec( sql )

		W.commit()

		C.disconnect ()

	} catch ( exception &e)	  cerr << e.what() << endl
	  return 1


   return 0

