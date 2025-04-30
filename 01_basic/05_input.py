###
# 05 - Entrada de usuario (input()) version simplificada
# La funcion input() permite obtener datos del usuario a traves de la consola.
###

name = input("¿Cuál es tu nombre? ")  # Se muestra un mensaje en la consola y se espera a que el usuario ingrese un valor. También se puede porner un salto de linea con \n
print(f"Hola {name}, bienvenido a Python")

age = input("¿Cuál es tu edad? ")

print(f"Dentro de 5 años tendrás {int(age) + 5} años")  # Se convierte el valor ingresado a un entero para poder realizar la suma. Si no se hace esto, se sumará como un string y no como un número.

print("Obtener multiples valores a la vez")
country, city = input("¿Cuál es tu país y ciudad? (separados por coma): ").split(", ")  # Se usa el método split() para separar los valores ingresados por el usuario. Se puede usar cualquier separador, no solo la coma.
print(f"Tu país es {country} y tu ciudad es {city}") 