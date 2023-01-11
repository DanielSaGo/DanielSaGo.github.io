"""
 Este es el Ejercicio 2.13 de Python

Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene
que evaluar la cadena y decir cuantas letras mayúsculas tiene
"""

cadena = str(input("Proporcione una cadena:"))

def numayus(string):
    cont = 0
    for letra in string:
        if letra == letra.upper():      #Si la letra es igual en mayus
            cont += 1                   #Cuenta 1 y sumalo en el contador
    print("El numero de mayusculas es:", cont)

numayus(cadena)