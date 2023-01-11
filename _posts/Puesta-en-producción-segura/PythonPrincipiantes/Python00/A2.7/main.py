"""
 Este es el Ejercicio 2.7 de Python

Definir una función superposicion() que tome dos listas y devuelva True si tienen al
menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando
el bucle for anidado.
"""

lista1 = [1, 2, 3, 4]
lista2 = [1, 7, 5]

def superposicion(lista1, lista2):
    for i in lista1:
        for o in lista2:
            if i == o:
                return (True)
    return (False)

print(superposicion(lista1, lista2))