import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENWEATHER_API_KEY')


def get_coordinates_data():
    location = input('enter the location name:>> ').capitalize()
    country = input('''enter country code, eg; ng,us,uk
	>>> ''').upper()

    url = f'http://api.openweathermap.org/geo/1.0/direct?q={location},{country}&Limit=10&appid={api_key}'

    try:
        response = requests.get(url)
        response.raise_for_status()

        return(response.text)
    except requests.exceptions.RequestException as e:
        print(f'sorry an error occured, {e}')
        return None


located = get_coordinates_data()


def extract_coordinates(data):
    res = json.loads(data)
    for place in res:
        lat = place.get('lat', 0)
        lon = place.get('lon', 0)

    return lat, lon


lat_lon = extract_coordinates(located)
# print(lat_lon)


def get_weather_data(lat_lon):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_lon[0]}&lon={lat_lon[1]}&appid={api_key}'
    try:
        response = requests.get(url)
        response.raise_for_status()

        res = json.loads(response.text)
        return res
    except requests.exceptions.RequestException as e:
        print(f'soory an error occured, {e}')
        return None


weather = get_weather_data(lat_lon)


temperature_in_kevin = weather['main'].get('temp', 0)
pressure = weather['main'].get('pressure', 0)
humidity = weather['main'].get('humidity', 0)
name = weather['name']
country = weather['sys'].get('country', 'Unknown')
temp_in_celsius = int(temperature_in_kevin) - 273


print(f'The temperature of {name}, {country}, is {temp_in_celsius} ℃, the humidity is {humidity} and pressure is {pressure}')
