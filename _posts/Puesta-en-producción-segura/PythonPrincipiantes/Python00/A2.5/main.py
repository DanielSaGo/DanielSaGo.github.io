"""
 Este es el Ejercicio 2.5 de Python

Escribir una función sum() y una función multip() que sumen y multipliquen
respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería
devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""

listnum = [1,2,3,4]

def funsuma(numeros):
    suma = 0
    for i in numeros:                                       #por cada uno de los valores de la lista haz... (lo de dentro)
        suma += i                                           #por cada salto que de, lo suma al anterior y asi por cada valor de la lista
    print("La suma de los numeros son:", suma)

def funmulti(numeros):
    multi = 1
    for i in numeros:                                       #por cada uno de los valores de la lista haz... (lo de dentro)
        multi *= i                                          #por cada salto que de, lo multiplica al anterior y asi por cada valor de la lista
    print("La multiplicacion de los numeros son:", multi)

funsuma(listnum)
funmulti(listnum)

