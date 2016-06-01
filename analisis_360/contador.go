package main

import(
	// "encoding/json"
	_ "github.com/lib/pq"
	"database/sql"
	"time"
	"fmt"
	// js "github.com/bitly/go-simplejson"
)

var (
	db *sql.DB
	// local *time.Location

	sql_proyectos = `
		SELECT "id", "ciclico", "ciclos" FROM "cuestionarios_proyectos"
		WHERE "tipo" = '360 redes' OR "tipo" = '360 unico';`

	sql_respuestas = `
	SELECT
		"cuestionarios_360_respuestas"."id", "cuestionarios_360_respuestas"."numerico",
		"cuestionarios_360_respuestas"."pregunta_id", "cuestionarios_360_respuestas"."texto",
		"cuestionarios_360_preguntas"."id", "cuestionarios_360_preguntas"."multiple",
		"cuestionarios_360_preguntas"."texto", "cuestionarios_360_preguntas"."variable_id",
		"cuestionarios_360_variables"."id", "cuestionarios_360_variables"."dimension_id",
		"cuestionarios_360_variables"."nombre", "cuestionarios_360_dimensiones"."id",
		"cuestionarios_360_dimensiones"."instrumento_id", "cuestionarios_360_dimensiones"."nombre",
		"cuestionarios_360_instrumentos"."id", "cuestionarios_360_instrumentos"."nombre",
		"cuestionarios_360_instrumentos"."proyecto_id"
	FROM "cuestionarios_360_respuestas"
	INNER JOIN "cuestionarios_360_preguntas"
		ON ( "cuestionarios_360_respuestas"."pregunta_id" = "cuestionarios_360_preguntas"."id" )
	LEFT OUTER JOIN "cuestionarios_360_variables"
		ON ( "cuestionarios_360_preguntas"."variable_id" = "cuestionarios_360_variables"."id" )
	LEFT OUTER JOIN "cuestionarios_360_dimensiones"
		ON ( "cuestionarios_360_variables"."dimension_id" = "cuestionarios_360_dimensiones"."id" )
	LEFT OUTER JOIN "cuestionarios_360_instrumentos"
		ON ( "cuestionarios_360_dimensiones"."instrumento_id" = "cuestionarios_360_instrumentos"."id" )
	WHERE "cuestionarios_360_preguntas"."proyecto_id" = $1`

	// sql_datos = ``
	// sql_dummie = `
	// 	SELECT "respuesta" FROM "mensajeria_360_streaming" WHERE "id" = 40`
)

/*==============================================================================
	Estructuras de participacion
==============================================================================*/

type cargo struct {
	nombre			string
	total			int
	contestadas		int
}

type area struct {
	nombre			string
	total			int
	contestadas		int
	cargos			[]cargo
}

type ciudad struct {
	nombre			string
	total			int
	contestadas		int
	areas			[]area
}

type regional struct {
	nombre			string
	total			int
	contestadas		int
	ciudades		[]ciudad
}

/*==============================================================================
	Estructuras de analisis
==============================================================================*/

type datos struct {
	user			int
	pregunta		int
	respuesta		string
	fecha			time.Time
}

type respuesta struct {
	texto			string
	valor			int
	pregunta_id		string
}

type pregunta struct {
	id				string
	texto			string
	multiple		bool
	sumatoria		int
	contador		int
	promedio		float64
	respuestas		[]respuesta
}

type variable struct {
	id				string
	nombre			string
	sumatoria		int
	contador		int
	promedio		float64
	preguntas		[]pregunta
}

type dimension struct {
	id				string
	nombre			string
	sumatoria		int
	contador		int
	promedio		float64
	Variables		[]variable
}

type instrumento struct {
	id 				string
	nombre			string
	dimensiones		[]dimension
}

type proyecto struct {
	id				int
	ciclico			bool
	ciclos			int
}

type persona struct {
	id 				int
	regional		string
	ciudad			string
	area			string
	cargo			string
	instrumentos	[]instrumento
}


func main() {

	/*==========================================================================
		Variables globales
	==========================================================================*/

	var err error
	db, err = sql.Open("postgres", "user=suidi dbname=gogo password=Su1357*- sslmode=disable")
	defer db.Close()
	if err != nil {
		panic("Error conectando BD")
	}

	/*==========================================================================
		Query Proyectos
	==========================================================================*/

	proys, err := db.Query( sql_proyectos )
	defer proys.Close()
	if err != nil {
		fmt.Println(err)
		panic("Error recibiendo proyectos")
	}

	var pro proyecto
	var pros []proyecto
	for proys.Next(){
		err = proys.Scan(&pro.id, &pro.ciclico, &pro.ciclos )
		pros = append(pros,pro)
	}

	/*==========================================================================
	 	Conteo para cada proyecto
	==========================================================================*/
	fmt.Println(pros)
	for i := range pros {

		if pros[i].ciclico == true {

		} else {

			// Datos de instrumentos
			// rows, err := db.Query( sql_instrumentos,  pros[i].id )
			// defer rows.Close()
			// if err != nil {
			// 	fmt.Println(err)
			// }
			// var inst instrumento

			ind_instrumentos := map[string]map[string]variable
			var vars variable
			ind_instrumentos["2"]["3"] = ind_dimensiones["2"]
			fmt.Println(ind_instrumentos)

			// fmt.Println(ind_instrumentos)

			// for rows.Next() {
			// 	err = rows.Scan( &inst.id, &inst.nombre )
			// 	if err != nil {
			// 		fmt.Println(err)
			// 	}
			// 	ind_instrumentos[inst.id] = inst
			// }

			// Datos de los encuestados
			// rows, err := db.Query( sql_encuestados,  proyectos[i].id )
			// if err != nil {
			// 	fmt.Println(err)
			// }
			// ind_persona := make(map[int]persona)
			// for rows.Next() {
			// 	var human persona
			// 	err = rows.Scan( &human.id, &human.regional, &human.ciudad, &human.area, &human.cargo )
			// 	if err != nil {
			// 		fmt.Println(err)
			// 	}
			// 	ind_persona[human.id] = human
			// }
			//
			// // Datos del proyecto
			// rows, err = db.Query( sql_datos,  proyectos[i].id )
			// if err != nil {
			// 	fmt.Println(err)
			// }
			// var data datos
			// ind_datos := make(map[int]persona)
			// for rows.Next() {
			// 	err = rows.Scan( &data.user, &data.pregunta, &data.respuesta, &data.fecha )
			// 	if err != nil {
			// 		fmt.Println(err)
			// 	}
			// 	ind_datos[data.user] = data
			// }
		}
	}




	// var cadena string
	// err = db.QueryRow(sql_dummie).Scan(&cadena)
	// if err != nil {
	// 	fmt.Println(err)
	// }
	//
	// json_r, err := js.NewJson([]byte(cadena))
	// if err != nil {
	// 	fmt.Println(err)
	// }
	//
	// for i := 0; ; {
	// 	cadena, err = json_r.GetIndex(i).Get("r").String()
	// 	if err != nil {
	// 		fmt.Println(err)
	// 		break
	// 	} else {
	// 		fmt.Println( cadena )
	// 		i++
	// 	}
	// }
	//
	// var resp respuestas
	// json.Unmarshal( []byte(cadena), &resp)
	// fmt.Println(resp)
	// local, err = time.LoadLocation("America/Bogota")



	fmt.Println("Hola mundo")
}
