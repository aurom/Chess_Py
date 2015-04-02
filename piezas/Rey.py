#-*- coding: utf-8 -*-
import copy #para copiar objetos
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
		self.movida = False
	#Tostring 
	def __str__(self):
		if (self.color == Color.blanco): return "♚"
		else: return "♔"
			

	#@Override
	def get_movimientos(self, tablero):
		#NOTA: FAlta enroque
		matriz = tablero.getTablero()
		x = self._current[0]
		y = self._current[1]
		color = self.get_color() 
		lista = list() #lista de movimientos

		#Trata de moverse arriba
		i = x-1
		if self.enRango(i):
			if matriz[i][y] == 0:
				if not (self.check(tablero, (i, y))): #check
					lista.append((i, y))

		#Trata de moverse abajo
		i = x+1
		if self.enRango(i):
			if (matriz[i][y] == 0 and not (self.check(tablero, (i, y)))):
				lista.append((i, y))

		#Trata de mover a la izq
		i = y-1
		if self.enRango(i):
			if (matriz[x][i] == 0 and not (self.check(tablero, (x, i)))):
				lista.append((x, i))

		#Trata de mover a la der
		i = y+1
		if self.enRango(i):
			if (matriz[x][i] == 0 and not (self.check(tablero, (x, i)))):
				lista.append((x, i))

		#Trata de moverse esquina superior izquierda
		i = x-1
		j = y-1
		if self.enRango(i) and self.enRango(j): #
			if (matriz[i][j] == 0 and not (self.check(tablero, (i, j)))):
				lista.append((i, j))

		#Trata de moverse esquina superior derecha
		i = x-1
		j = y+1
		if self.enRango(i) and self.enRango(j): #
			if (matriz[i][j] == 0 and not (self.check(tablero, (i, j)))):
				lista.append((i, j))

		#Trata de moverse esquina inferior izquierda
		i = x+1
		j = y-1
		if self.enRango(i) and self.enRango(j): #
			if (matriz[i][j] == 0 and not (self.check(tablero, (i, j)))):
				lista.append((i, j))

		#Trata de moverse esquina inferior derecha
		i = x+1
		j = y+1
		if self.enRango(i) and self.enRango(j): #
			if (matriz[i][j] == 0 and not (self.check(tablero, (i, j)))):
				lista.append((i, j))

		#trata de enrocarse ala izq 
		if (self.movida == False):
			i = x
			j = y-1
			while self.enRango(j):
				pieza = matriz[i][j]
				if (pieza != 0 and pieza.getClass() == 'Torre' and pieza.get_color() == self.color): # se encontró una torre
					if pieza.movida == False and not (self.check(tablero, (i, j))):
						lista.append((i, j+2))
				elif(pieza != 0 and pieza.getClass() != 'Torre'): 
					break 
				j -= 1 

		#Trata de enrocarse a la der
		if (self.movida == False):
			i = x
			j = y+1
			while self.enRango(j):
				pieza = matriz[i][j]
				if (pieza != 0 and pieza.getClass() == 'Torre' and pieza.get_color() == self.color): # se encontró una torre
					if pieza.movida == False and not (self.check(tablero, (i, j))):
						lista.append((i, j-1))
				elif(pieza != 0 and pieza.getClass() != 'Torre'): 
					break 
				j += 1



		return lista	


	"""Comprueba si el rey está en jaque. Regresa True 
	si está en jaque False en caso contrario"""
	def esta_en_jaque(self, tablero):
		matriz = tablero.getTablero()
		x = self._current[0]
		y = self._current[1]
		color = self.get_color() 

		i = x-1
		while self.enRango(i): #Revisa hacia arriba del tablero
			#Si se encuentra una pieza de dieferente color debe ser Torre o dama para ser jaque
			pieza = matriz[i][y]
			if (pieza != 0 and pieza.get_color() != self.color):
				if (pieza.getClass() == "Dama" or pieza.getClass() == "Torre"): 
					return True 
			elif (pieza != 0 and pieza.get_color() == self.color): 
				break #se encontró una pieza suya en la columna 
			i -= 1

		i = x+1
		while self.enRango(i): #Revisa hacia aabajo del tablero
			#Si se encuentra una pieza de dieferente color debe ser Torre o dama para ser jaque
			pieza = matriz[i][y] 
			if (pieza != 0 and pieza.get_color() != self.color):
				if (pieza.getClass() == "Dama" or pieza.getClass() == "Torre"):
					return True 
			elif (pieza != 0 and pieza.get_color() == self.color): 
				break #se encontró una pieza suya en la columna 
			i += 1

		#Revisa en la misma fila  a la derecha
		j = y+1
		while self.enRango(j):
			#Si se encuentra una pieza de dieferente color debe ser Torre o dama para ser jaque
			pieza = matriz[x][j] 
			if (pieza != 0 and pieza.get_color() != self.color):
				if (pieza.getClass() == "Dama" or pieza.getClass() == "Torre"):
					return True 
			elif (pieza != 0 and pieza.get_color() == self.color): 
				break #se encontró una pieza suya en la columna 
			j += 1

		#Revisa en la misma fila  a la Izquierda
		j = y-1
		while self.enRango(j):
			#Si se encuentra una pieza de dieferente color debe ser Torre o dama para ser jaque
			pieza = matriz[x][j] 
			if (pieza != 0 and pieza.get_color() != self.color):
				if (pieza.getClass() == "Dama" or pieza.getClass() == "Torre"):
					return True 
			elif (pieza != 0 and pieza.get_color() == self.color): 
				break #se encontró una pieza suya en la columna 
			j -= 1

		#Revisa diagonal superior izq
		i = x-1
		j = y-1
		while self.enRango(i) and self.enRango(j): 
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.get_color() != self.color):
				if (pieza.getClass() == "Dama" or pieza.getClass() == "Alfil"):
					return True
			elif (pieza != 0 and pieza.get_color() == self.color): 
				break 
			i -= 1
			j -= 1

		#Revisa diagonal superior derecha
		i = x-1
		j = y+1
		while self.enRango(i) and self.enRango(j): 
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.get_color() != self.color):
				if (pieza.getClass() == "Dama" or pieza.getClass() == "Alfil"):
					return True
			elif (pieza != 0 and pieza.get_color() == self.color): 
				break 
			i -= 1
			j += 1

		#Revisa diagonal inferior izq
		i = x+1
		j = y-1
		while self.enRango(i) and self.enRango(j): 
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.get_color() != self.color):
				if (pieza.getClass() == "Dama" or pieza.getClass() == "Alfil"):
					return True
			elif (pieza != 0 and pieza.get_color() == self.color): 
				break 
			i += 1
			j -= 1

		#Revisa diagonal inferior derecha
		i = x+1
		j = y+1
		while self.enRango(i) and self.enRango(j): 
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.get_color() != self.color):
				if (pieza.getClass() == "Dama" or pieza.getClass() == "Alfil"):
					return True
			elif (pieza != 0 and pieza.get_color() == self.color): 
				break 
			i += 1
			j += 1

		#**********Revisa por Caballos ES MUUUUY LARGOOO*********
		i = x-2
		j = y+1
		if self.enRango(i) and self.enRango(j):
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.get_color() != color and pieza.getClass() == 'Caballo'):
					return True 

		i = x-1
		j = y+2
		if self.enRango(i) and self.enRango(j):
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.get_color() != color and pieza.getClass() == 'Caballo'):
					return True


		i = x+1
		j = y+2
		if self.enRango(i) and self.enRango(j):
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.get_color() != color and pieza.getClass() == 'Caballo'):
					return True


		i = x+2
		j = y+1
		if self.enRango(i) and self.enRango(j):
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.get_color() != color and pieza.getClass() == 'Caballo'):
					return True


		i = x+2
		j = y-1
		if self.enRango(i) and self.enRango(j):
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.get_color() != color and pieza.getClass() == 'Caballo'):
					return True

		i = x+1
		j = y-2
		if self.enRango(i) and self.enRango(j):
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.get_color() != color and pieza.getClass() == 'Caballo'):
					return True

		i = x-1
		j = y-2
		if self.enRango(i) and self.enRango(j):
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.get_color() != color and pieza.getClass() == 'Caballo'):
					return True

		i = x-2
		j = y-1
		if self.enRango(i) and self.enRango(j):
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.get_color() != color and pieza.getClass() == 'Caballo'):
				return True

		#***Fin del caballo***

		#checa por jaques por peon según color
		if (self.color == Color.blanco): #Si es blaco checa diagonales superiores
			i = x-1
			j = y-1
			if self.enRango(i) and self.enRango(j):
				pieza = matriz[i][j]
				if (pieza != 0 and pieza.get_color() != self.color and pieza.getClass() == 'Peon'):
					return True 

			i = x-1
			j = y+1
			if self.enRango(i) and self.enRango(j):
				pieza = matriz[i][j]
				if (pieza != 0 and pieza.get_color() != self.color and pieza.getClass() == 'Peon'):
					return True 

		else: #Ees un rey negro

			i = x+1
			j = y-1
			if self.enRango(i) and self.enRango(j):
				pieza = matriz[i][j]
				if (pieza != 0 and pieza.get_color() != self.color and pieza.getClass() == 'Peon'):
					return True 

			i = x+1
			j = y+1
			if self.enRango(i) and self.enRango(j):
				pieza = matriz[i][j]
				if (pieza != 0 and pieza.get_color() != self.color and pieza.getClass() == 'Peon'):
					return True

		#***Checa si hay reyes***#
		#Arriba
		i = x-1
		j = y
		if self.enRango(i):
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.getClass == 'Rey'):
				return True 
		#Abajo
		i = x+1
		j = y
		if self.enRango(i):
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.getClass == 'Rey'):
				return True 

		#der
		i = x 
		j = y+1
		if self.enRango(i):
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.getClass == 'Rey'):
				return True 
		#iz
		i = x
		j = y-1
		if self.enRango(i):
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.getClass == 'Rey'):
				return True 

		#esq sup der
		i = x-1
		j = y+1
		if self.enRango(i):
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.getClass == 'Rey'):
				return True 
		#Esq sup izq
		i = x-1
		j = y-1
		if self.enRango(i):
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.getClass == 'Rey'):
				return True 
		#Esq inf der
		i = x+1
		j = y+1
		if self.enRango(i):
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.getClass == 'Rey'):
				return True 
		#esq inf iz
		i = x+1
		j = y-1
		if self.enRango(i):
			pieza = matriz[i][j]
			if (pieza != 0 and pieza.getClass == 'Rey'):
				return True 
		return False #pasó todas las pruebas no está en jaque


	"""PRIVADO comprueba si el rey ESTARÁ en jaque en la posicion dada como parametro"""
	def check(self, tabla, pos):

		tablero_tmp = copy.deepcopy(tabla) #Hago un tablero temporal para simular el movimiento
		rey = Rey(pos, self.get_color())

		tablero_tmp.eliminaPieza(self.get_posicion())
		tablero_tmp.agregaPieza(rey)

		return rey.esta_en_jaque(tablero_tmp)

	"""Nos dice si el rey está en jaque mate
	Se sabe de antemano que el rey está en jaque"""
	def jaque_mate(self, tablero):
		lista = self.get_movimientos(tablero)
		if len(lista) != 0: #si la lista de movimientos no es vacía tiene movimientos posibles
			return False 

		matriz = tablero.getTablero()
		#Si no tiene movimientos checamos uno a uno sus piezas y simulamos todos sus movimientos posibles
		for fila in matriz:
			for pieza in fila:
				if (pieza == 0 or pieza.get_color() != self.color):
					continue
				elif (pieza != 0 and pieza.get_color() == self.color): #UNa pieza del color del rey en jaque
					movimientos = pieza.get_movimientos(tablero)
					for movi in movimientos:
						if (not self.simula(tablero, pieza, movi)): #simulamos el movimiento en el tablero
							return False 
			
		return True 

	def simula(self, tablero, pieza, movi):
		tablero_tmp = copy.deepcopy(tablero) #Una coopia del tablero 
		tablero_tmp.eliminaPieza(pieza.get_posicion())
		pieza.set_posicion(movi)
		tablero_tmp.agregaPieza(pieza)
		#Revisamos si su rey sigue en jaque
		rey = tablero_tmp.getPieza(tablero_tmp.reyBlanco)
		if (pieza.get_color() == Color.negro):
			rey = tablero_tmp.getPieza(tablero_tmp.reyNegro)

		if (rey.esta_en_jaque(tablero_tmp)):
			return True 
		return False 




