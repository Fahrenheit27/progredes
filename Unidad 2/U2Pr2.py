import requests

def linea(simbolo, longitud):
    """Función para dibujar una línea de símbolos."""
    for _ in range(longitud):
        print(simbolo, end="")
    print() 

def buscar_libro(titulo):
    """Función para buscar un libro en la API de Open Library."""
    url = f'https://openlibrary.org/search.json?q={titulo}' 
    response = requests.get(url)
    print(url)

    if response.status_code != 200:
        print("Error en la solicitud")
        return None
    return response.json()

while True:
    titulo = input("Ingrese el título del libro (o 'salir' para terminar): ").strip()
    if titulo.lower() == 'salir':
        break

    resultados = buscar_libro(titulo)

    if resultados and 'docs' in resultados:
        linea("-", 30)
        print("Resultados de la búsqueda:")
        linea("-", 30)

        for libro in resultados['docs']:
            print(f"Título: {libro['title']}")
            autores = libro.get('authors', [])
            if autores:
                print(f"Autor(es): {', '.join(autor['name'] for autor in autores)}")
            else:
                print("Autor(es): Desconocido")
            print(f"Año de publicación: {libro.get('first_publish_year', 'Desconocido')}")
            print(f"Más información: {libro.get('url', 'No disponible')}")
            linea("-", 30)
    else:
        print("No se encontraron resultados.")
