import requests

API_KEY = "129b91cca91bc699a368a1f649108d0c"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Ingrese el nombre de la ciudad: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    country = data['sys']["country"]
    weather = data['weather'][0]['description']
    temperature = round(data["main"]['temp'] - 273.15, 2)

    print("Pais:", country)
    print("Clima:", weather)
    print("Temperatura::", temperature, "°C")

else:
    print("Hubo un error en la petición")
