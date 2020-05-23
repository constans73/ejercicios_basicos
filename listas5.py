"""

Escribir un programa que almacene en una lista los números del 1 al 10
 y los muestre por pantalla en orden inverso separados por comas.

 """





lista = [1,2, 3, 4, 5, 6, 7, 8, 9, 10]

lista.sort (reverse=True)


print (lista[0],",", lista[1], ",", lista[2], ",", lista[3],",", lista[4], ",", lista[5], ",", lista[6], ",", lista[7], ",", lista[8], ",", lista[9])

########################   SOLUCION 1 AUTOR    #############################
 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, 11):
    print(numbers[-i], end=", ")

print("\n")

########################   SOLUCION 2 AUTOR    #############################

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.reverse()
for number in numbers:
    print(number, end=", ")
