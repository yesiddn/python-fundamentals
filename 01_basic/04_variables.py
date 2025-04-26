###
# 04 - Variables
# Python es un lenguaje de tipado dinámico y también de tipado fuerte.
###

# Asignación de variables
# Se puede asignar un valor a una variable usando el operador de asignación (=)
my_name = "Yesid"

print("my_name: ", my_name)  # my_name: Yesid

# Reasignación de variables
age = 20
print("age: ", age)  # age: 20

age = 21
print("age: ", age)  # age: 21

# Tipado dinámico: Python permite cambiar el tipo de dato de una variable en tiempo de ejecución
age = "twenty-one"
print("age: ", age)  # age: twenty-one
print("type(age): ", type(age))  # type(age): <class 'str'>

# Tipado fuerte: Python no permite realizar operaciones entre diferentes tipos de datos sin una conversión explícita
# print(age + 1)  # TypeError: can only concatenate str (not "int") to str

# Para poder mostrar en consola una variable int con un string, se puede usar las f-strings (format strings)
age = 21
print(f"My name is {my_name} and I am {age} years old")  # My name is Yesid and I am 21 years old

# ❌ No se recomienda declarar mas de una variable en la misma línea, ya que puede dificultar la lectura del código
# my_name, age = "Yesid", 21

# Convención de nombres de variables
# Se recomienda usar snake_case para los nombres de las variables, es decir, usar minúsculas y guiones bajos para separar palabras
# Ejemplo: my_name, my_age, my_favorite_color, MI_CONSTANTE, etc.

# COSNTANTES: Pyhton no soporta constantes, pero se puede simular usando UPPER_CASE como convención
# Ejemplo: PI = 3.14, MAX_VALUE = 100, etc.

# Palabras reservadas: Python tiene un conjunto de palabras reservadas que no se pueden usar como nombres de variables
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
#  'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in',
#  'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with',
#  'yield']

# Types annotation: Python permite usar anotaciones de tipo para indicar el tipo de dato de una variable
# Ejemplo: my_name: str = "Yesid", age: int = 21, is_student: bool = True, etc.
is_user_logged_in: bool = True
print("is_user_logged_in: ", is_user_logged_in)  # is_user_logged_in: True

# Las anotaciones no impiden que se le asigne un valor diferente a la variable, por lo que no son estrictas
# is_user_logged_in = 23
# print("is_user_logged_in: ", is_user_logged_in)  # is_user_logged_in: 23

# El editor puede ayudar a detectar errores de tipo, pero no es obligatorio. Esto se hace llendo a Preferences > Type Checking Mode > Strict
# o usando un linter como pylint o flake8