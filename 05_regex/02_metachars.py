###
# 02 - Meta caracteres
# Los metacaracteres son simbolos especiales con significados especificos en las expresiones regulares
###

import re

# 1. Punto (.)
# El punto coincide con cualquier caracter excepto el salto de linea
text = "Hola, mundo! H0la, Python! H)la, Regex!"
pattern = "H.la"

found = re.findall(pattern, text)
print("1. Punto (.)")
print("Texto:", text)
print("Patrón:", pattern)
print("Resultados encontrados:", found)

# ---
# Aunque se pueden usar regex como cadenas de texto, lo recomendable es usar raw strings (r"") 
text = "Mi casa es blanca. Y el coche es rojo."
pattern = r"\." # de esta forma el punto se interpreta literalmente, asi se anula el significado especial del punto (u otro metacaracter)
found = re.findall(pattern, text)
print("\nTexto:", text)
print("Patrón:", pattern)
print("Resultados encontrados:", found)

# 2. Digitos (\d)
# Coincide con cualquier digito (0-9)
text = "Mi número es 12345 y mi código postal es 28080."
pattern = r"\d"
found = re.findall(pattern, text) # esto devuelve una lista con todos los dígitos encontrados
# Si queremos encontrar un número completo, podemos agrupar \d, es decir, si queremos tres numeros consecutivos, usamos \d\d\d

print("\n2. Dígitos (\\d)")
print("Texto:", text)
print("Patrón:", pattern)
print("Resultados encontrados:", found)

# Cuantificadores
# Una forma de agrupar los dígitos es usando los cuantificadores
# {n} - Coincide con exactamente n ocurrencias del patrón
pattern = r"\d{5}"  # Coincide con exactamente 5 dígitos
found = re.findall(pattern, text)
print("\nCuantificadores:")
print("Texto:", text)
print("Patrón:", pattern)
print("Resultados encontrados:", found)

# Ejercicio: Detectar si hay un número de España en el texto gracias al prefijo +34
text = "Mi número de teléfono es +34 612 345 678. Apuntalo, vale?"
pattern = r"\+34 \d{3} \d{3} \d{3}"  # Coincide con el formato +34 xxx xxx xxx
found = re.findall(pattern, text)
print("\nEjercicio: Número de España")
print("Texto:", text)
print("Patrón:", pattern)
print("Resultados encontrados:", found)

# 3. Alfa numéricos (\w)
# Coincide con cualquier caracter alfanumérico (letras [a-z, A-Z], números [0-9] y guiones bajos)
text = "# Hola, mundo! H0la, Python! H)la, Regex!"
pattern = r"\w"  # Coincide con cualquier caracter alfanumérico

found = re.findall(pattern, text)
print("\n3. Alfanuméricos (\\w)")
print("Texto:", text)
print("Patrón:", pattern)
print("Resultados encontrados:", found) # se ignoran los caracteres especiales como #, !, ), etc.

# 4. Espacios (\s)
# Coincide con cualquier espacio en blanco (espacio, tabulación [\t], salto de línea [\n], etc.)
text = "Hola,\tmundo!\nHola, Python!\nHola, Regex!"
pattern = r"\s"  # Coincide con cualquier espacio en blanco

found = re.findall(pattern, text)
print("\n4. Espacios (\\s)")
print("Texto:", text)
print("Patrón:", pattern)
print("Resultados encontrados:", found)

# 5. Inicio (^) 
# Coincide con el inicio de una cadena
username = "_usuario123"
pattern = r"^\w"  # Validar nombre de usuario

valid = re.search(pattern, username)  
print("\n5. Inicio (\\^)")
print("Texto:", username)
print("Patrón:", pattern)

if valid: print("Resultado: El nombre de usuario es válido.")
else: print("Resultado: El nombre de usuario no es válido.")

# Validar numero de teléfono
phone_number = "+34 612 345 678"
pattern = r"^\+\d{2,3} "

valid = re.search(pattern, phone_number)
print("\nValidación de número de teléfono")
print("Texto:", phone_number)
print("Patrón:", pattern)

if valid: print("Resultado: El número de teléfono es válido.")
else: print("Resultado: El número de teléfono no es válido.")

# 6. Fin ($)
# Coincide con el final de una cadena
text = "Hola, mundo!"
pattern = r"mundo!$"  # Validar que la cadena termina con "mundo!"
valid = re.search(pattern, text)

print("\n6. Fin ($)")
print("Texto:", text)
print("Patrón:", pattern)
if valid: print("Resultado: La cadena termina con 'mundo!'.")
else: print("Resultado: La cadena no termina con 'mundo!'.")

# EJERCICIO:
# Tenemos una lista de archivos, necesitamos saber los nombres de los ficheros con extension .txt
files = "file1.txt file2.pdf midu-of.webp secret.txt"

# 7. Principio o final de una palabra (\b)
# Coincide con el principio o final de una palabra
text = "casa casada cosa cosas casado casa"
pattern = r"\bc.sa\b"  # Coincide con la palabra "casa" completa
found = re.findall(pattern, text)
print("\n7. Principio o final de una palabra (\\b)")
print("Texto:", text)
print("Patrón:", pattern)
print("Resultados encontrados:", found)
