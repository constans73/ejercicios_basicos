#!/usr/bin/env python 3.7
'''
    JulianV
    12/10/2019.
    Mostrar en pantalla el promedio de 
    un alumno que ha cursado 5 materias.
'''
print("Promedio de cinco materias cursadas.")
print("-------------------------------------")
# En las siguientes lineas se muestra el metodo rjust()
# Tambien se pueden utilizar ljust() y center() 
# En este caso estamos alineando el texto a la derecha a 35
# espacios del margen.
espanol = float(input("Calificacion Espanol: ".center(55)))  #dejaria el texto centrado en el espacio 55 caracteres
matematicas = float(input("Calificacion en Matematicas: ".rjust(35)))   #dejaria el texto en la derecha en 35 caracteres
economia = float(input("Calificacion en Economia: ".rjust(35)))
programacion = float(input("Calificacion en Programacion: ".rjust(35)))
ingles = float(input("Calificacion en Ingles: ".ljust(35)))				#dejaria el texto en la izquierda en 35 caracteres

promedio = (espanol + matematicas + economia + programacion + ingles) / 5
print(f"\nEl promedio de las cinco materias es : {promedio}",promedio)