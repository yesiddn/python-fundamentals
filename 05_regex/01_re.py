##
# 01 - Expresiones regulares
# 

""" Las expresiones regulares son una secuencia de caracteres que forman un patrón de búsqueda.
Se utilizan para la búsqueda de cadenas de texto, validación de datos, etc. 
"""


""" ¿Por qué aprender Regex?

- Búsqueda avanzada: Encontrar patrones específicos en textos grandes de forma rápida y precisa. (un editor de Markdown sólo usando Regex)

- Validación de datos: Asegurarte que los datos que ingresa un usuario como el email, teléfono, etc. son correctos.

- Manipulación del texto: Extraer, reemplazar y modificar partes de la cadena de texto fácilmente
"""

# 1. Importar el módulo de expresiones regulares "re"
import re

# 2. Crear un patrón, que es una cadena de texto que describe lo que queremos encontrar
pattern = "Hola"

# 3. Crear el texto donde queremos buscar el patrón
text = "Hola mundo, este es un ejemplo de Regex."

# 4. Usar la función de búsqueda "re.search()" para encontrar el patrón en el texto
match = re.search(pattern, text) # se pasa el patrón y el texto

if match:
  print("He encontrado el patrón en el texto.")
else:
  print("No he encontrado el patrón en el texto.")

# .group() devuelve el texto que coincide con el patrón
print("Texto encontrado:", match.group())  # Imprime el texto encontrado

# .start() devuelve la posición de inicio del texto encontrado
print("Posición de inicio:", match.start())  # Imprime la posición de inicio del texto encontrado

# .end() devuelve la posición de fin del texto encontrado
print("Posición de fin:", match.end())  # Imprime la posición de fin del texto encontrado

# EJERCICIO 01
# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
# e indica en que posición empieza y termina la coincidencia.
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"
pattern = "IA"

match = re.search(pattern, text)

if match:
  print("He encontrado el patrón en el texto.")
  print("Texto encontrado:", match.group())
  print("Posición de inicio:", match.start())
  print("Posición de fin:", match.end())
else:
  print("No he encontrado el patrón en el texto.")

# ----------------
# Encontrar todas las ocurrencias de un patrón en un texto
# .findall() devuelve una lista con todas las ocurrencias del patrón en el texto

text = "Regex es una herramienta poderosa. Regex es muy útil para buscar patrones en textos. Regex es genial."
pattern = "Regex"

matches = re.findall(pattern, text)

print(f"He encontrado {len(matches)} ocurrencias del patrón '{pattern}' en el texto.")

# ------------------
# .finditer() devuelve un iterador con todas las ocurrencias del patrón en el texto
matches_iter = re.finditer(pattern, text)

for match in matches_iter:
  print(f"Texto encontrado: {match.group()}")
  print(f"Posición de inicio: {match.start()}")
  print(f"Posición de fin: {match.end()}")
  print("---")

# ------------------
# Modificadores (flags)
# Los modificadores son opciones que se pueden agregar a un patrón para cambiar su comportamiento.

# re.IGNORECASE: Ignora mayúsculas y minúsculas al buscar el patrón.
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero la ia no es tan mala. La Ia es genial."
pattern = "IA"
fount_ia = re.findall(pattern, text, re.IGNORECASE)

if fount_ia: print(fount_ia)
print("---")

# Reemplazar texto
# re.sub() reemplaza todas las ocurrencias del patrón en el texto por otro texto
text = "Regex es una herramienta poderosa. Regex es muy útil para buscar patrones en textos. Regex es genial."
pattern = "Regex"
replacement = "Expresiones Regulares"
new_text = re.sub(pattern, replacement, text) # pattern, replacement, text, count=0 (cantidad de veces a reemplazar), flags=0 (modificadores)
print("Texto original:", text)
print("Texto modificado:", new_text)