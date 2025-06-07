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

# ?
# Coincide con cero o una ocurrencia del patrón anterior
text = "aaabaacb"
pattern = r"a?b" # Coincide con cero o una 'a'

found = re.findall(pattern, text)
print("\n3. Cero o una ocurrencia (?)")
print("Texto:", text)
print("Patrón:", pattern)
print("Resultados encontrados:", found) # ['ab', 'b']

# Ejercicio:
# Hacer opcional que aparezca el +34 antes del número de teléfono
text = "+34 987654321 34 123456789 987654321 123456789"
pattern = r"\+?34 \d{9}" # Coincide con un número de teléfono que puede empezar con +34 o solo 34

found = re.findall(pattern, text)
print("\nEjercicio: Números de teléfono con +34 opcional")
print("Texto:", text)
print("Patrón:", pattern)
print("Resultados encontrados:", found)  # ['+34 987654321', '34 123456789']  # Coincide con los números de teléfono que cumplen el patrón
