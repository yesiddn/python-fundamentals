###
# 04 - Funciones
# Bloques de código reutilizables y parametrizables para hacer tareas especificas
###

# """ Definición de una función

# def nombre_de_la_funcion(parametro1, parametro2, ...):
#   # docstring
#   # cuerpo de la función
#   return valor_de_retorno # opcional

# """

# Ejemplo de uso de la función
def saludar():
  print("¡Hola, mundo!")

# Llamada a la función
saludar()

# Ejemplo de función con parámetros
def saludar_persona(nombre: str):
  """Función que saluda a una persona por su nombre."""
  print(f"¡Hola, {nombre}!")

# Llamada a la función con un argumento
saludar_persona("Alice")

def sumar(a: int, b: int) -> int:
  """Función que suma dos números enteros y devuelve el resultado."""
  return a + b

result = sumar(5, 3)
print(f"La suma de 5 y 3 es: {result}")

# Acceder a la documentación de la función
print(sumar.__doc__)

# help(sumar) # Muestra la documentación de la función. Se usaba mucho antes cuando los editores no tenían las ayudas de código.

# Ejemplo de función con valor por defecto
def multiplicar(a: int, b: int = 1) -> int:
  """Función que multiplica dos números enteros. El segundo número tiene un valor por defecto de 1."""
  return a * b

result = multiplicar(5)
print(f"La multiplicación de 5 por 1 es: {result}")

# Ejemplo de función con argumentos por posición
def dividir(a: float, b: float) -> float:
  """Función que divide dos números flotantes."""
  if b == 0:
    raise ValueError("No se puede dividir por cero.")
  return a / b

result = dividir(10.0, 2.0)
print(f"La división de 10.0 entre 2.0 es: {result}")

# Ejemplo de función con argumentos por clave
def restar(a: int, b: int) -> int:
  """Función que resta dos números enteros."""
  return a - b

result = restar(b=5, a=10)
print(f"La resta de 10 y 5 es: {result}")

# Ejemplo de función con argumentos de longitud variable (*args)
def sumar_todos(*args: int) -> int:
  """Función que suma todos los números enteros proporcionados como argumentos."""
  return sum(args)

result = sumar_todos(1, 2, 3, 4, 5)
print(f"La suma de todos los números es: {result}")

# Ejemplo de función con argumentos de longitud variable (**kwargs)
def mostrar_info(**kwargs: str) -> None:
  """Función que muestra información proporcionada como argumentos de longitud variable."""
  for clave, valor in kwargs.items():
    print(f"{clave}: {valor}")

mostrar_info(nombre="Alice", ciudad="Madrid", username="alice123")

# Ejercicios
# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora