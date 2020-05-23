"""

Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> 
es cada una de las asignaturas de la lista.

"""


asignaturas = ["Matematicas", "Física", "Química", "Historia", "Lengua"]

print ("Yo estudio", asignaturas[0])
print ("Yo estudio", asignaturas[1])
print ("Yo estuido", asignaturas[2])
print ("Yo estudio", asignaturas[3])
print ("Yo estudio", asignaturas[4])


#######    SOLUCION DEL AUTOR   ############
#import os
#os.system("cls")

subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for subject in subjects:
    print("Yo estudio " + subject)