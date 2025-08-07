class PosOcupadaException(Exception):
    ...


class Tablero:
    def __init__(self):
        self.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]

    def poner_la_ficha(self, fil, col, ficha):
        # ver si esta ocupado...
        if self.contenedor[fil][col] == "":
            self.contenedor[fil][col] = ficha
        else:
            raise PosOcupadaException("pos ocupada!")
    
    def verificar_ganador(self):
        # Verificar filas
        for fila in self.contenedor:
            if fila[0] != "" and fila[0] == fila[1] == fila[2]:
                return fila[0]
        
        # Verificar columnas
        for col in range(3):
            if (self.contenedor[0][col] != "" and 
                self.contenedor[0][col] == self.contenedor[1][col] == self.contenedor[2][col]):
                return self.contenedor[0][col]
        
        # Verificar diagonales
        if (self.contenedor[0][0] != "" and 
            self.contenedor[0][0] == self.contenedor[1][1] == self.contenedor[2][2]):
            return self.contenedor[0][0]
        
        if (self.contenedor[0][2] != "" and 
            self.contenedor[0][2] == self.contenedor[1][1] == self.contenedor[2][0]):
            return self.contenedor[0][2]
        
        return None
    
    def esta_lleno(self):
        for fila in self.contenedor:
            for casilla in fila:
                if casilla == "":
                    return False
        return True