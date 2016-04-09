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
palabrasRestringidas = ['que', 'los', 'del', 'las', 'por', 'para', 'con', 'una',
						'pero', 'sus', 'este', 'porque', 'esta', 'entre', 'cuando', 'sobre', 'tambien', 'hasta', 'hay',
						'donde', 'quien', 'desde', 'todo', 'nos', 'durante', 'todos', 'uno', 'les', 'ni', 'contra', 'otros', 'ese', 'eso', 'ante',
						'ellos', 'esto', 'antes', 'algunos', 'que', 'unos', 'otro', 'otras', 'otra', 'tanto', 'esa', 'estos', 'quienes',
						'muchos', 'cual', 'poco', 'ella', 'estar', 'estas', 'algunas', 'algo', 'nosotros', 'mis', 'tus',
						'ellas', 'nosotras', 'vosostros', 'vosostras', 'mio', 'mia', 'mios', 'mias', 'tuyo', 'tuya', 'tuyos', 'tuyas', 'suyo', 'suya',
						'suyos', 'suyas', 'nuestro', 'nuestra', 'nuestros', 'nuestras', 'vuestro', 'vuestra', 'vuestros', 'vuestras', 'esos', 'esas', 'estoy',
						'estas', 'esta', 'estamos', 'estais', 'estan', 'este', 'estes', 'estemos', 'esteis', 'esten', 'estare', 'estaras', 'estara', 'estaremos',
						'estareis', 'estaran', 'estaria', 'estarias', 'estariamos', 'estariais', 'estarian', 'estaba', 'estabas', 'estabamos', 'estabais', 'estaban',
						'estuve', 'estuviste', 'estuvo', 'estuvimos', 'estuvisteis', 'estuvieron', 'estuviera', 'estuvieras', 'estuvieramos', 'estuvierais', 'estuvieran',
						'estuviese', 'estuvieses', 'estuviesemos', 'estuvieseis', 'estuviesen', 'estando', 'estado', 'estada', 'estados', 'estadas', 'estad', 'has',
						'hemos', 'habeis', 'han', 'haya', 'hayas', 'hayamos', 'hayais', 'hayan', 'habre', 'habras', 'habra', 'habremos', 'habreis', 'habran', 'habria',
						'habrias', 'habriamos', 'habriais', 'habrian', 'habia', 'habias', 'habiamos', 'habiais', 'habian', 'hube', 'hubiste', 'hubo', 'hubimos', 'hubisteis', 'hubieron',
						'hubiera', 'hubieras', 'hubieramos', 'hubierais', 'hubieran', 'hubiese', 'hubieses', 'hubiesemos', 'hubieseis', 'hubiesen', 'habiendo', 'habido', 'habida',
					   	'habidos', 'habidas', 'soy', 'eres','somos', 'sois', 'son', 'sea', 'seas', 'seamos', 'seais', 'sean', 'sere', 'seras', 'sera', 'seremos', 'sereis', 'seran',
						'seria', 'serias', 'seriamos', 'seriais', 'serian', 'era', 'eras', 'eramos', 'erais', 'eran', 'fui', 'fuiste', 'fue', 'fuimos', 'fuisteis', 'fueron', 'fuera',
						'fueras', 'fueramos', 'fuerais', 'fueran', 'fuese', 'fueses', 'fuesemos', 'fueseis', 'fuesen', 'sintiendo', 'sentido', 'sentida', 'sentidos', 'sentidas', 'siente',
						'sentid', 'tengo', 'tienes', 'tiene', 'tenemos', 'teneis', 'tienen', 'tenga', 'tengas', 'tengamos', 'tengais', 'tengan', 'tendre', 'tendras', 'tendra', 'tendremos',
						'tendreis', 'tendran', 'tendria', 'tendrias', 'tendriamos', 'tendriais', 'tendrian', 'tenia', 'tenias', 'teniamos', 'teniais', 'tenian', 'tuve', 'tuviste', 'tuvo', 'tuvimos',
						'tuvisteis', 'tuvieron', 'tuviera', 'tuvieras', 'tuvieramos', 'tuvierais', 'tuvieran', 'tuviese', 'tuvieses', 'tuviesemos', 'tuvieseis', 'tuviesen', 'teniendo', 'tenido', 'tenida',
						'tenidos', 'tenidas', 'tened','myself','our','ours','ourselves','you','your','yours','yourself','yourselves','him','his','himself','she','her',
						'hers','herself','its','itself','they','them','their','theirs','themselves','what','which','who','whom','this','that','these','those','are','was','were','be',
						'been','being','have','has','had','having','does','did','doing','the','and','but','because','until','while','for','with','about',
						'against','between','into','through','during','from','up','down','out','off','over','under','further','then','once','here','there','when','where','why','how',
						'all','any','both','each','few','more','most','other','some','such','nor','not','only','own','same','than','can','will','just','don','should','now']

palabrasAutorizadas = ['no',  'si', 'mi' ]


def depuracionDiccionario(lista):
	z = []
	for i in range(len(lista)):
		if len(lista[i])>2 and lista[i] not in palabrasRestringidas:
			z.append(lista[i])
	for m in palabrasAutorizadas:
		z.append(m)
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
