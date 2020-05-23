"""

Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla 
con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las 
asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.


"""




asignatura = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []


print ("Que has puntuado en Matemáticas?\n")
nota = input()
notas.insert(0, nota)

nota = input("Que has puntuado en Física?\n")
notas.insert(1, nota)

nota = input("Que has puntuado en Química?\n")
notas.insert(2, nota)

nota = input("Que has puntuado en Historia?\n")
notas.insert(3, nota)

nota = input("Que has puntuado en Lengua\n")
notas.insert(4,nota)




print ("En", asignatura[0], "tu nota ha sido de", notas[0])
print ("En", asignatura[1], "tu nota ha sido de", notas[1])
print ("En", asignatura[2], "tu nota ha sido de", notas[2])
print ("En", asignatura[3], "tu nota ha sido de", notas[3])
print ("En", asignatura[4], "tu nota ha sido de", notas[4])


print (notas)


#######    SOLUCION DEL AUTOR   ############


subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
scores = []
for subject in subjects:
    score = input("¿Qué nota has sacado en " + subject + "?")
    scores.append(score)
for i in range(len(subjects)):
    print("En " + subjects[i] + " has sacado " + scores[i])

    