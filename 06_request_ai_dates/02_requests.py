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
json_response = response.json()
print("Response", json_response)  # Imprimimos el objeto JSON
print("---")
print(f"Respuesta en posición 0: {json_response[0]}")  # Imprimimos el primer elemento del objeto JSON

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

# Usar la API de OpenAI (platform.openai.com)

OPENAI_KEY = "sk-..." # Reemplaza con tu propia clave de API de OpenAI

def call_openai_gpt(api_key: str, prompt: str):
  """
  Llama a la API de OpenAI con el prompt proporcionado.
  """
  
  url = "https://api.openai.com/v1/chat/completions"
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }
  data = {
    "model": "gpt-3.5-turbo",
    "messages": [
      {
        "role": "user",
        "content": prompt
      }
    ]
  }

  try:
    response = requests.post(url, headers=headers, json=data)
    # response.raise_for_status()  # Lanza un error si la respuesta no es exitosa
    return response.json()
  except requests.exceptions.RequestException as e:
    print("Error en la petición a OpenAI:", e)
  except KeyError:
    print("Error al procesar la respuesta de OpenAI.")
  except Exception as e:
    print("Ocurrió un error inesperado:", e)

api_response = call_openai_gpt(OPENAI_KEY, "Escribe un poema sobre Python y la programación.")

# formatear json con dumps
print(json.dumps(api_response, indent=2))  # Imprimir la respuesta formateada

print("Respuesta de OpenAI:")
print(api_response["choices"][0]["message"]["content"])
