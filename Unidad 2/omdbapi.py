''' 
    Nombre: Fabio Alonso Sánchez García
    Fecha: 30/10/2024
    Actividad: Practica APis en casa
    
'''

import requests

def get_movie_info(title):
 
  api_key = "7cafc42d"  
  url = f"http://www.omdbapi.com/?t={title}&apikey={api_key}"
  
  json_data = requests.get(url).json()
  print(json_data)
  print(url)

  try:
    response = requests.get(url)
    response.raise_for_status()
  except requests.exceptions.RequestException as e:
    print(f"Error  al buscar la película: {e}")
    return None

  data = response.json()
  if data["Response"] == "False":
    print(f"Película no encontrada: {data['Error']}")
    return None

  return data

if __name__ == "__main__":
  while True:
    titulo = input("Ingrese el título de una película (o 'salir' para terminar): ")
    if titulo.lower() == "salir":
      break

    info_pelicula = get_movie_info(titulo)

    if info_pelicula:
      print("Información de la película:")
      for clave, valor in info_pelicula.items():
        print(f"{clave}: {valor}")
    else:
      print("Película no encontrada.")

