"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

# forma de resolver el problema sin uso de diccionarios
# def find_first_sum(nums: list[int], goal: int) -> list[int] | None:
#   for i in range(len(nums) - 1):
#     for j in range(i + 1, len(nums)):
#       if nums[i] + nums[j] == goal:
#         return [i, j]
      
#   return None

# nums = [4, 5, 6, 2]
# goal = 8

# print(find_first_sum(nums, goal))  # [2, 3]
# print(find_first_sum([1, 2, 3, 4], 5))  # [0, 3]
# print(find_first_sum([1, 2, 3, 4], 10))  # None
# print(find_first_sum([1, 2, 3, 4, 3], 6))  # [2, 4]

# Solución usando diccionarios
def find_first_sum(nums: list[int], goal: int) -> list[int] | None:
  seen: dict[int, int] = {} # Diccionario para almacenar los números vistos y sus índices

  for i, num in enumerate(nums):
    missing = goal - num  # Calcula el número que falta para alcanzar el objetivo
    if missing in seen:
      return [seen[missing], i]  # Si el número que falta ya está en el diccionario, devuelve sus índices
    seen[num] = i  # Almacena el índice del número actual en el diccionario

  return None

nums = [4, 5, 6, 2]
goal = 8
result = find_first_sum(nums, goal)  # [2, 3]
print(result)

print(find_first_sum([1, 2, 3, 4], 5))  # [1, 2]
print(find_first_sum([1, 2, 3, 4], 10))  # None
print(find_first_sum([1, 2, 3, 4, 3], 6))  # [1, 3]