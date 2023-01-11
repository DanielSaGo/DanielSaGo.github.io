"""
 Este es el Ejercicio 2.11 de Python

 Escribir una función mas_larga() que tome una lista de palabras y devuelva la más larga.
"""

lista = ['manzana', 'platano', 'pera', 'mango', 'naranjas']

def palabramaslarga(list):
    long_mayor = 0
    palabra_mas_larga = None
    for palabra in list:
        if len(palabra) > long_mayor:
            long_mayor = len(palabra)
            palabra_mas_larga = palabra
    print(palabra_mas_larga)

palabramaslarga(lista)