import requests
from pprint import pprint
from datetime import datetime, timedelta
import pandas 
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get('OPENWEATHER_API_KEY') 

current_datetime = datetime.now()

timeNow = (f'{current_datetime.hour:02}:{current_datetime.minute:02}:{current_datetime.second:02}')
dateNow = (f'{current_datetime.day:02}/{current_datetime.month:02}/{current_datetime.year}')


city = input('Enter a city: ')
base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

if not API_KEY:
    raise ValueError("OpenWeather API key not found in environment variables")

response = requests.get(base_url)
weather_data = response.json()

def windDirection (windDeg):
    if windDeg == 0 and windDeg == 360:
        return 'N'
    elif windDeg > 0 and windDeg <= 75:
        return 'NE'
    elif windDeg > 75 and windDeg <= 150:
        return 'E'
    elif windDeg > 105 and windDeg <= 165:
        return 'SE'
    elif windDeg > 165 and windDeg <= 195:
        return 'S'
    elif windDeg > 195 and windDeg <= 255:
        return 'SW'
    elif windDeg > 255 and windDeg <= 285:
        return 'W'
    elif windDeg > 285 and windDeg < 359:
        return 'NW'
    else:
        return 'Something went wrong'
    
def getVisilibity (visibilityVal):
    if visibilityVal <= 50:
        return 'Too foogy'
    elif visibilityVal > 50 and visibilityVal <= 500:
        return 'Heavy Fog'
    elif visibilityVal > 500 and visibilityVal <= 2000:
        return 'Expect some fog'
    elif visibilityVal > 2000 and visibilityVal <= 9000:
        return 'Expect some haze'
    else:
        return 'Very clear day'
    
def getTemperature(tempVal):
    return tempVal - 273.15

def getClouds(cloudVal):
    if cloudVal == 0:
        return 'Clear sky'
    elif cloudVal > 0 and cloudVal < 25:
        return 'Mostly clear'
    elif cloudVal > 25 and cloudVal < 50:
        return 'Partly cloudy'
    elif cloudVal > 50 and cloudVal < 75:
        return 'Mostly cloudy'
    else:
        return 'Cloudy'

def getPressure(pressureVal):
    if pressureVal < 980:
        return 'Very low pressure'
    elif pressureVal >= 980 and pressureVal < 1000:
        return 'Low pressure'
    elif pressureVal >= 1000 and pressureVal < 1020:
        return 'Moderate pressure'
    elif pressureVal >= 1020 and pressureVal < 1040:
        return 'High pressure'
    elif pressureVal >= 1040:
        return 'Very high pressure'
    else:
        return 'Something went wrong'

def getHumidity(humidityVal):
    if humidityVal <= 55:
        return 'Dry'
    elif humidityVal > 55 and humidityVal <= 65:
        return 'Moisture is in the air'
    elif humidityVal > 65:
        return 'It\'s pretty humid'

def timeCity(timezone):
    timezone_hours = timezone / 3600
    current_time = datetime.now()
    local_time = current_time + timedelta(hours=timezone_hours)
    return local_time.strftime('%H:%M:%S')


if response.status_code == 200:
   weather_info = {
       'City': weather_data['name'],
       'Time of Request': timeNow,
       'Date': dateNow,
       'Time from the city searched': timeCity(weather_data['timezone']),
       'Temperature': getTemperature(weather_data['main']['temp']),
       'Feels likes': getTemperature(weather_data['main']['feels_like']),
       'Min Temperature': getTemperature(weather_data['main']['temp_min']),
       'Max Temperature': getTemperature(weather_data['main']['temp_max']),
       'Humidity': getHumidity(weather_data['main']['humidity']),
       'Pressure': getPressure(weather_data['main']['pressure']),
       'Wind': windDirection(weather_data['wind']['deg']),
       'Visibility': getVisilibity(weather_data['visibility']),
       'Clouds': getClouds(weather_data['clouds']['all'])
   }
   
   df = pandas.DataFrame([weather_info])
   
   pprint(df)
else:
    pprint(f'Something went wrong. Failed to fetch data, status code: {response.status_code}')

