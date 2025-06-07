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

# Ejercicio:
# Encontrar las palabras man, fan y ban
text = "man ran fan ban can omniman"
pattern = r"\b[mbf]an\b"  # Coincide con palabras que empiezan con m, b o f y terminan con an
matches = re.findall(pattern, text)
print("\nEjercicio: Palabras que empiezan con m, b o f y terminan con an")
print("Texto:", text)
print("Patrón:", pattern)
print("Palabras encontradas:", matches)  # ['man', 'fan', 'ban']

# Rango de numeros
text = "abc ABC 123 !@#"
pattern = r"[0-9]"  # Coincide con cualquier dígito del 0 al 9
matches = re.findall(pattern, text)
print("\nEjercicio: Dígitos en un texto")
print("Texto:", text)
print("Patrón:", pattern)
print("Dígitos encontrados:", matches)  # ['1', '2', '3']

# Rango de letras
pattern = r"[a-zA-Z]"  # Coincide con cualquier letra mayúscula o minúscula
matches = re.findall(pattern, text)
print("\nEjercicio: Letras en un texto")
print("Texto:", text)
print("Patrón:", pattern)
print("Letras encontradas:", matches)  # ['a', 'b', 'c', 'A', 'B', 'C']

# Rango de caracteres especiales
pattern = r"[^a-zA-Z0-9]"  # Coincide con cualquier carácter que no sea una letra o un dígito
matches = re.findall(pattern, text)
print("\nEjercicio: Caracteres especiales en un texto")
print("Texto:", text)
print("Patrón:", pattern)
print("Caracteres especiales encontrados:", matches)  # ['$', '_', ' ', '!', '@', '#'] 

# Ejercicio final con todo lo aprendido
# Mejorar esto: https://www.computerhope.com/jargon/r/regular-expression.png

## Buscar corner cases que no pasa y arreglarlo:
"lo.que+sea@shopping.online"
"michael@gov.co.uk"