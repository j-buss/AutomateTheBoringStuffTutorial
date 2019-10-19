#! /usr/bin/python3

import json
import logging
import sys
import requests

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: quickWeather.py location')
        sys.exit()
    location = ' '.join(sys.argv[1:])
