###
# 02 - Bucles (for)
# Permiten ejecutar un bloque de código repetidamente mientras ITERA un iterable o una lista
###

print("Ejemplo 1: Bucles for iterando una lista")

frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
  print(fruta)

# Se puede iterar sobre cualquier objeto iterable, como listas, tuplas, diccionarios, conjuntos y cadenas de texto.
print("Ejemplo 2: Bucles for iterando sobre strings")
frase = "Hola Mundo"
for letra in frase:
  print(letra)

# enemerate() permite obtener el índice y el valor al mismo tiempo
print("Ejemplo 3: Bucles for con enumerate()")
frutas = ["manzana", "banana", "cereza"]
for indice, fruta in enumerate(frutas):
  print(f"Índice: {indice}, Fruta: {fruta}")

# break
print("Ejemplo 4: Bucles for con break")
animales = ["perro", "gato", "pájaro", "pez", "loro"]
for animal in animales:
  if animal == "pájaro":
    print("¡He encontrado un pájaro!")
    break
  print(f"Animal: {animal}")

# continue
print("Ejemplo 5: Bucles for con continue")
for animal in animales:
  if animal == "pájaro":
    print("¡He encontrado un pájaro! Pero lo voy a ignorar.")
    continue
  print(f"Animal: {animal}")

# Comprensión de listas (list comprehension)
print("Ejemplo 6: Comprensión de listas")
animales = ["perro", "gato", "pájaro", "pez", "loro"]
animales_mayusculas = [animal.upper() for animal in animales]
print(animales_mayusculas)

# Numeros pares
print("Ejemplo 7: Números pares")
pares = [numero for numero in [1, 2, 3, 4, 5] if numero % 2 == 0]

###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")