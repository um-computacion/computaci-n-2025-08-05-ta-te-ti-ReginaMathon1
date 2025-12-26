import unittest

from tablero import Tablero, PosOcupadaException
from tateti import Tateti
from jugador import Jugador


class TestTablero(unittest.TestCase):
    
    def setUp(self):
        self.tablero = Tablero()
    
    def test_tablero_inicial_vacio(self):
        """Test 1: Verificar que el tablero inicia vacío"""
        for fila in self.tablero.contenedor:
            for casilla in fila:
                self.assertEqual(casilla, "")
    
    def test_poner_ficha_en_posicion_vacia(self):
        """Test 2: Verificar que se puede poner una ficha en posición vacía"""
        self.tablero.poner_la_ficha(0, 0, "X")
        self.assertEqual(self.tablero.contenedor[0][0], "X")
    
    def test_excepcion_posicion_ocupada(self):
        """Test 3: Verificar que lanza excepción al ocupar posición ya ocupada"""
        self.tablero.poner_la_ficha(1, 1, "X")
        with self.assertRaises(PosOcupadaException):
            self.tablero.poner_la_ficha(1, 1, "O")
    
    def test_verificar_ganador_fila(self):
        """Test 4: Verificar detección de ganador en fila"""
        # Llenar primera fila con X
        for col in range(3):
            self.tablero.poner_la_ficha(0, col, "X")
        self.assertEqual(self.tablero.verificar_ganador(), "X")
    
    def test_verificar_ganador_diagonal(self):
        """Test 5: Verificar detección de ganador en diagonal"""
        # Llenar diagonal principal con O
        for i in range(3):
            self.tablero.poner_la_ficha(i, i, "O")
        self.assertEqual(self.tablero.verificar_ganador(), "O")


class TestTateti(unittest.TestCase):
    
    def setUp(self):
        self.juego = Tateti()
    
    def test_cambio_de_turno(self):
        """Test 6: Verificar que los turnos cambian correctamente"""
        self.assertEqual(self.juego.turno, "X")
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.assertEqual(self.juego.turno, "O")
        self.juego.ocupar_una_de_las_casillas(0, 1)
        self.assertEqual(self.juego.turno, "X")
    
    def test_deteccion_fin_juego_por_victoria(self):
        """Test 7: Verificar que el juego termina cuando hay un ganador"""
        self.juego.ocupar_una_de_las_casillas(0, 0)  # X
        self.juego.ocupar_una_de_las_casillas(1, 0)  # O
        self.juego.ocupar_una_de_las_casillas(0, 1)  # X
        self.juego.ocupar_una_de_las_casillas(1, 1)  # O
        self.juego.ocupar_una_de_las_casillas(0, 2)  # X - gana
        
        self.assertTrue(self.juego.juego_terminado)
        self.assertEqual(self.juego.ganador, "X")
        self.assertEqual(self.juego.obtener_estado_juego(), "¡Jugador X ha ganado!")


class TestJugador(unittest.TestCase):
    
    def test_crear_jugador(self):
        """Test adicional: Verificar creación de jugador"""
        jugador = Jugador("Regina", "X")
        self.assertEqual(jugador.nombre, "Regina")
        self.assertEqual(jugador.ficha, "X")
        self.assertEqual(jugador.victorias, 0)


if __name__ == '__main__':
    unittest.main()
