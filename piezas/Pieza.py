# -*- coding: utf-8 -*-
import abc
"""
Clase abstracta para piezas, las piezas 
(Torre, caballo, etc) herederán esta clase 
y deberán impletementar los métodos 
"""
class Pieza():
	__metaclass_ = abc.ABCMeta #no sé que es

	"""Constructor para Pieza"""
	def __init__(self, _current, color):
		self._current = _current
		self.color = color 
		self.tipo = tipo 

	"""Regresa una lista de tuplas con los movimientos 
	posibles de la pieza"""
	@abc.abstractmethod
	def get_movimientos(self):
		#Algo 
		return 

	"""regresa una tupla con su posicion actual"""
	def get_posicion(self):
		return self._current


	"""Actualiza la posicion de una pieza 
	Recibe una tupla con su nueva posicion
	"""
	def set_posicion(self, act):
		return self._current

	"""Regresa el color de la pieza"""
	def get_color(self):
		return self.color 

	"""Comprueba si dado parametros n se encuentran en el 
	rango valido del tamaño de la matriz"""
	def enRango(self, n): 
		return n <= 7 and n >= 0

	




