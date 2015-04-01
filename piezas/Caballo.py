#-*- coding: utf-8 -*-
from Pieza import Pieza
from Color import Color 
"""Clase para pieza Caballo""" 
class Caballo(Pieza):
	""" Constructor de Caballo
		Recibe la coordenada inicial en forma de tupla
		Recibe también un color de la clase Enum Color
	"""
	def __init__(self, _current, color):
		super(Caballo, self).__init__(_current, color) #LLama al constructor de la super clas
		
	#Tostring 
	def __str__(self):
		if self.color == Color.blanco: return "♞" 
		else: return "♘"

	#@Override
	def get_movimientos(self, tablero):
		matriz = tablero.getTablero()
		x = self._current[0]
		y = self._current[1]
		color = self.get_color() 
		lista = list() #lista de movimientos
		
		"se checan todos los patrones de moviemientos posibles del caballo"
		i = x-2
		j = y+1
		if (self.enRango(i) and self.enRango(j)):
			if (matriz[i][j] == 0):
				lista.append((i, j))
			elif (color != matriz[i][j].get_color()): #Entonces no está vacío 
				lista.append((i, j))


		i = x-1
		j = y+2
		if (self.enRango(i) and self.enRango(j)):
			if (matriz[i][j] == 0):
				lista.append((i, j))
			elif (color != matriz[i][j].get_color()): #Entonces no está vacío 
				lista.append((i, j))

		i = x+1
		j = y+2
		if (self.enRango(i) and self.enRango(j)):
			if (matriz[i][j] == 0):
				lista.append((i, j))
			elif (color != matriz[i][j].get_color()): #Entonces no está vacío 
				lista.append((i, j))


		i = x+2
		j = y+1
		if (self.enRango(i) and self.enRango(j)):
			if (matriz[i][j] == 0):
				lista.append((i, j))
			elif (color != matriz[i][j].get_color()): #Entonces no está vacío 
				lista.append((i, j))

		i = x+2
		j = y-1
		if (self.enRango(i) and self.enRango(j)):
			if (matriz[i][j] == 0):
				lista.append((i, j))
			elif (color != matriz[i][j].get_color()): #Entonces no está vacío 
				lista.append((i, j))

		i = x+1
		j = y-2
		if (self.enRango(i) and self.enRango(j)):
			if (matriz[i][j] == 0):
				lista.append((i, j))
			elif (color != matriz[i][j].get_color()): #Entonces no está vacío 
				lista.append((i, j))


		i = x-2
		j = y-1
		if (self.enRango(i) and self.enRango(j)):
			if (matriz[i][j] == 0):
				lista.append((i, j))
			elif (color != matriz[i][j].get_color()): #Entonces no está vacío 
				lista.append((i, j))

		i = x-1
		j = y-2
		if (self.enRango(i) and self.enRango(j)):
			if (matriz[i][j] == 0):
				lista.append((i, j))
			elif (color != matriz[i][j].get_color()): #Entonces no está vacío 
				lista.append((i, j))

		return lista