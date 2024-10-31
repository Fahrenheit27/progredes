''' 
    Nombre: Fabio Alonso Sánchez García
    Fecha: 30/10/2024
    Actividad: Practica APis en casa
    
'''

import requests

def get_swapi_info(resource, id=None, search=None):

  base_url = "https://www.swapi.tech/api/"
  url = f"{base_url}{resource}/{id}/" if id else f"{base_url}{resource}"

  if search:
      url += f"?search={search}"

  try:
      response = requests.get(url)
      response.raise_for_status()  # Raise an exception for bad status codes
  except requests.exceptions.RequestException as e:
      print(f"Error al buscar la información: {e}")
      return None

  data = response.json()

  return data['result']['properties'] if 'result' in data else None

if __name__ == "__main__":
  while True:
      resource = input("Ingrese el recurso a buscar (e.g., 'films', 'planets', 'people') o 'salir': ")
      if resource.lower() == "salir":
          break

      resource_id = input("Ingrese el ID del recurso (si aplica, o dejar en blanco): ")
      search_term = input("Ingrese un término de búsqueda (opcional): ")

      data = get_swapi_info(resource, resource_id, search_term)

      if data:
          # Print relevant information based on resource
          if resource == 'films':
              # Access data based on your needs (titles, episode numbers, etc.)
              print(f"Películas encontradas:")
              # Iterate through data if it's a list
              for item in data:
                  print(f"- {item['title']}")  # Assuming 'title' exists

          elif resource == 'planets':
              print(f"Nombre: {data['name']}")
              print(f"Clima: {data['climate']}")
              # Access other properties as needed

          elif resource == 'people':
              print(f"Nombre: {data['name']}")
              print(f"Altura: {data['height']}")
              # Access other properties as needed

          else:
              print(data)  # Print all data for unrecognized resources
      else:
          print("No se encontró la información.")

