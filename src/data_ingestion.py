import requests
import os 
from dotenv import load_dotenv


load_dotenv()

def getMtaData(route: str):

    mta_auth = os.getenv("API_KEY_ID")
    mta_secret = os.getenv("API_KEY_SECRET")

    headers = {'Authorization': f'Basic {mta_auth}:{mta_secret}'}

    response = requests.get(route, headers=headers)

    if response.status_code == 200:
        response = response.json()
        return response
    else:
        print(f"Error {response.status_code}: {response.text}")


