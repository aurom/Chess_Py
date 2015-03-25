from Pieza import Pieza

"""Clase para pieza torre""" 
class Torre(Pieza):
	#constructor de Torre
	#Recibe la coordenada inicial en forma de tupla
	def __init__(self, _current):
		self._current = _current

	#Tostring 
	def __str__(self):
		return "♜"

	#@Override
	def get_movimientos():
		pass	
