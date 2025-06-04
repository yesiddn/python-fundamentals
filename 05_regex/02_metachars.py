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
