from Color import Color
from Peon import Peon
from Rey import Rey
from Torre import Torre
from Alfil import Alfil
from Caballo import Caballo
from Dama import Dama
from Tablero import Tablero

def mueveBlancas(tablero):
	while True:
		text = input("Movida (blancas): ")
		coor = text.split(" ")
		inicial = (int(coor[0]), int(coor[1]))
		final = (int(coor[2]), int(coor[3]))
		if (tablero.mueve(inicial, final, Color.blanco)):
			print (t)
			break

def mueveNegras(tablero):
	while True:
		text = input("Movida (negras): ")
		coor = text.split(" ")
		inicial = (int(coor[0]), int(coor[1]))
		final = (int(coor[2]), int(coor[3]))
		if (tablero.mueve(inicial, final, Color.negro)):
			print (t)
			break
		
if __name__ == '__main__':
	t = Tablero()
	t.eliminaPieza((0, 1))
	t.eliminaPieza((0, 2))
	t.eliminaPieza((0, 3))
	t.eliminaPieza((0, 5))
	t.eliminaPieza((0, 6))
	print (t)

	"""while True:
		mueveBlancas(t)
		mueveNegras(t)"""
	