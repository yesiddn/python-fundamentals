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

# Ten en cuenta que hay valores que al usarlos como condiciones
# en Python son evaluados como verdaderos o falsos
# por ejemplo, el número 5, es True
numero = 5
if numero: # True
  print("El número no es cero")

# Pero el número 0 se evalúa como False
numero = 0
if numero: # False
  print("Aquí no entrará nunca")

# También el valor vacío "" se evalúa como False
nombre = ""
if nombre:
  print("El nombre no es vacío")

# ¡Ten cuidado con no confundir la asignación = con la comparación ==!
numero = 3 # asignación
es_el_tres = numero == 3 # comparación

if es_el_tres:
  print("El número es 3")

# A veces podemos crear condicionales en una sola línea usando
# las ternarias, es una forma concisa de un if-else en una línea de código
print("\nLa condición ternaria:")
# [código si cumple la condición] if [condicion] else [codigo si no cumple]

edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)

###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)