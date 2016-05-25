package main

import(
	_ "github.com/lib/pq"
	"database/sql"
	"time"
	"log"
)

var (
	db *sql.DB
	local *time.Location

	sql_proyectos = ``
	sql_datos = ``

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
	instrumento_id	int
	sumatoria		int
	contador		int
	promedio		float64
	respuestas		[]respuestas
}

type instrumento struct {
	id 				string
	nombre			string
	preguntas		[]pregunta
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

	local, err = time.LoadLocation("America/Bogota")

	/*==========================================================================
		Query Proyectos
	==========================================================================*/

	proys, err := db.Query( sql_proyectos )
	defer proys.Close()
	if err != nil {
		log.Print(err)
		panic("Error recibiendo proyectos")
	}

	var pro proyectos
	var pros []proyectos
	for filas.Next(){
		err = filas.Scan(&pro.id, &pro.ciclico, &pro.ciclos, &pro.dimensiones)
		pros = append(pros,pro)
	}

	/*==========================================================================
		Conteo para cada proyecto
	==========================================================================*/

	for i := range proyectos {

		// Datos de instrumentos
		rows, err := db.Query( sql_instrumentos,  proyectos[i].id )
		defer rows.Close()
		if err != nil {
			log.Print(err)
		}
		var inst instrumento
		ind_instrumentos := make(map[string]intrumentos)
		for rows.Next() {
			err = rows.Scan( &inst.id, &inst.nombre )
			if err != nil {
				log.Print(err)
			}
			ind_instrumentos[&inst.id] = inst
		}

		// Datos de los encuestados
		rows, err := db.Query( sql_encuestados,  proyectos[i].id )
		if err != nil {
			log.Print(err)
		}
		ind_persona := make(map[int]persona)
		for rows.Next() {
			var human persona
			err = rows.Scan( &human.id, &human.regional, &human.ciudad, &human.area, &human.cargo )
			if err != nil {
				log.Print(err)
			}
			ind_persona[human.id] = human
		}

		// Datos del proyecto
		rows, err = db.Query( sql_datos,  proyectos[i].id )
		if err != nil {
			log.Print(err)
		}
		var data datos
		ind_datos := make(map[int]persona)
		for rows.Next() {
			err = rows.Scan( &data.user, &data.pregunta, &data.respuesta, &data.fecha )
			if err != nil {
				log.Print(err)
			}
			ind_datos[data.user] = data
		}




	}





	log.Print("Hola mundo")
}
