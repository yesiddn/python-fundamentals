###
# 03 - Listas
# Secuencias mutables de elementos.
# Pueden contener elementos de diferentes tipos.
###

# Creación de una lista
print("Creación de una lista")
mi_lista = [1, 2, 3, 4, 5] # Lista de enteros
string_lista = ["Hola", "Mundo"] # Lista de strings
lista_mixta: list[int | str | float | bool] = [1, "Hola", 3.14, True] # Lista mixta
# lista_vacia = [] # Lista vacía
lista_vacia: list[int] = [] # Lista vacía
list_de_listas = [[1, 2], [3, 4], [5, 6]] # Lista de listas
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz (lista de listas)

# Los datos mostrados son iguales que como se escriben en el código
print(mi_lista) # [1, 2, 3, 4, 5]
print(string_lista) # ["Hola", "Mundo"]
print(lista_mixta) # [1, "Hola", 3.14, True]
print(lista_vacia) # []
print(list_de_listas) # [[1, 2], [3, 4], [5, 6]]
print(matrix) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Acceso a elementos por índice
print("\nAcceso a elementos por índice")
fruits = ["manzana", "banana", "cereza"]
print(fruits[0]) # "manzana"
print(fruits[1]) # "banana"
print(fruits[-1]) # "cereza" (último elemento)
print(fruits[-2]) # "banana" (penúltimo elemento)
print(list_de_listas[1][0]) # 3 (accediendo a la lista de listas)

# Slicing de listas
print("\nSlicing de listas")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:5]) # [3, 4, 5] (índices 2 a 4)
print(numbers[:4]) # [1, 2, 3, 4] (primeros 4 elementos)
print(numbers[5:]) # [6, 7, 8, 9] (desde el índice 5 hasta el final)
print(numbers[-3:]) # [7, 8, 9] (últimos 3 elementos)
print(numbers[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9] (copia de toda la lista)

# El tercer parámetro es el paso (step)
print(numbers[1:8:2]) # [2, 4, 6, 8] (índices 1 a 7, cada segundo elemento)
print(numbers[::2]) # [1, 3, 5, 7, 9] (cada segundo elemento)
print(numbers[::-1]) # [9, 8, 7, 6, 5, 4, 3, 2, 1] (inversa de la lista)

# Modificación de listas
print("\nModificación de listas")
# Cambiar un elemento
numbers[2] = 10
print(numbers) # [1, 2, 10, 4, 5, 6, 7, 8, 9]

# Añadir elementos
print("\nAñadir elementos")
numbers = numbers + [11, 12] # Concatenación de listas
print(numbers) # [1, 2, 10, 4, 5, 6, 7, 8, 9, 11, 12]

numbers += [13, 14] # Forma corta y eficiente
print(numbers) # [1, 2, 10, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14]

###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]