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