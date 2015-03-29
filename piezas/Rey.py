#-*- coding: utf-8 -*-
from Pieza import Pieza
from Color import Color 
from Tablero import Tablero


"""Clase para pieza Rey""" 
class Rey(Pieza):
	""" Constructor de Rey
		Recibe la coordenada inicial en forma de tupla
		Recibe también un color de la clase Enum Color
	"""
	def __init__(self, _current, color):
		super(Rey, self).__init__(_current, color) #LLama al constructor de la super clas
		
	#Tostring 
	def __str__(self):
		return "♜"

	#@Override
	def get_movimientos(self, tablero):
		matriz = tablero.getTablero()
		x = self._current[0]
		y = self._current[1]
		color = self.get_color() 
		lista = list() #lista de movimientos

		#Trata de moverse arriba
		i = x-1
		if self.enRango(i):
			if (matriz[i][y] == 0 and not (self.check((i, y), tablero))):
				lista.append((i, y))

		#Trata de moverse abajo
		i = x+1
		if self.enRango(i):
			if (matriz[i][y] == 0 and not (self.check((i, y), tablero))):
				lista.append((i, y))

		#Trata de mover a la izq
		i = y-1
		if self.enRango(i):
			if (matriz[x][i] == 0 and not (self.check((x, i), tablero))):
				lista.append((x, i))

		#Trata de mover a la der
		i = y+1
		if self.enRango(i):
			if (matriz[x][i] == 0 and not (self.check((x, i), tablero))):
				lista.append((x, i))

		#Trata de moverse esquina superior izquierda
		i = x-1
		j = y-1
		if self.enRango(i) and self.enRango(j): #
			if (matriz[i][j] == 0 and not (self.check((i, j), tablero))):
				lista.append((i, j))

		#Trata de moverse esquina superior derecha
		i = x-1
		j = y+1
		if self.enRango(i) and self.enRango(j): #
			if (matriz[i][j] == 0 and not (self.check((i, j), tablero))):
				lista.append((i, j))

		#Trata de moverse esquina inferior izquierda
		i = x+1
		j = y-1
		if self.enRango(i) and self.enRango(j): #
			if (matriz[i][j] == 0 and not (self.check((i, j), tablero))):
				lista.append((i, j))

		#Trata de moverse esquina inferior derecha
		i = x-1
		j = y+1
		if self.enRango(i) and self.enRango(j): #
			if (matriz[i][j] == 0 and not (self.check((i, j), tablero))):
				lista.append((i, j))

		return lista	


	"""Comprueba si el rey está en jaque. Regresa True 
	si está en jaque False en caso contrario"""
	def esta_en_jaque(self, tablero):
		matriz = tablero.getTablero()
		x = self._current[0]
		y = self._current[1]
		color = self.get_color() 

		i = x-1
		while self.enRango(i): #Revisa hacia arriba del tablero
			#Si se encuentra una pieza de dieferente color debe ser Torre o dama para ser jaque
			pieza = matriz[i][y]
			if (pieza != 0 and pieza.get_color() != self.color):
				if (pieza.getClass() == "Dama" or pieza.getClass() == "Torre"): 
					return True 
			elif (pieza != 0 and pieza.get_color() == self.color): 
				break #se encontró una pieza suya en la columna 
			i -= 1

		i = x+1
		while self.enRango(i): #Revisa hacia aabajo del tablero
			#Si se encuentra una pieza de dieferente color debe ser Torre o dama para ser jaque
			pieza = matriz[i][y] 
			if (pieza != 0 and pieza.get_color() != self.color):
				if (pieza.getClass() == "Dama" or pieza.getClass() == "Torre"):
					return True 
			elif (pieza != 0 and pieza.get_color() == self.color): 
				break #se encontró una pieza suya en la columna 
			i += 1

		#Revisa en la misma fila  a la derecha
		j = y+1
		while self.enRango(j):
			#Si se encuentra una pieza de dieferente color debe ser Torre o dama para ser jaque
			pieza = matriz[x][j] 
			if (pieza != 0 and pieza.get_color() != self.color):
				if (pieza.getClass() == "Dama" or pieza.getClass() == "Torre"):
					return True 
			elif (pieza != 0 and pieza.get_color() == self.color): 
				break #se encontró una pieza suya en la columna 
			j += 1

		#Revisa en la misma fila  a la Izquierda
		j = y-1
		while self.enRango(j):
			#Si se encuentra una pieza de dieferente color debe ser Torre o dama para ser jaque
			pieza = matriz[x][j] 
			if (pieza != 0 and pieza.get_color() != self.color):
				if (pieza.getClass() == "Dama" or pieza.getClass() == "Torre"):
					return True 
			elif (pieza != 0 and pieza.get_color() == self.color): 
				break #se encontró una pieza suya en la columna 
			j -= 1

		#Revisa diagonal superior izq
		i = x-1
		j = y-1
		while self.enRango(i) and self.enRango(j): 
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.get_color() != self.color):
				if (pieza.getClass() == "Dama" or pieza.getClass() == "Alfil"):
					return True
			elif (pieza != 0 and pieza.get_color() == self.color): 
				break 
			i -= 1
			j -= 1

		#Revisa diagonal superior derecha
		i = x-1
		j = y+1
		while self.enRango(i) and self.enRango(j): 
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.get_color() != self.color):
				if (pieza.getClass() == "Dama" or pieza.getClass() == "Alfil"):
					return True
			elif (pieza != 0 and pieza.get_color() == self.color): 
				break 
			i -= 1
			j += 1

		#Revisa diagonal inferior izq
		i = x+1
		j = y-1
		while self.enRango(i) and self.enRango(j): 
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.get_color() != self.color):
				if (pieza.getClass() == "Dama" or pieza.getClass() == "Alfil"):
					return True
			elif (pieza != 0 and pieza.get_color() == self.color): 
				break 
			i += 1
			j -= 1

		#Revisa diagonal inferior derecha
		i = x+1
		j = y+1
		while self.enRango(i) and self.enRango(j): 
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.get_color() != self.color):
				if (pieza.getClass() == "Dama" or pieza.getClass() == "Alfil"):
					return True
			elif (pieza != 0 and pieza.get_color() == self.color): 
				break 
			i += 1
			j += 1
		#**********Revisa por Caballos ES MUUUUY LARGOOO*********
		i = x-2
		j = y+1
		if self.enRango(i) and self.enRango(j):
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.get_color() != color and pieza.getClass() == 'Caballo'):
					return True 

		i = x-1
		j = y+2
		if self.enRango(i) and self.enRango(j):
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.get_color() != color and pieza.getClass() == 'Caballo'):
					return True


		i = x+1
		j = y+2
		if self.enRango(i) and self.enRango(j):
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.get_color() != color and pieza.getClass() == 'Caballo'):
					return True


		i = x+2
		j = y+1
		if self.enRango(i) and self.enRango(j):
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.get_color() != color and pieza.getClass() == 'Caballo'):
					return True


		i = x+2
		j = y-1
		if self.enRango(i) and self.enRango(j):
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.get_color() != color and pieza.getClass() == 'Caballo'):
					return True

		i = x+1
		j = y-2
		if self.enRango(i) and self.enRango(j):
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.get_color() != color and pieza.getClass() == 'Caballo'):
					return True

		i = x-1
		j = y-2
		if self.enRango(i) and self.enRango(j):
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.get_color() != color and pieza.getClass() == 'Caballo'):
					return True

		i = x-2
		j = y-1
		if self.enRango(i) and self.enRango(j):
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.get_color() != color and pieza.getClass() == 'Caballo'):
				return True

		#***Fin del caballo***
		#checa por jques por peon según color
		if (self.color == Color.blanco): #Si es blaco checa diagonales superiores
			i = x-1
			j = y-1
			if self.enRango(i) and self.enRango(j):
				pieza = matriz[i][j]
				if (pieza != 0 and pieza.get_color() != self.color and pieza.getClass() == 'Peon'):
					return True 

			i = x-1
			j = y+1
			if self.enRango(i) and self.enRango(j):
				pieza = matriz[i][j]
				if (pieza != 0 and pieza.get_color() != self.color and pieza.getClass() == 'Peon'):
					return True 

		else: #Ees un rey negro

			i = x+1
			j = y-1
			if self.enRango(i) and self.enRango(j):
				pieza = matriz[i][j]
				if (pieza != 0 and pieza.get_color() != self.color and pieza.getClass() == 'Peon'):
					return True 

			i = x+1
			j = y+1
			if self.enRango(i) and self.enRango(j):
				pieza = matriz[i][j]
				if (pieza != 0 and pieza.get_color() != self.color and pieza.getClass() == 'Peon'):
					return True

		return False 


	"""PRIVADO comprueba si el rey ESTARÁ en jaque en la posicion dada como parametro"""
	def check(self, tablero, pos):
		tablero_tmp = Tablero()
		#Hago un tablero temporal para simular el movimiento
		tablero_tmp.tablero = tablero.tablero 
		rey = Rey(pos, self.get_color())
		 

		tablero_tmp.eliminaPieza(self._current)
		tablero_tmp.agregaPieza(rey)

		return rey.esta_en_jaque(tablero_tmp)