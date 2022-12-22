"""
 Este es el Ejercicio 2.3 de Python

Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto
que python tiene la función len() incorporada, pero escribirla por nosotros mismos
resulta un muy buen ejercicio.
"""

cadena = ("Me llamo Daniel")                                            #Creacion de la cadena
lista = ['manzana', 'platano', 'pera', 'mango', 'naranja']              #Creacion de la lista

def longuitud(datolong):                                                #Creacion de la funcion
    contador = 0                                                        #Crear un contador para que empiece desde 0
    for i in datolong:
        contador += 1                                                   #bucle para que cada vez que se mueva uno en la cadena, sume al contador 1 y cuando termine muestre por pantalla el numero final
    return print("La loguitud es de:", contador)

longuitud(cadena)                                                       #Llamar a la funcion cadena
longuitud(lista)                                                        #Llamar a la funcion lista