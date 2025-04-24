###
# 03 - casting de tipos
# Transformar un tipo de dato a otro 
###

print("--- 03 - casting ---")
print("--- int() ---")

print("'100'")
print(type("100"))  # <class 'str'>
print("int('100')")
print(type(int("100")))  # <class 'int'>

print("--- example ---")
print("int('200') + 1")
print(int("200") + 1)  # 201 (suma de enteros)
print("3.1416 to int")
print("int(3.1416)")
print(int(3.1416))  # 3 (truncamiento de decimales)

print("--- str() ---")

print("100")
print(type(100))  # <class 'int'>
print("str(100)")
print(type(str(100)))  # <class 'str'>

print("--- example ---")
print("str(100) + '1'")
print(str(100) + '1')  # 1001 (concatenación de cadenas)

print("--- float() ---")
print("'3.1416'")
print(type("3.1416"))  # <class 'str'>
print("float('3.1416')")
print(type(float("3.1416")))  # <class 'float'>

print("--- example ---")
print("float('3.1416') + 1")
print(float("3.1416") + 1)  # 4.1416 (suma de flotantes)

print("--- bool() ---")
print("bool(0)")
print(bool(0))  # False (0 es falso)
print("bool(1)") 
print(bool(1))  # True (< 0 > es verdadero)
print("bool('')")
print(bool(''))  # True (cadena no vacía es verdadero)
print("bool(' ')")
print(bool(' '))  # True (cadena no vacía es verdadero)
print("bool('False')")
print(bool('False'))  # True (cadena no vacía es verdadero)
print("bool(-1)") 
print(bool(-1)) # True (-1 es verdadero)