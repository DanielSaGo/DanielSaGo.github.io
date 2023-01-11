"""
 Este es el Ejercicio 2.15 de Python

Definir una tupla con 10 edades de personas.
Imprimir la cantidad de personas con edades superiores a 20.
Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.
"""

tupla = (10, 23, 45, 14, 3, 34, 23, 67, 16, 9)

def mayor20(tupla):
    cont = 0
    for edad in tupla:
        if edad > 20:
            cont += 1
    print("El numero de personas mayores de 20 son:", cont)

mayor20(tupla)