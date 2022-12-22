"""
 Este es el Ejercicio 2.8 de Pytho

Definir una función generar_n_caracteres() que tome un entero n y devuelva el
caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver
"xxxxx".
"""

n = int(input("Proporcione un numero:"))
c = str(input("Proporcione un caracter:"))

def funmulti(numero, caracter):
    multi = numero*caracter
    print("Caracter multiplicado por el numero:", multi)

funmulti(n, c)