###
# 02 - types
# Python tiene varios tipos de datos
# Los tipos de datos más comunes son:
# - int: enteros (números enteros)
# - float: flotantes (números decimales)
# - complex: números complejos (números con parte real e imaginaria)
# - str: cadenas (texto)
# - bool: booleanos (True o False)
# - None: representa la ausencia de valor (nulo)
# - list: listas (colecciones de elementos)
# - tuple: tuplas (colecciones de elementos inmutables)
# - dict: diccionarios (colecciones de pares clave-valor)
# - range: rangos (secuencias de números)
# - set: conjuntos (colecciones de elementos únicos)
###

print("--- 02 - types ---")

###
# type() devuelve el tipo de dato de un objeto
# Se puede usar para verificar el tipo de dato de una variable o un valor
###
print("type()")
print("type(int): ", type(1))  # <class 'int'>
print("type(float): ", type(1.0))  # <class 'float'>

print("int:")
print(100)  # 100
print(24015) # 24015
print(-5)  # -5
print(1234092173409374) # 1234092173409374

print("float:")
print(1.0)  # 1.0
print(1.5)  # 1.5
print(1.5e3)  # 1500.0 (notación científica)
print(1.5e-3)  # 0.0015 (notación científica)

print("complex:")
print(1 + 2j)  # (1+2j) (parte real + parte imaginaria)

print("str:")
print("Hello, World!")  # Hello, World!
print("") # cadena vacía
print("""
  Multilinea
""")  # Multilinea (cadenas multilínea)

print("bool:")
print(True)  # True
print(False)  # False
print(1 == 1)  # True (comparación)

print("NoneType:")
print(None)  # None (nulo)