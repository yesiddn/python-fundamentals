###
# 01 - Bucles (while)
# Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición
###

# Bucle con condición simple
print("Ejemplo 1: Contar hasta 5")

counter = 0
while counter <= 5:
  counter += 1  # Incrementar el contador en 1
  print("Contador:", counter)

# Salir del bucle
print("Salir de bucle usando break")
counter = 0
while True:
  counter += 1  # Incrementar el contador en 1
  if counter == 3:
    break  # Salir del bucle cuando el contador sea igual a 3
  print("Contador:", counter)

# Saltar una iteración
print("Ejemplo 2: Saltar una iteración")
counter = 0
while counter <= 5:
  counter += 1  # Incrementar el contador en 1
  if counter == 3:
    continue  # Saltar la iteración cuando el contador sea igual a 3
  print("Contador:", counter)

# Bucle while con else
print("Ejemplo 3: Bucle while con else")
counter = 0
while counter <= 5:
  counter += 1  # Incrementar el contador en 1
  print("Contador:", counter)
else:
  print("El bucle ha terminado. El contador es:", counter)

# Else no se ejecuta si se usa break, es decir, si no se cumple la condición del bucle
print("Ejemplo 4: Bucle while con else y break")
counter = 0
while counter <= 5:
  counter += 1  # Incrementar el contador en 1
  if counter == 3:
    break  # Salir del bucle cuando el contador sea igual a 3
else:
  print("El bucle ha terminado. El contador es:", counter)
  # Este else no se ejecutará porque se ha usado break

# Ejecicio práctico: Pedir al usuario un número hasta que ingrese un número negativo
print("Ejercicio práctico: Pedir un número al usuario hasta que ingrese un número negativo")
number = -1  # Inicializar el número en 1 para entrar en el bucle
while number > 0:
  # usar try except para manejar la excepción de que el usuario ingrese un valor no numérico
  try:
    number = int(input("Ingrese un número (número negativo para salir): "))
  except ValueError:
    print("Por favor, ingrese un número válido.")
    continue  # Volver al inicio del bucle si se produce una excepción

  if number >= 0:
    print("Número ingresado:", number)
  else:
    print(f"Número negativo ({number}) ingresado. Saliendo del bucle.")

###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")