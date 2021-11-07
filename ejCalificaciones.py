"""La Universidad para el nuevo curso va a implementar una nueva poítica de calificación:
• Cada estudiante recibe una nota en el rango inclusivo de 0 a 100 .
• Si tienes una nota inferior a 40 o menos es una calificación suspensa.
Además a los profesores en la universidad  nos gusta redondear los  de acuerdo con estas reglas:
• Si la diferencia entre una  nota y el siguiente múltiplo de 5 es menos que 3 , se redondea hasta
el siguiente múltiplo de 5 .
• Si el valor de  la nota es menorque 40 , no se produce redondeo ya que el resultado seguirá
siendo una calificación suspensa.
Ejemplos
• 84 redondear a  (85 - 84 es menos de 3)
• 29 no redondear (el resultado es menos de 40)
• 57 no redondear (60 - 57 es 3 o más)
Dado el valor inicial de la nota para cada uno de los n estudiantes,
escriban código para automatizar el proceso de redondeo
"""
from typing import no_type_check_decorator


nota = int(input("Introduzca la nota obtenida entre 0 y 100 incluidos: "))
contador =0
if nota<=40:
    print("Tu nota es "+str(nota)+". Estas suspenso")
if nota>40 and nota%5==0:
    print("Tu nota es "+str(nota))
if nota >40:
    if (nota+2)%5==0:
        print("Tu nota es "+str(nota+2))
    else:
        print("Tu nota es "+str(nota))
    '''while (nota%5!=0):
        contador+1
        if contador >=3:
            break
        if nota%5!=0 and contador<3:
            nota+1
            print("Tu nota es "+ str(nota))
            break'''
