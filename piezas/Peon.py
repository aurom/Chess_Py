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
		return "♜"

	#@Override
	#Error: Si el peon es blanco o negro avanzan de manera diferente
	def get_movimientos(self, tablero):
		matriz = tablero.getTablero()
		current = self._current
		lista = list() #lista de movimientos
		if (self.enRango(current[0]+2) and not self.movida): #peon avanza dos lugares
			if (matriz[current[0]+1][current[1]] == 0 and matriz[current[0]+2][current[1]] == 0): #no tiene a nadie adelante
				lista.append((current[0]+2, current[1]))
		if (self.enRango(current[0]+1)): 
			if (matriz[current[0]+1][current[1]] == 0): #si no tiene a nadie adelante
				lista.append((current[0]+1, current[1]))
		if (self.enRango(current[0]-1) and self.enRango(current[1]-1)):
			if (matriz[current[0]-1][current[1]-1] != 0): #Hay una pieza en su diagonal izq
				lista.append((current[0]-1, current[1]-1))
		if (self.enRango(current[0]-1) and self.enRango(current[1]+1)):
			if (matriz[current[0]-1][current[1]+1] != 0): #Hay una pieza en su diagonal der
				lista.append((current[0]-1, current[1]+1))
		return lista

	"""@Override Regresa la tupla que contiene la posicion"""
	def get_posicion(self):
		return self._current

	"""@Override"""
	def get_color(self):
		return self.color

	"""Comprueba si dado un entero n se encuentra en el 
	rango valido del tamaño del arreglo"""
	def enRango(self, n): 
		return n <= 8 and n >= 0 	


if __name__ == '__main__':
	p = Peon((1, 1), Color.blanco)
	t = Tablero()
	t.agregaPieza(Peon((0, 0), Color.negro))
	t.agregaPieza(Peon((0, 2), Color.negro))
	l = p.get_movimientos(t)
	for x in l:
		print(x)