#! /usr/bin/python3

import json
import logging
import sys
import requests
import config_OWM
import collections
import datetime
from dateutil.parser import parse

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

def convertKelvinToFahrenheit(inputKelvin):
    celsius = inputKelvin - 273.15
    logging.debug(celsius)
    fahrenheit = (9/5 * celsius) + 32
    logging.debug(fahrenheit)
    return round(fahrenheit,2)

def printCurrent(currentJSON):
    print("\n----------------------")
    print("Forecast for: " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    print("\t" + currentJSON["weather"][0]["description"])
    kelvinTemp = convertKelvinToFahrenheit(currentJSON["main"]["temp"])
    logging.debug("\tTemperature (K): " + str(currentJSON["main"]["temp"]))
    print("\tTemperature (F): " + str(convertKelvinToFahrenheit(currentJSON["main"]["temp"])))
    logging.debug("\n-----------------")
    logging.debug(currentJSON)
    return None

def printForecast(forecastJSON):
    targetTime = datetime.time(hour=12,minute=0)
    targetForecasts = []
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    tomorrow2 = tomorrow + datetime.timedelta(days=1)
    targetDT = datetime.datetime.combine(tomorrow,targetTime)
    targetDT2 = datetime.datetime.combine(tomorrow2,targetTime)
    targetForecasts.append(targetDT)
    targetForecasts.append(targetDT2)

    for forecast in forecastJSON["list"]:
        if parse(forecast["dt_txt"]) in targetForecasts:
            logging.debug("Found Match: " + str(targetDT))
            logging.debug(forecast)
            print("\n----------------------")
            print("Forecast for: " + forecast["dt_txt"])
            print("\t" + forecast["weather"][0]["description"])
            kelvinTemp = forecast["main"]["temp"]
            logging.debug("\tTemperature (K): " + str(kelvinTemp))
            print("\tTemperature (F): " + str(convertKelvinToFahrenheit(kelvinTemp)))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: quickWeather.py apiName zipCode')
        sys.exit()

    apiName = sys.argv[1]
    zipCode = sys.argv[2]

    if apiName == "forecast":
        URL = "https://api.openweathermap.org/data/2.5/forecast"
    else:
        URL = "https://api.openweathermap.org/data/2.5/weather"

    logging.debug(config_OWM.api_key)
    params = collections.OrderedDict([('zip',zipCode),('APPID',config_OWM.api_key)])

    r = requests.get(URL, params=params)
    r.raise_for_status()
    
    weatherData = json.loads(r.text)
    if apiName == "forecast":
        printForecast(weatherData)
    else:
        printCurrent(weatherData)
