#-*- coding: utf-8 -*-

from Pieza import Pieza
from Color import Color 
"""Clase para pieza torre""" 
class Torre(Pieza):
	""" Constructor de Torre
		Recibe la coordenada inicial en forma de tupla
		Recibe también un color de la clase Enum Color
	"""
	def __init__(self, _current, color):
		super(Torre, self).__init__(_current, color) #LLama al constructor de la super clas
		
	#Tostring 
	def __str__(self):
		if (self.get_color() == Color.blanco):
			return "♜"
		else:
			return "♖"

	#@Override
	def get_movimientos(self):
		pass

	"""@Override Regresa la tupla que contiene la posicion"""
	def get_posicion(self):
		return self._current

	"""@Override"""
	def get_color(self):
		return self.color 	
