"""

Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva,
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

"""


import os
os.system("cls")

print ("Acontinuacion introduzca los números ganadores del sorteo")


numeros = []

numero = int(input())
numeros.insert(0,(numero))

numero = int(input())
numeros.insert(1,(numero))

numero = int(input())
numeros.insert(2,(numero))

numero = int(input())
numeros.insert(3,(numero))

numero = int(input())
numeros.insert(4,(numero))

numero = int(input())
numeros.insert(5,(numero))

print ("Ahora introduzca el numero complementario")

numero = int(input())
numeros.insert(6,(numero))

numero = int(input("Solo nos queda el reintegro, introduzcalo por favor\n"))
numeros.insert(7,(numero))

ganadores = numeros[0:6]
ganadores.sort()
#numeros.sort()
print ("La combinacion ganadora ordenada es la siguiente",  ganadores,"\nEl numero completentario es", numeros[6],"\ny el reintegro el ", numeros[7])



print(numeros)

#######    SOLUCION DEL AUTOR   ############

awarded = []
for i in range(6):
    awarded.append(int(input("Introduce un número ganador: ")))
awarded.sort()
print("Los números ganadores son " + str(awarded))


