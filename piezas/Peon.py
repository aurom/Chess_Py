#-*- coding: utf-8 -*-
from Pieza import Pieza
from Color import Color
from Tablero import Tablero
"""Clase para pieza Peon""" 
class Peon(Pieza):

	""" Constructor de Peon
		Recibe la coordenada inicial en forma de tupla
		Recibe también un color de la clase Enum Color
	"""
	def __init__(self, _current, color):
		super(Peon, self).__init__(_current, color) #LLama al constructor de la super clase
		self.movida = False 
		
	#Tostring 
	def __str__(self):
		if (self.color == Color.blanco): return "♙" 
		else : return "♟"

	
	"""#@Override"""
	def get_movimientos(self, tablero):
		#si es blanca solo mueve en una dirección, 
		#por tanto, se ejecutan métodos dieferentes según el color
		if (self.color == Color.blanco): 
			return self.moviBlanco(tablero) 
		else: 
			return self.moviNegra(tablero)


	"""***********Métodos privados NO USAR******************"""
	
	def moviBlanco(self, tablero):
		matriz = tablero.getTablero()
		x = self._current[0]
		y = self._current[1]
		color = self.get_color() 
		lista = list() #lista de movimientos

		if (self.enRango(x-2) and self.enRango(x-1) and (not self.movida)): #peon avanza dos lugares
			if (matriz[x-1][y] == 0 and matriz[x-2][y] == 0): #no tiene a nadie adelante
				lista.append((x-2, y))
		if (self.enRango(x-1)): #Avanza un lugar
			if (matriz[x-1][y] == 0): #si no tiene a nadie adelante
				lista.append((x-1, y))
		if (self.enRango(x-1) and self.enRango(y-1)):
			if (matriz[x-1][y-1] != 0 and matriz[x-1][y-1].get_color() != color): #Hay una pieza en su diagonal izq y es de diferente color
				lista.append((x-1, y-1))
		if (self.enRango(x-1) and self.enRango(y+1)):
			if (matriz[x-1][y+1] != 0 and matriz[x-1][y+1].get_color() != color): #Hay una pieza en su diagonal der y es de diferente color
				lista.append((x-1, y+1))
		return lista

	def moviNegra(self, tablero):
		matriz = tablero.getTablero()
		x = self._current[0]
		y = self._current[1]
		color = self.get_color() 
		lista = list() #lista de movimiento
		if (self.enRango(x+2) and self.enRango(x+1) and (not self.movida)): #peon avanza dos lugares
			if (matriz[x+1][y] == 0 and matriz[x+2][y] == 0): #no tiene a nadie adelante
				lista.append((x+2, y))
		if (self.enRango(x+1)): #Avanza un lugar
			if (matriz[x+1][y] == 0): #si no tiene a nadie adelante
				lista.append((x+1, y))
		if (self.enRango(x+1) and self.enRango(y+1)):
			if (matriz[x+1][y+1] != 0 and matriz[x+1][y+1].get_color() != color): #Hay una pieza en su diagonal izq y es de diferente color
				lista.append((x+1, y+1))
		if (self.enRango(x+1) and self.enRango(y-1)):
			if (matriz[x+1][y-1] != 0 and matriz[x+1][y-1].get_color() != color): #Hay una pieza en su diagonal der y es de diferente color
				lista.append((x+1, y-1))
		return lista