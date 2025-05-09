###
# 04 - Listas Métodos
# Los métodos más importantes para trabajar con listas
###

letters = ['a', 'b', 'c', 'd', 'e']
print(letters)  # ['a', 'b', 'c', 'd', 'e']

# append() - Agrega un elemento al final de la lista
letters.append('f')
print(letters)  # ['a', 'b', 'c', 'd', 'e', 'f']

# insert() - Agrega un elemento en una posición específica de la lista
letters.insert(2, 'x') # Agrega 'x' en la posición 2
print(letters)  # ['a', 'b', 'x', 'c', 'd', 'e', 'f']

# extend() - Agrega varios elementos al final de la lista
letters.extend(['g', 'h', 'i', 'x'])
print(letters)  # ['a', 'b', 'x', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'x']

# remove() - Elimina el primer elemento de la lista que coincida con el valor especificado
letters.remove('x')
print(letters)  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'x']

# pop() - Elimina y devuelve el último elemento de la lista (o el elemento en la posición especificada)
last = letters.pop()  # Elimina 'x' # el valor por defecto es -1
print(last)  # 'x'
print(letters)  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

# Eliminar el segundo elemento de la lista
second = letters.pop(1)  # Elimina 'b'
print(second)  # 'b'
print(letters)  # ['a', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'x']

# del - Elimina a lo bestia un elemento de la lista en la posición especificada (o toda la lista si no se especifica)
del letters[-1]  # Elimina 'i'
print(letters)  # ['a', 'c', 'd', 'e', 'f', 'g', 'h']

# Eliminar un rango de elementos de la lista
del letters[1:4]  # Elimina ['c', 'd', 'e']
print(letters)  # ['a', 'f', 'g', 'h']

# clear() - Elimina todos los elementos de la lista
letters.clear()
print(letters)  # []

# Ordenar listas
numbers = [5, 10, 2, 9, 1, 5, 6]
numbers.sort()  # Ordena la lista en orden ascendente, pero modifica la lista original
print(numbers)  # [1, 2, 5, 5, 6, 9, 10] -> a diferencia de javascript, ordena correctamente los números 

# Ordenar lista creando una nueva lista
numbers = [5, 10, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 2, 5, 5, 6, 9, 10]

# Ordenar lista de strings
fruits = ['banana', 'apple', 'cherry', 'date', 'Avocado']
sorted_fruits = sorted(fruits)  # Ordena la lista en orden alfabético
print(sorted_fruits)  # ['Avocado', 'apple', 'banana', 'cherry', 'date'] # primero mayúscula, luego minúscula

# Para ordenar ignorando mayúsculas y minúsculas, se puede usar el parámetro key
sorted_fruits = sorted(fruits, key=str.lower)  # Ordena la lista en orden alfabético ignorando mayúsculas y minúsculas
fruits.sort(key=str.lower)
print(sorted_fruits)  # ['apple', 'Avocado', 'banana', 'cherry', 'date']

# count() - Cuenta el número de veces que aparece un elemento en la lista
numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
count = numbers.count(1)
print(count)  # 2

# in - Verifica si un elemento está en la lista
numbers = [1, 2, 3, 4, 5]
print(1 in numbers)  # True
print(6 in numbers)  # False

###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.