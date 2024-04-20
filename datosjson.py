import json
from datetime import datetime, timedelta

# Abrir el archivo JSON
with open('myfile.json') as json_file:
    # Cargar el archivo JSON en una variable llamada json_data
    json_data = json.load(json_file)

# Obtener el valor del token y tiempo restante antes de que caduque
token = json_data.get("access_token", "")
expires_in_seconds = json_data.get("expires_in", 0)

# Calcular la fecha y hora de expiración del token
tiempo_expiracion = datetime.now() + timedelta(seconds=expires_in_seconds)

# Imprimir el valor del token y la fecha y hora de expiración
print("Valor del token:", token)
print("Fecha y hora de expiración del token:", tiempo_expiracion)
