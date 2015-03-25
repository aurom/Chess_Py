# -*- coding: utf-8 -*-
import abc
"""
Clase abstracta para piezas, las piezas 
(Torre, caballo, etc) herederán esta clase 
y deberán impletementar los métodos 
"""
class Pieza():
	__metaclass_ = abc.ABCMeta #no sé que es

	"""Regresa una lista de tuplas con los movimientos 
	posibles de la pieza"""
	@abc.abstractmethod
	def get_movimientos():
		#Algo 
		return 

	"""regresa una tupla con su posicion actual"""
	@abc.abstractmethod
	def get_posicion():
		return 

	"""
	Mueve una piezas a la posicion que se pasa como parametro
	NO MOVER A MENOS QUE SE HAYA COMPROBADO QUE ES UN MOVIMIENTO VÁLIDO
	"""
	@abc.abstractmethod
	def mueve(coordenada):
		#stuff
		return 

	"""Elimina la pieza del tablero en caso de ser comida"""
	@abc.abstractmethod
	def eliminar_pieza():
		return




