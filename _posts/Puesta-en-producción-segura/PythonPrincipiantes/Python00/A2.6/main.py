"""
 Este es el Ejercicio 2.6 de Python

Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la
cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""

cadena = ("Mi nombre es Daniel")

def inversa(palabra):
    cadenainv = ""
    for i in palabra:
        cadenainv = i+ cadenainv
    print(cadenainv)

inversa(cadena)
