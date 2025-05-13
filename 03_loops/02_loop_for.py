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