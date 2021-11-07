"""
Dada una matriz de números enteros N, encuentre la suma de sus elementos.
Función descriptiva
Complete la función simpleArraySum . Debe devolver la suma de los elementos de la matriz como un número entero.
simpleArraySum tiene los siguientes parámetros:
ar : una matriz de números enteros
Formato de entrada
La primera línea contiene un número entero, N, que denota el tamaño de la matriz.
La segunda línea contiene  N enteros separados por espacios que representan los elementos de la matriz.
"""
nfilas = int(input("ingrese el numero de filas "))
mcolumnas = int(input("ingrese el numero de columnas "))
matriz = [[0 for i in range(nfilas)] for j in range(mcolumnas)]
sumaTotal=0
for i in range(nfilas):
    for j in range(mcolumnas):
        matriz[i][j] = int(input("ingrese un numero "))
        sumaTotal= sumaTotal+ matriz[i][j]
print(sumaTotal)