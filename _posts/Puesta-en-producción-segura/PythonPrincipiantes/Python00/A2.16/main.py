"""
 Este es el Ejercicio 2.16 de Python

Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la
letra a.
También se puede hacer elegir al usuario la letra a buscar. (Un poco mas emocionante)
"""

listnombres = ['Daniel', 'Carlos', 'David', 'Jose', 'Maria', 'Alvaro', 'Bruno']
letra = str(input("Proporcione una letra:"))

def DetectLetra(list, letter):
    listafin = []
    for word in list:
        if letter == word[0].upper() or letter == word[0].lower():
            listafin.append(word)
    print(listafin)

DetectLetra(listnombres, letra)