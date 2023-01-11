"""
Este es el Ejercicio 1.2 de Python

Solicitar al usuario dos valores:
● numero1 (int)
● numero2 (int)
Se debe imprimir el mayor de los dos números (la salida debe ser idéntica a la que
sigue):
Proporciona el numero1:
Proporciona el numero2:
El numero mayor es:<numeroMayor>
"""

print("Proporciona el numero1:")
numero1 = int(input())
print("Proporciona el numero2:")
numero2 = int(input())

if numero1 > numero2:
    print("El numero mayor es:",numero1,)
elif numero2 > numero1:
    print("El numero mayor es:", numero2,)