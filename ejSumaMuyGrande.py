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
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#
def aVeryBigSum(ar):
    # Write your code here
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()
"""
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#
def aVeryBigSum(ar):
    # Write your code here
    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        ar_count = int(input().strip())
        ar = list(map(int, input().rstrip().split()))
        result = aVeryBigSum(ar)
        fptr.write(str(result) + '\n')
        fptr.close()