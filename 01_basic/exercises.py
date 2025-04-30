###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
print("Hola, soy Yesid.")
print("Vivo en Colombia.")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(f"a: {a}, type: {type(a)}")
print(f"b: {b}, type: {type(b)}")
print(f"c: {c}, type: {type(c)}")
print(f"d: {d}, type: {type(d)}")
print(f"e: {e}, type: {type(e)}")

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
string_num = "12345"
int_num = int(string_num)
print(f"El número entero es: {int_num}, type: {type(int_num)}")

float_num = float(int_num)
print(f"El número float es: {float_num}, type: {type(float_num)}")

float_num = 3.99
int_num = int(float_num)
print(f"El número entero es: {int_num}, type: {type(int_num)}")
print("Al convertir el float 3.99 a un entero, se pieden los decimales (.99).")

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
name = "Yesid"
age = 20
height = 1.70

print(f"Hola! Me llamo {name} y tengo {age} años, mido {height} metros.")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

# 1
PI = 3.14159

# 2
pi_rounded = round(PI)
print(f"PI: {PI}, PI redondeado: {pi_rounded}")

# 3 -> División entera: para hacer una división normal se usa el operador /, para hacer una división entera se usa el operador //
pi_divided = pi_rounded // 2
print(f"PI redondeado y dividido entre 2: {pi_divided}")