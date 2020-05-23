

print("Este es un progrma para cambiar divisas")

nombre_divisa = input("¿A que divisa quieres cambiar tus dolares? introduce el nombre.\n")


valor_divisa = float(input("Itroduce el valor de la divisa que quieres cambiar tus dolares\n"))
cantidad_dolares = float(input("Introduce la cantidad de dolares a ingresar\n"))

saldo_total= cantidad_dolares * valor_divisa

print ("tu saldo en pesos colombianos es de:", saldo_total, nombre_divisa)