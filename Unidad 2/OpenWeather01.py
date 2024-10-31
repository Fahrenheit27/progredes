''' 
    Nombre: Fabio Alonso Sánchez García
    Fecha: 14/10/2024
    Actividad: 01
    
'''

import requests

latitud = 21.0188
longitud = 101.2627
clave = "c12301cde3d74ed95133c436b384473a"
main_api = f"https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={clave}"
print(main_api)

json_data = requests.get(main_api).json()
print(json_data)
print(json_data['name'])
