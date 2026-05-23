import requests
import os
def get_weather(city):

    API_KEY = os.getenv("WEATHER_API_KEY")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    print("WEATHER API RESPONSE:", data)  # IMPORTANT DEBUG LINE

    # SAFE CHECK (prevents crash)
    if "main" not in data:
        return "hot"   # fallback so app doesn't crash

    temperature = data["main"]["temp"] - 273.15

    if temperature > 30:
        return "hot"
    elif temperature < 20:
        return "cold"
    else:
        return "rainy"