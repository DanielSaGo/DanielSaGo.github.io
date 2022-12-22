"""
 Este es el Ejercicio 2.9 de Python

Definir un histograma procedimiento() que tome una lista de números enteros e
imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir
lo siguiente:
"""

listnum = [1, 3, 4, 2, 7, 2, 7, 9, 4, 8, 4, 2, 6, 4, 8, 2, 7, 9, 8, 7]
def procedimiento(numeros):
    mapnum = {}

    for i in numeros:
        if i in mapnum:
            mapnum[i] += 1
        else:
            mapnum[i] = 1

    for x in sorted(mapnum):
        print(f'{x}: {mapnum[x]}')

procedimiento(listnum)