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

# 2. Con dependencias externas (usando requests)
import requests
# para instalar requests, ejecutar: pip install requests
# otro package manager es uv

print("GET con requests")
response = requests.get(api_posts)
json = response.json()
print("Response", json)  # Imprimimos el objeto JSON
print("---")
print(f"Respuesta en posición 0: {json[0]}")  # Imprimimos el primer elemento del objeto JSON

# Ejemplo de post
print("POST con requests")
input = {
  "title": "Who am I?",
  "body": "I am a Python developer.",
  "userId": 1
}
try:
  response = requests.post(api_posts, json=input)
  print("Response", response.json())
  print("Status Code:", response.status_code)  # Imprimimos el código de estado de la respuesta
except requests.exceptions.RequestException as e:
  print("Error en la petición:", e)

# Ejemplo de put
print("PUT con requests")
input = {
  "id": 1,
  "title": "Who am I? (updated)",
  "body": "I am a Python developer (updated).",
  "userId": 1
}
try:
  response = requests.put(api_posts + "1", json=input)
  print("Response", response.json())
  print("Status Code:", response.status_code)  # Imprimimos el código de estado de la respuesta
except requests.exceptions.RequestException as e:
  print("Error en la petición:", e)
