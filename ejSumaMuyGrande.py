"""
En este desafío, debe calcular e imprimir la suma de los elementos en una matriz,
teniendo en cuenta que algunos de esos números enteros pueden ser bastante grandes.
Función descriptiva
Complete la función aVeryBigSum. Debe devolver la suma de todos los elementos de la matriz.
aVeryBigSum tiene los siguientes parámetros:
int ar [n] : una matriz de números enteros.
Salida
long : la suma de todos los elementos de la matriz
Formato de entrada
La primera línea de la entrada consta de un número entero .
La siguiente línea contiene enteros separados por espacios contenidos en la matriz.
"""
nfilas = int(input("ingrese el numero de filas "))
mcolumnas = int(input("ingrese el numero de columnas"))
matriz = [[0 for i in range(nfilas)] for j in range(mcolumnas)]
sumaTotal=0
for i in range(nfilas):
    for j in range(mcolumnas):
        matriz[i][j] = int(input("ingrese un numero "))
        sumaTotal= sumaTotal+ matriz[i][j]
print(sumaTotal)