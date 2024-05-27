import requests
import base64
import json

# Prompt the user to enter the text to synthesize
text = input("Enter the text to synthesize: ")

# URL of the Polly API with the text as a parameter
api_url = f"https://56q2rxpufj.execute-api.us-east-2.amazonaws.com/prod/synthesize?text={text}"

# Make a GET request to the API
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    response_data = response.json()

    # Get the audio content in base64
    audio_base64 = response_data.get('audioContent')

    if audio_base64:
        # Decode the audio content
        audio_data = base64.b64decode(audio_base64)

        # Save the audio to a file
        with open("output.mp3", "wb") as audio_file:
            audio_file.write(audio_data)

        print("File saved as output.mp3")
    else:
        print("No audio content found in the response.")
else:
    print(f"Error in the request: {response.status_code}")
    print(response.text)
