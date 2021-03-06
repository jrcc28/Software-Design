from Interfaz import *
from Juego import *
import csv
#to windows compile: py -m pip install -U pygame --user
#windows use: >py -m Controlador

class Controlador:
    def __init__(self):
        self.game = Game()
        self.interfaz = Interfaz(self)
        self.turno = 1
        self.nombreJugador1 = "Jugador 1"
        self.nombreJugador2 = "Jugador 2"
		#posiciones del tablero y tamanos
        self.cuadro = 50
        self.borde = 20
        self.tableroPos = 30
        self.BOARD_SIZE = 400


    def start(self):
        self.interfaz.game_menu()

    def get_tablero(self):
        return self.game.get_tablero()
    #por el momento solo csv
    def leer_archivo(self, name):
       count_info=0
       count_lineas=1
       with open(name , newline='') as File:
           reader = csv.reader(File)
           for row in reader:
               if count_lineas % 2!=0:
                   if count_info < 8 :
                       self.game.llenar_tablero(row,count_info)
                   else:
                       self.turno=self.game.llenar_fichas(row)

                   count_info=count_info+1

               count_lineas=count_lineas+1



    #por el momento solo csv
    def crear_archivo(self, name):
        myFile = open(name, 'w')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(self.game.get_tablero())
            writer.writerows(self.game.get_estado_juego(self.turno))

    def reset(self):
        self.game.clean_game()
        self.turno=1

    def jugar_turno(self,x,y):
        pos_valida = self.convertir_pos(x,y)
        #esto es para colocar alguna ficha en el tablero(matriz) debe ser una posicion valida
        if self.turno==1 and pos_valida!=(-1,-1):#si el jugador es ficha negra
            if self.game.set_ficha(pos_valida[0],pos_valida[1],1):#si se logro colocar la ficha
                self.set_turno(2) # ahora pasa a ser la ficha blanca
                self.game.cambiar_turno(2)
                if not self.game.hay_posiciones():
                    self.set_turno(1)
                    self.game.cambiar_turno(1)
        elif self.turno==2 and pos_valida!=(-1,-1):#si el jugador es ficha blanca
            if self.game.set_ficha(pos_valida[0],pos_valida[1],2):#si se logro colocar la ficha
                self.set_turno(1)
                self.game.cambiar_turno(1)
                if not self.game.hay_posiciones():
                    self.set_turno(2)
                    self.game.cambiar_turno(2)
				    

    def setNombreJugador1(self,nombre):
        self.nombreJugador1 = nombre

    def getNombreJugador1(self):
        return self.nombreJugador1

    def setNombreJugador2(self,nombre):
        self.nombreJugador2 = nombre

    def getNombreJugador2(self):
        return self.nombreJugador2

    def get_reglas(self):
        #string con las reglas.
        reglas = ["El objetivo del juego es tener mas fichas del propio color.",
        "De inicio se colocan cuatro fichas como en el tablero:",
        "Dos fichas blancas en D4 y E5, y dos negras en E4 y D5.",
        "Comienzan a mover las negras: Un movimiento consiste",
        "en colocar una ficha propia sobre el tablero de",
        "forma que \'flanquee\' una o varias fichas contrarias.",
        "Las fichas flanqueadas son volteadas para mostrar",
        "el color propio. Es obligatorio voltear todas",
        "las fichas flanqueadas entre la ficha que se coloca",
        "y las que ya estaban colocadas.",
        "Una vez volteadas las fichas el turno pasa al contrario",
        "que procede de la misma forma con sus fichas.",
        "Si un jugador no tiene ninguna posibilidad",
        "de mover, el turno pasa al contrario.",
        "La partida termina cuando ninguno de los dos jugadores puede mover.",
        "Normalmente cuando el tablero esta lleno o practicamente lleno.",
        "Gana el jugador que acaba con mas fichas propias",
        "sobre el tablero Es posible el empate.",
        "Disfruta el Juego!"]
        return reglas

    def set_turno(self, valor):
        self.turno = valor

    def get_turno(self):
        return self.turno

    def get_num_negras(self):
        return self.game.get_num_negras()

    def get_num_blancas(self):
        return self.game.get_num_blancas()

    def get_mover_negras(self):
        return self.game.get_mover_negras()

    def get_mover_blancas(self):
        return self.game.get_mover_blancas()

    def convertir_pos(self,mouse_x ,mouse_y ):
        # click was out of board, ignores
        if mouse_x > self.BOARD_SIZE + 50 or \
            mouse_x < 50 or \
            mouse_y > self.BOARD_SIZE + 50 or \
            mouse_y < 50:
            position = (-1,-1)
            return position

        # find place
        position = ((mouse_x - 50) // self.cuadro),((mouse_y - 50) // self.cuadro)
        # flip orientation
        position = (position[1], position[0])
        continar = False
        return position

def main():
    controlador = Controlador()
    controlador.start()


if __name__ == '__main__':
    main()
