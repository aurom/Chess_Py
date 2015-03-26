class Tablero(object):
	"""Constructor """
	def __init__(self):
		tablero = [[0 for x in range(8)] for x in range(8)] 
		#falta inicar todas las piezas en el lugar done les corresponde
		#Falta poner siempre posicion actual del rey
		

	"""Regresa la matriz donde se encuentran todas las piezas"""
	def getTablero(self):
		return self.tablero

	"""Agrega una pieza al tablero en la 
	posicion que se pasa como parametro"""
	def agregaPieza(self, pieza, posicion):
		self.tablero[posicion[0]][[1]] = pieza

	"""
	Mueve una piezas a la posicion que se pasa como parametro
	NO MOVER A MENOS QUE SE HAYA COMPROBADO QUE ES UN MOVIMIENTO VÁLIDO
	"""
	def mueve(pieza, coordenada):
		#stuff
		pass 

	"""Elimina la pieza del tablero en caso de ser comida"""
	def eliminar_pieza(pieza):
		pass