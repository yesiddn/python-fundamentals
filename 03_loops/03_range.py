###
# 03 - range()
# Permite crear una secuencia de números. Puede ser útil para for, pero no solo para eso
###

print("Ejemplo 1: range()")
nums = range(5) # NO crea una lista -> [0, 1, 2, 3, 4]
print(nums) # range(0, 5)
print(type(nums)) # <class 'range'>

# range no crea el rango de numeros, sino que va devolviendo los numeros conforme se le pida
for num in nums:
  print(num) # 0, 1, 2, 3, 4

for num in range(5, 10):
  print(num) # 5, 6, 7, 8, 9

for num in range(5, 10, 2):
  print(num) # 5, 7, 9

for num in range(-5, 0):
  print(num) # -5, -4, -3, -2, -1

for num in range(10, 0, -1):
  print(num) # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

nums = range(5)
list_of_nums = list(nums) # es mejor evitarlo, pero a veces es necesario 
print(list_of_nums) # [0, 1, 2, 3, 4]

for _ in range(5): print("Hola") # 5 veces

###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")