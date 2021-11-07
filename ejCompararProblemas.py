"""
Lucía y Carlos crearon cada uno un problema para su posterior calificació.
Un revisor califica los dos problemas, otorgando puntos en una escala del 1 al 100
para tres categorías: claridad del problema, originalidad y dificultad.
La calificación del desafío de Lucía es el desafío a = (a [0], a [1], a [2]),
y la calificación del desafío de Carlos es el desafío b = (b [0], b [1], b [2]).
La tarea consiste en encontrar sus puntos de comparación comparando a [0] con b [0],
a [1] con b [1] y a [2] con b [2] .
Si a [i]> b [i] , entonces Lucía recibe 1 punto.
Si a [i] <b [i] , entonces Carlos recibe 1 punto.
Si a [i] = b [i] , ninguna persona recibe un punto.
Los puntos de comparación son los puntos totales que ganó una persona.
Dada una a y b , determinar sus respectivos puntos de comparación.
Para los elementos * 0 *, Carlos recibe un punto debido a un [0].
Para los elementos iguales a [1] y b [1] , se consiguen sin puntos.
Finalmente, para los elementos 2 , a [2]> b [2] por lo que Lucía recibe un punto.
La matriz de retorno es [1, 1] con la puntuación de Lucía primero y la de Carlos en segundo lugar.
Función descriptiva
Complete la función compareTriplets . compareTriplets tiene los siguientes parámetros:
int a [3] : calificación de desafío de Lucía
int b [3] : calificación de desafío de Carlos
Salida
int [2] : la puntuación de Alice está en la primera posición y la puntuación de Bob en la segunda.
Formato de entrada
La primera línea contiene 3 números enteros separados por espacios, un a[0] , un a[1] y un a[2],
los valores respectivos al desafío a . La segunda línea contiene 3 números enteros separados por espacios,
b [0] , b [1] , y b [2] , los valores respectivos al desafío b .
"""
a1=int(input("Introduce la primera nota de Lucia: "))
a2=int(input("Introduce la segunda nota de Lucia: "))
a3=int(input("Introduce la tercera nota de Lucia: "))
b1=int(input("Introduce la primera nota de Carlos: "))
b2=int(input("Introduce la segunda nota de Carlos: "))
b3=int(input("Introduce la tercera nota de Carlos: "))
lucia =[a1,a2,a3]
carlos =[b1,b2,b3]
puntosl = 0
puntosc = 0
if lucia[0] > carlos[0]:
    puntosl+=1
elif lucia[0]< carlos[0]:
    puntosc+=1
if lucia[1]> carlos[1]:
    puntosl+=1
elif lucia[1]< carlos[1]:
    puntosc+=1
if lucia[2]> carlos[2]:
    puntosl+=1
elif lucia[2]< carlos[2]:
    puntosc+=1
print("Carlos tiene "+ str(puntosc)+ " puntos")
print("Lucía tiene "+ str(puntosl)+ " puntos")
if puntosl>puntosc:
    print ("Ha ganado Lucía")
elif puntosl<puntosc:
    print ("Ha ganado Carlos")
else:
    print ("No ha ganado nadie")