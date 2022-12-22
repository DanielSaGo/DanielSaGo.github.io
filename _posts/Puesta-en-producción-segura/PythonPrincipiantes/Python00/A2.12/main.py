"""
 Este es el Ejercicio 2.12 de Python

Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y
devuelva las palabras que tengan más de n caracteres.
"""

lista = ['manzana', 'platano', 'pera', 'mango', 'naranjas']
numero = int(input("Proporciona un numero:"))

def palabramaslarga(list, num):
    long_min = num
    lista_palabras = []
    for palabra in list:
        if len(palabra) > long_min:
            lista_palabras.append(palabra)    #Añadimos las palabras a la lista
    print(lista_palabras)

palabramaslarga(lista, numero)