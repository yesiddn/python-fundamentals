# Cómo hacer peticiones a APIs con Python
# Trabajando sin dependencias externas y con dependencias externas

# 1. Sin dependencias externas (usando urllib)
import urllib.request
import json

api_posts = "https://jsonplaceholder.typicode.com/posts/"

# Para este caso, el codigo se ejecuta uno detras de otro y no hay que preocuparnos de asincronía
try:
  response = urllib.request.urlopen(api_posts) # Le estamos diciendo que abra la URL
  data = response.read()  # Leemos el contenido de la respuesta (el contenido será en bytes)
  json_data = json.loads(data.decode('utf-8'))  # Decodificamos los bytes a string y luego lo convertimos a un objeto JSON
  print(json_data)  # Imprimimos el objeto JSON
  response.close()  # Cerramos la conexión
except urllib.error.URLError as e:
  print("Error:", e.reason)