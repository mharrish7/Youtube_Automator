import requests
import sys 
import time

try:
    secret = open("gemini_secret.txt")
except:
    print("GEMINI SECRET NOT FOUND. Please name it as gemini_secret.txt")
    print("Paste the Key in the text file")
    print("QUITTING in 5 Seconds")
    time.sleep(5)
    sys.exit()
API_KEY = secret.read().strip()
if API_KEY == "":
    print("GEMINI SECRET EMPTY")
    print("QUITTING in 5 Seconds")
    time.sleep(5)
    sys.exit()

URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=" + API_KEY


# Todo: Handle invalid Gemini API keys.
def query(text):
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": text}
                ]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(URL, json=payload, headers=headers)

    # Check for successful response
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
