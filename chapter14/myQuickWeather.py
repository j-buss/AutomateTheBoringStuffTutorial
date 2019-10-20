#! /usr/bin/python3

import json
import logging
import sys
import requests
import config_OWM
import collections
#from datetime import timedelta
import datetime
from dateutil.parser import parse

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

def printForecast(forecastJSON):
#    import datetime
    t = datetime.time(hour=12,minute=0)
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    targetDT = datetime.datetime.combine(tomorrow,t)
    logging.debug("Target Date Time for tomorrow: " + str(targetDT))
    for forecast in forecastJSON["list"]:
        logging.debug(forecast["dt_txt"])
        if targetDT == parse(forecast["dt_txt"]):
            logging.debug("Found Match")

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
    
    #logging.debug(r.url)
    #logging.debug(r.text)

    weatherData = json.loads(r.text)
    printForecast(weatherData)
