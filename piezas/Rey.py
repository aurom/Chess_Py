#-*- coding: utf-8 -*-
from Pieza import Pieza
from Color import Color 
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
	def get_movimientos(self):
		pass

	"""@Override Regresa la tupla que contiene la posicion"""
	def get_posicion(self):
		return self._current

	"""@Override"""
	def get_color(self):
		return self.color

	"""Comprueba si el rey está en jaque"""
	def esta_en_jaque(self):
		pass
