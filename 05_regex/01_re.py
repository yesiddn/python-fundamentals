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
