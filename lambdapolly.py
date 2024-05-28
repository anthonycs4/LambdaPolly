import requests
import base64
import json

# Prompt the user to enter the text to synthesize
text = input("Enter the text to synthesize: ")

# URL of the Polly API with the text as a parameter
api_url = f"https://2k2pcb479g.execute-api.us-east-2.amazonaws.com/prod/?text={text}"

# Make a GET request to the API
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    response_data = response.json()

    # Get the audio content in base64
    audio_base64 = response_data.get('body')
    body_json = json.loads(audio_base64)
    audio_base64_value = body_json.get('audio_base64')

    # Print the base64 audio content
    print("Base64 audio content:", audio_base64_value)

    if audio_base64_value:
        # Decode the audio content
        audio_data = base64.b64decode(audio_base64_value)

        # Save the audio to a file
        with open("output.mp3", "wb") as audio_file:
            audio_file.write(audio_data)

        print("File saved as output.mp3")
    else:
        print("No audio content found in the response.")
else:
    print(f"Error in the request: {response.status_code}")
    print(response.text)
