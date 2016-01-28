# -*- encoding: utf-8 -*-
import numpy as np
import sys
sys.setrecursionlimit(2000)
#############################
#~ datasetgrafo = [
                 #~ ["pregunta1","este es un comentario","la gloria de belén","Veamos como funciona"],
                 #~ ["pregunta2","trabajo en equipo","vamos pastores, vamos","porque que no puedo estar donde ellos"],
                 #~ ["pregunta3","comunicación, confianza y respeto","De ahí vamos a otra parte","nunca piensan en ellos"],
                 #~ ["pregunta4","este es un nuevo comentario","como lograr esto","nosotros estabamos en la casa"],
                 #~ ["pregunta5","este es un  comentario","como lograr esto","nosotros estabamos nuevamente en la casa"],
                 #~ ]
#############################

#~ def matrizComentarios(datasetInfo):
	#~ comentarios = datasetInfo[1:]

datasetgrafo =[['Por favor escribe 3 aspectos que le ayudar dan a tu área HOY para lograr que el cambio sea exitoso',
				'El libro se abre con el retrato largo y detallado del obispo Bienvenue Myriel, el obispo de Digne, donde vive modestamente con su hermana Baptistine y de una criada, la señora Magloire. El religioso vive de solo lo que es necesario y distribuye el resto de sus ahorros para los pobres, siempre muestra un gran amor, deja la puerta abierta y confraterniza con aquellos a quienes la sociedad rechaza.',
				'Su destino se cruza con el personaje central de la obra: Jean Valjean.',
				'La acción comienza en 1815 con la llegada de Jean Valjean, el personaje principal de la obra, después de una sentencia de diecinueve años de prisión: víctima de un trágico destino, originalmente sentenciado a cinco años de prisión por robar pan para alimentar a su familia, ve ampliada su sentencia después de varios intentos de fuga. Su pasado como convicto lo abruma y en cada ciudad que pasa, escucha la negativa por ser un ex convicto con un pasaporte amarillo, universalmente rechazado; y sólo el obispo Myriel le abre la puerta para ofrecerle alimento y refugio. Jean Valjean, muestra un odio-amor y resentimiento con la sociedad. Sin ser muy consciente de sus actos, le roba su vajilla de plata al obispo y huye por la ventana. Cuando es detenido y llevado por la policía ante el obispo Myriel, éste cuenta a la policía que él le había regalado la vajilla de plata y que aún se había olvidado de darle dos candelabros del mismo metal, consiguiendo así que Valjean quede libre de nuevo. Después dice a Valjean que lo perdona y le ofrece los candelabros de plata, haciéndole prometer que redimirá su vida y se transformará en una persona de bien. Perdido en sus pensamientos, Valjean roba sin querer una moneda de 40 sueldos de un saboyano llamado Petit Gervais cubriéndolo con su pie. ',
				'Camaraderia, liderazgo y comunicación',
				'Ya he contestado esto tres veces. ',
				'Respeto, confianza, trabajo en equipo. Comunicación.',
				'conocimiento, respaldo, confianza, trabajo en equipo',
				'La señora y el señor Thenardier carecen de honradez ',
				'Trabajar, Mejorar, Ser Humilde',
				'Poder, Valor, Lealtad',
				'Totalmente de acuerdo',
				'XXX','zzz','hola mundo trascendental valor'],
				]

def SplitRespuestas(respuestas):
	SplitRespuesta = []
	for respuesta in respuestas:
		respuesta = respuesta.replace(',','').replace('.','').lower()
		SplitRespuesta.append(respuesta.split())
	return SplitRespuesta

# listaRespuestas = SplitRespuestas(datasetgrafo[0])

def creaDiccionario(dataset):
	conjuntoPalabras = set([])
	for data in dataset:
		conjuntoPalabras = conjuntoPalabras.union(data)
	return  list(conjuntoPalabras)

# diccPrueba = creaDiccionario(listaRespuestas)

def depuracionDiccionario(lista):
	z = []
	for i in range(len(lista)):
		if len(lista[i])>4:
			z.append(lista[i])
	z.append("no")
	z.append("si")
	return z

# diccPruebaDepurado = depuracionDiccionario(diccPrueba)
# print len(diccPruebaDepurado)
# print diccPruebaDepurado

def traduccionString(listadepurada,stringVector):
	vectorcodificado = [0]*len(listadepurada)
	for palabra in stringVector:
		if palabra in listadepurada:
			vectorcodificado[listadepurada.index(palabra)]=1
		#~ else:
			#~ print "la palabra %s no esta en el diccionario"% palabra
	return vectorcodificado



def traductorVectorial(matrizprueba,listaDepurada):
	z = []
	for comentario in matrizprueba:
		z.append(traduccionString(listaDepurada,comentario))
	return z

# respuestasPruebaVecoriales = traductorVectorial(listaRespuestas,diccPruebaDepurado)
# print len(respuestasPruebaVecoriales[0])
## CONTEO DE PALABRAS!!!!
def conteoPalabras(respuestasVectoriales):
	suma = [0]*len(respuestasVectoriales[0])
	suma = np.array(suma)
	for respuesta in respuestasVectoriales:
		suma += np.array(respuesta)
	return suma

# pruebita = conteoPalabras([[1,2,3],[2,3,4],[3,4,5]])
# print pruebita
# sumaPruebaVectoriales = conteoPalabras(respuestasPruebaVecoriales)
# print sumaPruebaVectoriales
# print len(sumaPruebaVectoriales)


# CONSTRUCCION DE GRAFOS
def BolsaEdges(v,bolsa):
	n = 0
	if len(v)==2:
		bolsa.append(v)
	else:
		for i in range(len(v)-1):
			bolsa.append([v[i],v[len(v)-1]])
		BolsaEdges(v[0:len(v)-1],bolsa)

	return bolsa


def Nodos(v):
	nodos = []
	for i in range(len(v)):
		if v[i]==1:
			nodos.append(i)
	return nodos

def hacerConexion(G,nodo1,nodo2):
	if nodo1 not in G:
		G[nodo1] = {}

	if nodo2 not in G[nodo1]:
		G[nodo1][nodo2]=1
	else:
		G[nodo1][nodo2]+=1

	if nodo2 not in G:
		G[nodo2]={}

	if nodo1 not in G[nodo2]:
		G[nodo2][nodo1]=1
	else:
		G[nodo2][nodo1]+=1


def ConstrucGrafo(graph,frase):
	for elemento in frase:
		hacerConexion(graph,elemento[0],elemento[1])


def GrafoTotal(graph,dataset):   ###graph = {} , dataset = [[1,0,1,0,1,1,0],[0,0,1,0,1,1]....]
	var = []
	var2 = []
	for frase1 in dataset:
		var.append(Nodos(frase1))

	for frase2 in var:
		if len(frase2)>1:
			var2.append(BolsaEdges(frase2,[]))

	for frase3 in var2:
		ConstrucGrafo(graph,frase3)

	return graph




def Grafos(datasetgrafo):
	grafos = []
	diccionarios = []
	cantidades =[]
	for vector in datasetgrafo:
		respuestas = vector[1:]
		respuestasSplit = SplitRespuestas(respuestas)
		diccionario = depuracionDiccionario(creaDiccionario(respuestasSplit))
		respuestasVectoriales = traductorVectorial(respuestasSplit,diccionario)
		sumaVectoriales = list(conteoPalabras(respuestasVectoriales))
		cantidades.append(sumaVectoriales)
		grafo = {}
		grafos.append(GrafoTotal(grafo,respuestasVectoriales))
		diccionarios.append(diccionario)
	return (grafos,diccionarios,cantidades)

def preguntas(dataini):
	listaPreguntas = []
	for data in dataini:
		 listaPreguntas.append(data[0])
	return listaPreguntas

# grafoPorPregunta,diccionariosPorPregunta,cantidades = Grafos(datasetgrafo)

#
#
# print len(grafoPorPregunta[0])
# print len(diccionariosPorPregunta[0])

# print diccionariosPorPregunta
