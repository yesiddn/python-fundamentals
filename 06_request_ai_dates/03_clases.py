# 1. Introducción a las Clases en Python
# Las clases son plantillas para crear objetos. Un objeto es una instancia de una clase.
# Nos permite agrupar datos (atributos o propiedades) y funciones (métodos) en un solo lugar.

# Ejemplo básico de una clase
import requests


class Coche:
  # Atributos de la clase
  tipo = "Vehículo de cuatro ruedas"

  # Método constructor
  # se llama automáticamente al crear una instancia de la clase
  def __init__(self, marca: str, modelo: str, color: str):
    self.marca = marca  # Atributo de instancia
    self.modelo = modelo  # Atributo de instancia
    self.color = color  # Atributo de instancia

  def arrancar(self):
    """
    Método para arrancar el coche.
    """
    print(f"El coche {self.marca} {self.modelo} de color {self.color} está arrancando. 🏎️")

mi_coche = Coche("Toyota", "Corolla", "Rojo")
mi_coche.arrancar()

otro_coche = Coche("Ford", "Mustang", "Azul")
otro_coche.arrancar()

class AI_API:
    """
    Clase para interactuar con la API de OpenAI.
    """

    def __init__(self, api_key: str, url: str = "https://api.openai.com/v1/chat/completions", model: str = "gpt-3.5-turbo"):
      self.api_key = api_key
      self.url = url
      self.model = model

    def call(self, prompt: str):
      """
      Llama a la API de OpenAI con el prompt proporcionado.
      """
        
      headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {self.api_key}"
      }
      data = {
        "model": self.model,
        "messages": [
          {
            "role": "user",
            "content": prompt
          }
        ]
      }

      try:
        response = requests.post(self.url, headers=headers, json=data)
        # response.raise_for_status()  # Lanza un error si la respuesta no es exitosa
        res_json = response.json()
        return res_json["choices"][0]["message"]["content"]
      except requests.exceptions.RequestException as e:
        return f"Error en la petición a la API: {e}"
      except KeyError:
        return "Error al procesar la respuesta de la API."
      except Exception as e:
        return f"Ocurrió un error inesperado: {e}"

openai_api = AI_API("sk-...")
api_response = openai_api.call("Escribe un poema sobre Python y la programación.")
print("Respuesta de OpenAI:")
print(api_response)

deepseek_api = AI_API("sk-...", url="https://api.deepseek.com/v1/chat/completions", model="deepseek-chat")
deepseek_response = deepseek_api.call("Escribe un poema sobre Python y la programación.")
print("Respuesta de DeepSeek:")
print(deepseek_response)
