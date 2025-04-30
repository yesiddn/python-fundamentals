###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###

import os

if os.system("clear") != 0: os.system("cls") # system permite ejecutar comandos del sistema operativo, en este caso se usa para limpiar la consola. En Windows se usa cls

print("Sentencia simple condicional (if)")

edad = 18
if edad >= 18:
  print("Eres mayor de edad")

print("--------------------")

print("Sentencia condicional compuesta (if, else)")

if edad >= 18:
  print("Eres mayor de edad")
else:
  print("Eres menor de edad")

print("--------------------")

print("Sentencia condicional anidada (if, elif, else)")

nota = 5.0

if nota >= 4.0:
  print("Aprobado")
elif nota >= 3.0:
  print("Regular")
else:
  print("Reprobado")

print("--------------------")

print("Condiciones multiples")

age = 18
has_driving_license = False

if age >= 18 and has_driving_license:
  print("Puedes conducir")
else:
  print("Policia!!! 🚓")

# En un pueblo de Isla Margarita son más laxos y
# te dejan conducir si eres mayor de edad O tienes carnet
if age >= 18 or has_driving_license:
  print("Puedes conducir en la Isla Margarita 🚗")
else:
  print("Paga al policía y te deja conducir!!!")

is_weekend = False

if not is_weekend:
  print("Es un día laboral")