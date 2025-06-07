import re

# [:]
# Coincide con un conjunto de caracteres
username = "ye$id_123"
pattern = r"^[\w._%+-]+$" # Coincide con caracteres alfanuméricos, guiones bajos, puntos, signos de porcentaje, más y guiones # Debe cumplir con el patrón de principio a fin

match = re.search(pattern, username)

print("\n1. Conjunto de caracteres ([:])")

if match:
  print("Texto:", username)
  print("Patrón:", pattern)
  print("Coincidencia encontrada:", match.group())  # ye$id_123
else:
  print("No se encontró coincidencia.")

# Ejercicio:
# Encontrar vocales de un texto
text = "hola, mundo"
pattern = r"[aeiou]"  # Coincide con cualquier vocal

matches = re.findall(pattern, text)
print("\nEjercicio: Vocales en un texto")
print("Texto:", text)
print("Patrón:", pattern)
print("Vocales encontradas:", matches)  # ['o', 'a', 'u', 'o']  # Coincide con todas las vocales en el texto

