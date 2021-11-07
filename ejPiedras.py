"""Dos jugadores llamados P1 Y P2 están jugando un juego con un número inicial de n piedras.
Jugador1 siempre juega primero, y los dos jugadores se mueven en turnos alternos.
Las reglas del juego son las siguientes:
En un solo movimiento, un jugador puede eliminar ,2,3 o 5 , o  piedras del tablero de juego.
Si un jugador no puede hacer un movimiento, ese jugador pierde el juego.
Dado el número inicial de piedras, busque e imprima el nombre del ganador.
Cada jugador juega de manera óptima, lo que significa que no harán un movimiento que les haga perder
el juego si existe un movimiento ganador.
• Por ejemplo, si n=4, P1  puede hacer los siguientes movimientos:
• P1 elimina 2 piedras quedando 2. P2 luego eliminará 2  piedras y ganar.
• P1 elimina 3 piedras quedando 1. P2 no se puede mover y pierde.
"""
n=int(input("Introduzca un numero "))
if n<=1:
    print("P1 pierde")
else:
    if n==2 or n==3:
        print("P1 gana")
    if n%2==0 and n!= 2:
        print("P2 gana")
    if n%2!=0:
        print("P1 gana")
