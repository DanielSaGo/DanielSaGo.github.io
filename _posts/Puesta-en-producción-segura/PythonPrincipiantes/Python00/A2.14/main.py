"""
 Este es el Ejercicio 2.14 de Python

Construir un pequeño programa que convierta números binarios en enteros.

Ejercicio 6
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla.

"""

#Numeros binarios a enteros

numbinario = str(input("Proporcione un numero binario:"))

def calcbin(num):
    res = 0
    for i in range(len(num)):
        res += int(num[i]) * 2 ** (len(num) - i - 1)
    print(res)

calcbin(numbinario)


print(" ")
# Ejercicio 6
añoencurso = int(input("Proporciona el año actual:"))

nombre1 = str(input("Proporciona el nombre de la persona1:"))
añonacim1 = int(input("Proporciona el año de nacimiento de la persona1:"))

nombre2 = str(input("Proporciona el nombre de la persona2:"))
añonacim2 = int(input("Proporciona el año de nacimiento de la persona2:"))

nombre3 = str(input("Proporciona el nombre de la persona3:"))
añonacim3 = int(input("Proporciona el año de nacimiento de la persona3:"))

edadactu1 = añoencurso - añonacim1
edadactu2 = añoencurso - añonacim2
edadactu3 = añoencurso - añonacim3

print(nombre1, "tiene", edadactu1)
print(nombre2, "tiene", edadactu2)
print(nombre3, "tiene", edadactu3)