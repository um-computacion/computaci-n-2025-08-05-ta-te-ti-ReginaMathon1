class Jugador:
    def __init__(self, nombre, ficha):
        self.nombre = nombre
        self.ficha = ficha  # "X" o "O"
        self.victorias = 0
    
    def incrementar_victorias(self):
        self.victorias += 1
    
    def __str__(self):
        return f"Jugador {self.nombre} ({self.ficha}) - Victorias: {self.victorias}"