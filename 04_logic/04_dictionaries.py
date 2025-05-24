###
# 04 - Dictionaries
# Los diccionarios son colecciones de pares clave-valor.
# Sirven para almacenar datos relacionados.
###

# ejemplo de diccionario
person = {
  "name": "John",
  "age": 30,
  "city": "New York",
  "socials": {
    "twitter": "@john",
    "github": "john123"
  }
}

# ejemplo de acceso a un valor
print(person["name"])  # John
print(person["age"])  # 30
print(person["socials"]["twitter"])  # @john

# ejemplo de modificación de un valor
person["age"] = 31
print(person["age"])  # 31

# ejemplo de eliminación de un valor
del person["city"]
print(person)  # {'name': 'John', 'age': 31, 'socials': {'twitter': '@john', 'github': 'john123'}}

# ejemplo de eliminar y devolver un valor
age = person.pop("age")
print(age)  # 31

# ejemplo de sobreescritura de un diccionario con otro diccionario
a = { "name": "John", "age": 30 }
b = { "age": 31, "city": "New York" }
a.update(b)
print(a)  # {'name': 'John', 'age': 31, 'city': 'New York'}

# ejemplo de comprobar si una clave existe en un diccionario
print("name" in person)  # True
print("city" in person)  # False

# ejemplo de obtener todas las claves de un diccionario
print("\nKeys:")
print(person.keys())  # dict_keys(['name', 'socials'])

# ejemplo de obtener todos los valores de un diccionario
print("\nValues:")
print(person.values())  # dict_values(['John', {'twitter': '@john', 'github': 'john123'}])

# ejemplo de obtener todos los pares clave-valor de un diccionario
print("\nItems:")
print(person.items())  # dict_items([('name', 'John'), ('socials', {'twitter': '@john', 'github': 'john123'})])