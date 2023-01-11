"""
Este es el Ejercicio 1.3 de Python

Iterar un rango de 0 a 10 e imprimir sólo los números divisibles entre 3
"""
listanum = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def div(numeros):
    for x in numeros:
        if x % 3 == 0:
          print(x)

div(listanum)