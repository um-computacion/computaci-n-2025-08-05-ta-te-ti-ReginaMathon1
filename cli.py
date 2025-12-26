from tateti import Tateti


def mostrar_tablero(tablero):
    print("\n  0   1   2")
    for i, fila in enumerate(tablero):
        print(f"{i} {fila[0] or ' '} | {fila[1] or ' '} | {fila[2] or ' '}")
        if i < 2:
            print("  ---------")


def main():
    print("¡Bienvenidos al Tateti!")
    print("Instrucciones: Ingresa fila (0-2) y columna (0-2)")
    juego = Tateti()
    
    while not juego.juego_terminado:
        print("\n" + "="*30)
        print("Tablero actual:")
        mostrar_tablero(juego.tablero.contenedor)
        print(f"\nTurno del jugador: {juego.turno}")
        
        try:
            fil = int(input("Ingrese fila (0-2): "))
            col = int(input("Ingrese columna (0-2): "))
            
            if fil < 0 or fil > 2 or col < 0 or col > 2:
                print("Error: Las coordenadas deben estar entre 0 y 2")
                continue
                
            juego.ocupar_una_de_las_casillas(fil, col)
            
        except ValueError:
            print("Error: Ingrese números válidos")
        except Exception as e:
            print(f"Error: {e}")
    
    # Mostrar resultado final
    print("\n" + "="*30)
    print("¡JUEGO TERMINADO!")
    mostrar_tablero(juego.tablero.contenedor)
    print(f"\nResultado: {juego.obtener_estado_juego()}")
    print("¡Gracias por jugar!")


if __name__ == '__main__':
    main()