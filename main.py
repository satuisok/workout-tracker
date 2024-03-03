import os
import requests
from datetime import datetime as dt
from dotenv import load_dotenv

load_dotenv()

WEIGHT = int(input("Enter your weight: "))
HEIGHT = float(input("Enter your height: "))
AGE = int(input("Enter your age: "))

today = dt.now()
time = today.time()

track_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/f9159d5548706cc52f9f2cc1418403a9/myWorkouts/workouts"

track_headers = {
    "x-app-id": os.getenv("APP_ID"),
    "x-app-key": os.getenv("APP_KEY")
}

track_params = {
    "query": input("Tell about your exercise: "),
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

track_connect = requests.post(url=track_endpoint, json=track_params, headers=track_headers)
track_connect.raise_for_status()
data = track_connect.json()
print(data)

sheety_headers = {
    "Authorization": os.getenv("SHEETY_TOKEN")
}
sheet_input = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": time.strftime("%X"),
        "exercise": data["exercises"][0]["name"].title(),
        "duration": data["exercises"][0]["duration_min"],
        "calories": data["exercises"][0]["nf_calories"]
    }
}

sheety_connect = requests.post(url=sheety_endpoint, json=sheet_input, headers=sheety_headers)
sheety_connect.raise_for_status()
print(sheety_connect.text)
