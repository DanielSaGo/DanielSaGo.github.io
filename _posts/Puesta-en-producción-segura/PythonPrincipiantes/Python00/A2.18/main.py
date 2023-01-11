"""
 Este es el Ejercicio 2.16 de Python

Escriba una función es_bisiesto() que determine si un año determinado es un año
bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400
"""

año = int(input("Proporcione un año:"))

def añosbisiestos(fecha):
    if fecha % 4 == 0 and fecha % 400 == 0 or fecha % 100 != 0:
        print("Es un año bisiesto")
    else:
        print("No es un año bisiesto")

añosbisiestos(año)