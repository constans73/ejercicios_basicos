#Ejercicio que saca una media de 5 evaluaciones.


print ("Esete es un programa que saca la media de las cinco materias del curso")


materia_esp = float(input("Introduce la puntuacion de Español".ljust(55)))    #alinea a la izquierda en una longitud de 55 caracteres
materia_mat = float(input("Introduce la puntuacion de Matematicas".ljust(55)))
materia_eco = float(input("Introduce la puntuacion de Economia".ljust(55)))
materia_pro = float(input("Introduce la puntuacion de Programacion".ljust(55)))
materia_ing = float(input("Introduce la puntuacion de Ingles".ljust(55)))

media = (materia_esp + materia_mat + materia_eco + materia_pro + materia_ing)/5   

print ("La puntuacion media del curso es de".rjust(54),round(media,2))		#nos mostraria solo 2 decimales