###
# 03 - Quantifiers
# Los cuantificadores se utilizan para especificar cuántas ocurrencias de un carácter o grupo de caracteres se deben encontrar en una cadena.
###

import re

# *
# Coincide con cero o más ocurrencias del patrón anterior
text = "aaaba"
pattern = r"a*"  # Coincide con cero o más 'a'
found = re.findall(pattern, text)
print("\n1. Cero o más ocurrencias (*)")
print("Texto:", text)
print("Patrón:", pattern)
print("Resultados encontrados:", found) # ['aaa', '', '', 'b', '']  # Coincide con todas las 'a' y los espacios entre ellas

# Ejercicio:
# ¿Cuántas palabras tienen de 0 a más "a" y después una "b"?
text = "aaaba aav ab aa b"
pattern = r"a*b"  # Coincide con cero o más 'a' seguidas de una 'b'
found = re.findall(pattern, text)
print("\nEjercicio: Palabras con cero o más 'a' y una 'b'")
print("Texto:", text)
print("Patrón:", pattern)
print("Resultados encontrados:", found)  # ['aaab', 'aab', 'ab', 'b']  # Coincide con todas las palabras que cumplen el patrón

# +
# Coincide con una o más ocurrencias del patrón anterior
text = "aaaba ddd dda ccc bbba dadaddd"
pattern = r"a+"  # Coincide con una o más 'a'

found = re.findall(pattern, text)
print("\n2. Una o más ocurrencias (+)")
print("Texto:", text)
print("Patrón:", pattern)
print("Resultados encontrados:", found)  # ['aaa', 'a', 'a']  # Coincide con todas las 'a' que aparecen al menos una vez
