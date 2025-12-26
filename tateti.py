from tablero import Tablero

class Tateti:
    def __init__(self):
        self.turno = "X"
        self.tablero = Tablero()
        self.ganador = None
        self.juego_terminado = False

    def ocupar_una_de_las_casillas(self, fil, col):
        if self.juego_terminado:
            raise Exception("El juego ya terminó!")
        
        # pongo la ficha...
        self.tablero.poner_la_ficha(fil, col, self.turno)
        
        # verificar condición de victoria
        self.ganador = self.tablero.verificar_ganador()
        if self.ganador:
            self.juego_terminado = True
            return
        
        # verificar empate
        if self.tablero.esta_lleno():
            self.juego_terminado = True
            return
        
        # cambiar turno... va a suceder solo si se pudo poner la ficha
        if self.turno == "X":
            self.turno = "O"
        else:
            self.turno = "X"
    
    def obtener_estado_juego(self):
        if self.ganador:
            return f"¡Jugador {self.ganador} ha ganado!"
        elif self.juego_terminado:
            return "¡Empate!"
        else:
            return "Juego en curso"
