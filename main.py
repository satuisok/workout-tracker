import os
import requests
from dotenv import load_dotenv
load_dotenv()

api_headers = {
    "x-app-id": os.getenv("APP_ID"),
    "x-app-key": os.getenv("APP_KEY")
}

parameters = {
    "query": input("Tell about your exercise: "),
    "weight_kg": 79,
    "height_cm": 179.00,
    "age": 35
}


api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
connection = requests.post(url=api_endpoint, json=parameters, headers=api_headers)
connection.raise_for_status()
print(connection.text)