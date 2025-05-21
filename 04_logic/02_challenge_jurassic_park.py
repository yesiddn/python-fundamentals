"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).
"""

eggs = [2, 3, 4, 5, 6, 7, 8, 9, 10]

def sum_carnivore_eggs(egg_list: list[int]) -> int:
  """
  Suma los huevos de los dinosaurios carnívoros (números pares) en una lista.

  Args:
    eggs: Lista de números enteros que representan la cantidad de huevos.

  Returns:
    La suma total de los huevos de los dinosaurios carnívoros.
  """

  total_carnivore_eggs = 0

  for eggs in egg_list:
    if eggs % 2 == 0:
      total_carnivore_eggs += eggs

  return total_carnivore_eggs

# Test cases
print(sum_carnivore_eggs(eggs))  # 30
print(sum_carnivore_eggs([1, 3, 5, 7]))  # 0
print(sum_carnivore_eggs([2, 4, 6, 8]))  # 20
print(sum_carnivore_eggs([1, 2, 3, 4, 5]))  # 6
