# -*- coding: utf-8 -*-
from Color import Color
from Peon import Peon
from Rey import Rey
from Torre import Torre
from Alfil import Alfil
from Caballo import Caballo
from Dama import Dama

class Tablero(object):
	"""Constructor """
	def __init__(self):
		self.tablero = [[0 for x in range(8)] for x in range(8)]
		self.init_piezas() #Agrega todas las piezas iniciales
		self.reyBlanco = (7, 4) #Se guarda siempre la posicion de los reyes
		self.reyNegro = (0, 4)
		#Falta poner siempre posicion actual del rey
	

	#Es como el toString del tablero solo imprime el contenido 
	def __str__(self):
		res = ""
		for filas in self.tablero:
			for pieza in filas:
				if (pieza != 0):
					res += pieza.__str__() + " "
				else: 
					res += "0 "
			res += "\n"
		return res 

	"""Regresa la matriz donde se encuentran todas las piezas"""
	def getTablero(self):
		tabla = self.tablero
		return tabla 

	"""Regresa la pieza que está en la posicion indicada"""
	def getPieza(self, pos):
		return self.tablero[pos[0]][pos[1]]
	"""Agrega una pieza al tablero en la 
	que se pasa como parametro"""
	def agregaPieza(self, pieza):
		pos = pieza.get_posicion()
		self.tablero[pos[0]][pos[1]] = pieza


	"""Recibe n argumentos (Piezas) y las agrega"""
	def agregaMuchasPiezas(self, *args):
		for p in args:
			self.agregaPieza(p)

	"""Elimina una pieza del tablero, 
	recibe una tupla de la posicion a eliminar"""
	def eliminaPieza(self, pos):
		x = pos[0]
		y = pos[1]
		self.tablero[x][y] = 0
	"""
	Mueve una piezas a la posicion que se pasa como parametro
	NO MOVER A MENOS QUE SE HAYA COMPROBADO QUE ES UN MOVIMIENTO VÁLIDO
	CUANDO SE MUEVA UNA PIEZA EL ESPACIO EN DONDE ESTABA SE ASIGNA A CERO
	PARA SABER QUE ESTA DISPONIBLE
	"""
	#NOTA: FALTA ENROQUE DEL REY Y JAQUE MATE
	#Regresa True si se hizo el movimiento
	def mueve(self, coor1, coor2, color):
		pieza = self.getPieza(coor1)
		if (pieza == 0): #No hay tal pieza
			return False
		if (pieza.get_color() != color): #La pieza en esa coordenada es de otro color
			return False
		if (pieza.getClass() == 'Rey'): #Si se quiere mover al rey lo manejamos en otro método
			return self.mueveRey(color, coor2)
			

		movimientos = pieza.get_movimientos(self)
		if (not coor2 in movimientos): #No es un movimiento válido
			return False 
		else: #Lo movemos
			self.eliminaPieza(pieza.get_posicion()) #eliminamos la pieza del tablero
			x = coor2[0]
			y = coor2[1]
			self.tablero[x][y] = pieza
			pieza.set_posicion((x, y)) #Actualizamos la posicion de la pieza
			#Comprobamos que su rey no haya quedado en jaque
			rey = self.getPieza(self.reyBlanco)
			if (color == Color.negro):
				rey = self.getPieza(self.reyNegro)
			if (rey.esta_en_jaque(self)): #Si el rey está en jaque deshacemos el movimiento
				self.eliminaPieza(pieza.get_posicion()) #eliminamos la pieza del tablero
				x = coor1[0]
				y = coor1[1]
				self.tablero[x][y] = pieza 
				pieza.set_posicion((x, y))
				return False 

			# si es Peon o Torre su variable movida se cambia 
			if (pieza.getClass() == 'Peon' or pieza.getClass() == 'Torre'):
				pieza.movida = True 

			return True 

	"""Mueve al rey a la coordenada dada como parametro, recibe el color del rey a mover"""
	def mueveRey(self, color, coor):
		#Se obtiene la pieza segpun su color, ver constructor de esta clase
		pieza = self.getPieza(self.reyBlanco)
		if (color == Color.negro): 
			pieza = self.getPieza(self.reyNegro)

		movimientos = pieza.get_movimientos(self)

		if (not coor in movimientos): #No es válido el movimiento
			return False 
		self.eliminaPieza(pieza.get_posicion()) #eliminamos la pieza del tablero
		x = coor[0]
		y = coor[1]
		self.tablero[x][y] = pieza
		pieza.set_posicion((x, y)) #Actualizamos la posicion de la pieza
		#Actualizamos la posicion del rey en el tablero segpun su color
		if (pieza.get_color() == Color.blanco):
			self.reyBlanco = (x, y)
		else:
			self.reyNegro = (x, y)
		pieza.movida = True # Decimos que ya se movió
		return True 


	"""Inicia las piezas en sus estados iniciales"""
	def init_piezas(self):
		#Peones blancos
		self.tablero[6][0] = Peon((6, 0), Color.blanco)
		self.tablero[6][1] = Peon((6, 1), Color.blanco)
		self.tablero[6][2] = Peon((6, 2), Color.blanco)
		self.tablero[6][3] = Peon((6, 3), Color.blanco)
		self.tablero[6][4] = Peon((6, 4), Color.blanco)
		self.tablero[6][5] = Peon((6, 5), Color.blanco)
		self.tablero[6][6] = Peon((6, 6), Color.blanco)
		self.tablero[6][7] = Peon((6, 7), Color.blanco)
		#Piezas blancas
		self.tablero[7][0] = Torre((7, 0), Color.blanco)
		self.tablero[7][1] = Caballo((7, 1), Color.blanco)
		self.tablero[7][2] = Alfil((7, 2), Color.blanco)
		self.tablero[7][3] = Dama((7, 3), Color.blanco)
		self.tablero[7][4] = Rey((7, 4), Color.blanco)
		self.tablero[7][5] = Alfil((7, 5), Color.blanco)
		self.tablero[7][6] = Caballo((7, 6), Color.blanco)
		self.tablero[7][7] = Torre((7, 7), Color.blanco)
		#Peones negros
		self.tablero[1][0] = Peon((1, 0), Color.negro)
		self.tablero[1][1] = Peon((1, 1), Color.negro)
		self.tablero[1][2] = Peon((1, 2), Color.negro)
		self.tablero[1][3] = Peon((1, 3), Color.negro)
		self.tablero[1][4] = Peon((1, 4), Color.negro)
		self.tablero[1][5] = Peon((1, 5), Color.negro)
		self.tablero[1][6] = Peon((1, 6), Color.negro)
		self.tablero[1][7] = Peon((1, 7), Color.negro)
		#Piezas negras
		self.tablero[0][0] = Torre((0, 0), Color.negro)
		self.tablero[0][1] = Caballo((0, 1), Color.negro)
		self.tablero[0][2] = Alfil((0, 2), Color.negro)
		self.tablero[0][3] = Dama((0, 3), Color.negro)
		self.tablero[0][4] = Rey((0, 4), Color.negro)
		self.tablero[0][5] = Alfil((0, 5), Color.negro)
		self.tablero[0][6] = Caballo((0, 6), Color.negro)
		self.tablero[0][7] = Torre((0, 7), Color.negro)



