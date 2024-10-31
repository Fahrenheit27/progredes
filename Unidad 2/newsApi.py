''' 
    Nombre: Fabio Alonso Sánchez García
    Fecha: 30/10/2024
    Actividad: Practica APis en casa
    
'''
import requests

def get_news_info(query):

    api_key = "442a8b5c8ee34c6ab147c76e9d4797a0"  
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error    al buscar la noticia: {e}")
        return None

    data = response.json()
    if not data['articles']:
        print("No se encontraron noticias para esa consulta.")
        return None

    first_article = data['articles'][0]

    print(f"Título: {first_article['title']}")
    print(f"Descripción: {first_article['description']}")
    print(f"URL: {first_article['url']}")
    print(f"URL con formato JSON: {url}")

    return first_article

if __name__ == "__main__":
    while True:
        query = input("Ingrese un término de búsqueda para noticias (o 'salir' para terminar): ")
        if query.lower() == "salir":
            break

        news_info = get_news_info(query)

        if news_info:
            print("Información de la noticia:")
        else:
            print("No se encontraron noticias.")

