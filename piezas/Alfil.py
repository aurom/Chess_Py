#-*- coding: utf-8 -*-
from Pieza import Pieza
from Color import Color 
"""Clase para pieza Alfil""" 
class Alfil(Pieza):
	""" Constructor de Alfil
		Recibe la coordenada inicial en forma de tupla
		Recibe también un color de la clase Enum Color
	"""
	def __init__(self, _current, color):
		super(Alfil, self).__init__(_current, color) #LLama al constructor de la super clas
		
	#Tostring 
	def __str__(self):
		if (self.color == Color.blanco): return "♝"
		else : return "♗"

	#@Override
	def get_movimientos(self, tablero):
		"""Revisaremos sus cuatro diagonales"""
		matriz = tablero.getTablero()
		x = self._current[0]
		y = self._current[1]
		color = self.get_color() 
		lista = list() #lista de movimientos

		i = x-1
		j = y-1
		while self.enRango(i) and self.enRango(j): #Diagonal superior izquierda los indices irán de -1 en -1
			if (matriz[i][j] == 0): #Hay un lugar disponible
				lista.append((i, j))
			elif (matriz[i][j] != 0 and matriz[i][j].get_color() != color): #Se encuentra un apieza de diferente color
				lista.append((i, j))
				break 
			else:
				break #se encontró una pieza de su color
			i -= 1
			j -= 1

		#Esquina superior derecha indice i va de -1 en -1 e indice j de i en 1
		i = x-1
		j = y+1
		while self.enRango(i) and self.enRango(j):
			if (matriz[i][j] == 0): #Hay un lugar disponible
				lista.append((i, j))
			elif (matriz[i][j] != 0 and matriz[i][j].get_color() != color): #Se encuentra un apieza de diferente color
				lista.append((i, j))
				break 
			else:
				break #se encontró una pieza de su color
			i -= 1
			j += 1

		#Esquina inferior izquierda
		i = x+1
		j = y-1
		while self.enRango(i) and self.enRango(j):
			if (matriz[i][j] == 0): #Hay un lugar disponible
				lista.append((i, j))
			elif (matriz[i][j] != 0 and matriz[i][j].get_color() != color): #Se encuentra un apieza de diferente color
				lista.append((i, j))
				break 
			else:
				break #se encontró una pieza de su color
			i += 1
			j -= 1

		#esquina inferior derecha
		i = x+1
		j = y+1
		while self.enRango(i) and self.enRango(j):
			if (matriz[i][j] == 0): #Hay un lugar disponible
				lista.append((i, j))
			elif (matriz[i][j] != 0 and matriz[i][j].get_color() != color): #Se encuentra un apieza de diferente color
				lista.append((i, j))
				break 
			else:
				break #se encontró una pieza de su color
			i += 1
			j += 1

		return lista 