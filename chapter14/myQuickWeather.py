#! /usr/bin/python3

import json
import logging
import sys
import requests
import config_OWM
import collections

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: quickWeather.py location')
        sys.exit()

    apiName = sys.argv[1]
    location = ' '.join(sys.argv[2:])

    if apiName == "forecast":
        URL = "https://api.openweathermap.org/data/2.5/forecast/hourly"
    else:
        URL = "https://api.openweathermap.org/data/2.5/weather"

    logging.debug(config_OWM.api_key)
    params = collections.OrderedDict([('q',location),('APPID',config_OWM.api_key)])

    #r = requests.get(URL, params=params)

    #r = requests.get(URL, params=dict(q=location,APPID=config_OWM.api_key))
    r.raise_for_status()
    logging.debug(r.url)

    logging.debug(r.text)
