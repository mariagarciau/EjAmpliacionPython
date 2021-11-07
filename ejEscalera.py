"""Esta es una escalera de tamaño n= 4:
   #
  ##
 ###
####
Su base y altura son iguales a n. Se dibuja mediante #símbolos y espacios. La última línea no está precedida por espacios.
Escribe un programa que imprima una escalera de tamaño n .
Función descriptiva
Complete la función de staircase. staircase tiene los siguientes parámetros:
int n : un número entero
Impresión
Imprima una escalera como se describe arriba.
Formato de entrada
Un solo entero, n , que denota el tamaño de la escalera.
Formato de salida
Imprime una escalera de tamaño utilizando #símbolos y espacios.
Salida de muestra
     #
    ##
   ###
  ####
 #####
######
    """
n = int(input("Introduce un número: "))
for altura in range(n):
    for ancho in range(altura+1):
        espacios = n*ancho
        print(espacios*'',end="#")
    print()


