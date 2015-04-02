#-*- coding: utf-8 -*-
from Pieza import Pieza
from Color import Color 
"""Clase para pieza Dama""" 
class Dama(Pieza):
	""" Constructor de Dama
		Recibe la coordenada inicial en forma de tupla
		Recibe también un color de la clase Enum Color
	"""
	def __init__(self, _current, color):
		super(Dama, self).__init__(_current, color) #LLama al constructor de la super clas
		
	#Tostring 
	def __str__(self):
		if (self.color == Color.blanco): return "♛"	
		else: return "♕"
			

	#@Override
	def get_movimientos(self, tablero):
		"""La Dama es básicamente un alfil y una Torre al mismo tiempo así que 
			es copy-paste de ambos metodos
		"""	
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

		"""
		Revisaremos espacios disponibles hacia arriba, abajo y a los lados
		"""
		i = x-1
		while self.enRango(i): #Revisa espacios disponibles hacia arriba del tablero
			if (matriz[i][y] == 0): #hay un espacio disponible
				lista.append((i, y))
			#Si se encuentra una pieza de dieferente color se la puede comer 
			elif (matriz[i][y] != 0 and matriz[i][y].get_color() != self.color):
				lista.append((i, y))
				break #nos salimos
			else: #se encontró una pieza pero es de su mismo color
				break
			i -= 1

		i = x+1 #usamos la misma variable para iterar por que BBB
		while self.enRango(i): #Revisa espacios disponibles hacia abajo del tablero
			if matriz[i][y] == 0: #Hay un espacio disponible
				lista.append((i, y))
			#Si se encuentra una pieza de dieferente color se la puede comer 
			elif (matriz[i][y] != 0 and matriz[i][y].get_color() != self.color):
				lista.append((i, y))
				break #nos salimos
			else: #se encontró una pieza pero es de su mismo color
				break
			i += 1

		i = y-1 
		while self.enRango(i): #Revisamos hacia la izquierda del tablero
			if matriz[x][i] == 0:
				lista.append((x, i))
			#Si se encuentra una pieza de dieferente color se la puede comer 
			elif (matriz[x][i] != 0 and matriz[x][i].get_color() != self.color):
				lista.append((x, i))
				break #nos salimos
			else: #se encontró una pieza pero es de su mismo color
				break
			i -= 1

		i = y+1
		while self.enRango(i): #Revisamos hacia la derecha
			if matriz[x][i] == 0:
				lista.append((x, i))
			elif (matriz[x][i] != 0 and matriz[x][i].get_color() != self.color):
				lista.append((x, i))
				break #nos salimos
			else: #se encontró una pieza pero es de su mismo color
				break
			i += 1

		return lista