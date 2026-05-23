import requests

def get_weather(city):

    api_key = "c1a34a5b0b21affff0f159bcf8c2e548"

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