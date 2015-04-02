from Color import Color
from Peon import Peon
from Rey import Rey
from Torre import Torre
from Alfil import Alfil
from Caballo import Caballo
from Dama import Dama
from Tablero import Tablero
import time
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
	print (t)

	t.mueve((6, 4), (4, 4), Color.blanco)
	print (t)
	time.sleep(1.5)

	t.mueve((1, 4), (3, 4), Color.negro)
	print (t)
	time.sleep(1)

	t.mueve((7, 5), (4, 2), Color.blanco)
	print (t)
	time.sleep(1.5)

	t.mueve((0, 1), (2, 2), Color.negro)
	print (t)
	time.sleep(1.5)

	t.mueve((7, 3), (3, 7), Color.blanco)
	print (t)
	time.sleep(1)

	t.mueve((1, 3), (2, 3), Color.negro)
	print (t)
	time.sleep(1.5)

	t.mueve((3, 7), (1, 5), Color.blanco)
	print (t)
	time.sleep(1.5)

	"""while True:
		mueveBlancas(t)
		mueveNegras(t)"""
	