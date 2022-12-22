"""
 Este es el Ejercicio 2.17 de Python

Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a"
tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
Se puede hacer que el usuario sea quien elija la palabra.
"""

cadena = str(input("Proporciona una palabra:"))
vocales = ('a', 'e', 'i', 'o', 'u')

def contletras(palabra, vocal):
    contA = 0
    contE = 0
    contI = 0
    contO = 0
    contU = 0
    for x in palabra:
        if x == vocal[0]:
            contA += 1
        elif x == vocal[1]:
            contE += 1
        elif x == vocal[2]:
            contI += 1
        elif x == vocal[3]:
            contO += 1
        elif x == vocal[4]:
            contU += 1
    print("La palabra tiene", contA,"A,", contE,"E,", contI,"I,", contO,"O,", contU,"U.")

contletras(cadena, vocales)
