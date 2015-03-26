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
	"""Regresa una lista de tuplas con los movimientos 
	posibles de la pieza"""
	@abc.abstractmethod
	def get_movimientos(self):
		#Algo 
		return 

	"""regresa una tupla con su posicion actual"""
	@abc.abstractmethod
	def get_posicion(self):
		return 


	"""Regresa el color de la pieza"""
	@abc.abstractmethod
	def get_color(self):
		return

	"""Comprueba si dado un entero n se encuentra en el 
	rango valido del tamaño del arreglo"""
	@staticmethod
	def enRango(n): 
		return n <= 8 and n >= 0


	




