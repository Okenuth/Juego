import hangman
import reversegam
import tictactoeModificado
import json
def guardar(jug,juego):
	jug["Juegos"]=juego
def main(args):
	print('Ingrese el nombre del jugador')
	nom=input()
	jugador={"Nombre":nom}
	sigo_jugando = True
	while sigo_jugando:
		
		print('''
		Elegí con qué juego querés jugar:
		1.- Ahorcado
		2.- Ta-TE-TI
		3.- Otello
		4.- Salir''')

		opcion = input()
		if opcion == '1':
			hangman.main()
			guardar(jugador,"Ahorcado")
		elif opcion == '2':
			tictactoeModificado.main()
			guardar(jugador,"Tateti")
		elif opcion == '3':
			reversegam.main()
			guardar(jugador,"Reverse")
		elif opcion == '4':
			sigo_jugando = False
	dato=open('dato.txt','a')
	json.dump(jugador,dato)	
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
