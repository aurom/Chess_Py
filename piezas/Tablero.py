class Tablero(object):
	"""Constructor """
	def __init__(self):
		tablero = [[0 for x in range(8)] for x in range(8)] 

	"""Regresa la matriz donde se encuentran todas las piezas"""
	def getTablero(self):
		return self.tablero

	"""Agrega una pieza al tablero en la 
	posicion que se pasa como parametro"""
	def agregaPieza(self, pieza, posicion):
		self.tablero[posicion[0]][[1]] = pieza


	