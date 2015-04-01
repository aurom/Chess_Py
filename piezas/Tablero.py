class Tablero(object):
	"""Constructor """
	def __init__(self):
		self.tablero = [[0 for x in range(8)] for x in range(8)] 
		#falta inicar todas las piezas en el lugar done les corresponde
		#Falta poner siempre posicion actual del rey
	

	#Es como el toString del tablero solo imprime el contenido 
	def __str__(self):
		res = ""
		for filas in self.tablero:
			for pieza in filas:
				if (pieza != 0):
					res += pieza.__str__() + " "
				else: 
					res += "0 "
			res += "\n"
		return res 

	"""Regresa la matriz donde se encuentran todas las piezas"""
	def getTablero(self):
		tabla = self.tablero
		return tabla 

	"""Agrega una pieza al tablero en la 
	que se pasa como parametro"""
	def agregaPieza(self, pieza):
		pos = pieza.get_posicion()
		self.tablero[pos[0]][pos[1]] = pieza


	"""Recibe n argumentos (Piezas) y las agrega"""
	def agregaMuchasPiezas(self, *args):
		for p in args:
			self.agregaPieza(p)

	"""Elimina una pieza del tablero, 
	recibe una tupla de la posicion a eliminar"""
	def eliminaPieza(self, pos):
		x = pos[0]
		y = pos[1]
		self.tablero[x][y] = 0
	"""
	Mueve una piezas a la posicion que se pasa como parametro
	NO MOVER A MENOS QUE SE HAYA COMPROBADO QUE ES UN MOVIMIENTO VÁLIDO
	CUANDO SE MUEVA UNA PIEZA EL ESPACIO EN DONDE ESTABA SE ASIGNA A CERO
	PARA SABER QUE ESTA DISPONIBLE
	"""
	def mueve(self, pieza, coordenada):
		#NOTA: Checar si es peón rey o torre y cmabiar su variable movida; Falta enroque
		movimientos = pieza.get_movimientos(self)
		if (not coordenada in movimientos): #No es un movimiento válido
			return 
		else: #Lo movemos
			self.eliminaPieza(pieza.get_posicion()) #eliminamos la pieza del tablero
			x = coordenada[0]
			y = coordenada[1]
			self.tablero[x][y] = pieza

			# si es Peon o Torre o Rey su variable movida se cambia 
			if (pieza.getClass() == 'Peon' or pieza.getClass() == 'Rey' 
				or pieza.getClass() == 'Torre'):

				pieza.movida = True 



