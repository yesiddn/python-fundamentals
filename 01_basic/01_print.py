###
# 01 - print()
# Sirve para imprimir en consola
# Se puede usar para imprimir variables, cadenas, números, etc.
# Se puede usar con comillas simples o dobles
###

print("Hello, World!")

# Se pueden imprimir varios elementos. print() separa los elementos por un espacio por default
print("Python", "es", "genial")

# Se puede cambiar el separador por defecto (espacio) usando el argumento sep
print("Python", "es", "genial", sep="-")

# Por default print() añade un salto de línea (\n) al final
print("Esto se imprime")
print("en dos líneas")

# Se puede cambiar el final de la línea por defecto (nueva línea) usando el argumento end
print("Esto se imprime", end=" ") 
print("en la misma línea")