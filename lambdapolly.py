import requests
import base64
import json

# URL de tu API
api_url = "https://56q2rxpufj.execute-api.us-east-2.amazonaws.com/prod/synthesize?text=hola,%20%C2%BFcomo%20estas?%20yo%20estoy%20muy%20bien"


# Hacer la solicitud GET a la API
response = requests.get(api_url)

# Comprobar si la solicitud fue exitosa
if response.status_code == 200:
    # Parsear la respuesta JSON
    response_data = response.json()

    # Obtener el contenido de audio en base64
    audio_base64 = response_data.get('audioContent')

    if audio_base64:
        # Decodificar el contenido de audio
        audio_data = base64.b64decode(audio_base64)

        # Guardar el audio en un archivo
        with open("output.mp3", "wb") as audio_file:
            audio_file.write(audio_data)

        print("Archivo guardado como output.mp3")
    else:
        print("No se encontró el contenido de audio en la respuesta.")
else:
    print(f"Error en la solicitud: {response.status_code}")
    print(response.text)
