"""
 Este es el Ejercicio 2.10 de Python

La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio
2 (primera parte), solo van a funcionar para 2 o 3 números. Supongamos que tenemos
más de 3 números o no sabemos cuántos números son. Escribir una función
max_in_list() que tome una lista de números y devuelva el más grande.
"""

listnum = [13, 5, 2, 23, 15, 12, 6, 7, 8]

def numMayor(list):
    Ordenlist = sorted(list)     #Ordena la lista de numeros
    print(Ordenlist[-1])         #Recoge el ultimo numero de la lista

numMayor(listnum)