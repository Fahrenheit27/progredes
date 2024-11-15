
import requests
from requests.auth import HTTPBasicAuth
from dnac_config import DNAC_IP, DNAC_PORT, DNAC_USER, DNAC_PASSWORD
def get_device_list():
    #Función para recuperar la lista de dispositivos de red desde Cisco DNA Center.
    token = get_auth_token()  # Obtiene el token de autenticación
    url = "https://sandboxdnac.cisco.com/api/v1/network-device"  # URL del endpoint de dispositivos de red
    hdr = {'x-auth-token': token, 'content-type': 'application/json'}  # Headers de la solicitud

    resp = requests.get(url, headers=hdr, verify=False)  # Realiza la solicitud GET

    device_list = resp.json()  # Convierte la respuesta a JSON
    print_device_list(device_list)  # Imprime la lista de dispositivos
def print_device_list(device_json):
    # Imprime el encabezado de la tabla con nombres de columnas, ajustado para alinearse.
    print("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
          format("hostname", "mgmt IP", "serial", "platformId", "SW Version", "role", "Uptime"))
    
    # Itera sobre cada dispositivo en la respuesta JSON.
    for device in device_json['response']:
        # Asigna "N/A" al tiempo de actividad si el valor es None; de lo contrario, usa el valor de 'upTime'.
        uptime = "N/A" if device['upTime'] is None else device['upTime']
        
        # Verifica si el número de serie contiene comas (indicando varios números de serie).
        if device['serialNumber'] is not None and "," in device['serialNumber']:
            # Empareja cada número de serie con su correspondiente platformId en una lista de tuplas.
            serialPlatformList = zip(device['serialNumber'].split(","), device['platformId'].split(","))
        else:
            # Si solo hay un número de serie y un platformId, los agrupa en una tupla única.
            serialPlatformList = [(device['serialNumber'], device['platformId'])]
        
        # Itera sobre cada par (serialNumber, platformId) en la lista.
        for (serialNumber, platformId) in serialPlatformList:
            # Imprime los detalles de cada dispositivo en formato tabular.
            print("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
                  format(device['hostname'],
                         device['managementIpAddress'],
                         serialNumber,
                         platformId,
                         device['softwareVersion'],
                         device['role'], uptime))
def get_auth_token():
    """
    Construye y envía una solicitud de autenticación para obtener un token de Cisco DNA Center.
    """
    # Define la URL del endpoint de autenticación de Cisco DNA Center.
    url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'       

    resp = requests.post(url, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASSWORD), verify=False)

    # Extrae el token de autenticación desde la respuesta JSON.
    token = resp.json()['Token']    

    # Devuelve el token de autenticación para su uso en futuras solicitudes.
    return token 
if __name__ == "__main__":
    get_device_list()