"""
 Este es el Ejercicio 2.1 de Python

Definir una función max() que tome como argumento dos números y devuelva el mayor
de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla
nosotros mismos es un muy buen ejercicio.
"""

numero1 = int(input("Numero1:"))
numero2 = int(input("Numero2:"))

def mayorn(n1, n2):
    if n1 > n2:
        print("El numero mayor es:", n1, )
    elif n1 < n2:
        print("El numero mayor es:", n2, )

mayorn(numero1, numero2)