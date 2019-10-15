#! /usr/bin/python3
# Get all links from a page and check their status

import requests
import sys
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

def returnSoup(pageURL, headers):
    req = requests.get(pageURL, headers)
    req.raise_for_status()
    soup = BeautifulSoup(req.text, "html.parser")
    return soup

def cleanLink(rawLink):
    startLink = rawLink.find('http')
    endLink = rawLink.find('&sa=')
    formattedLink = rawLink[startLink:endLink]
    return formattedLink

def printFailedLink(url, headers):
    req = requests.get(url, headers)
    if not req.ok:
        print("Failed link: " + url)

if __name__ == "__main__":
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

    url = "https://google.com/search?q=python"
    tempSoup = returnSoup(url, headers)

    for a in tempSoup.find_all("a", href=True):
        rawLink = a['href']
        if "http" in rawLink:
            cleanedLink = cleanLink(rawLink)
            logging.debug("Found the URL: " + cleanedLink)
            try:
                printFailedLink(cleanedLink, headers)
            except:
                print("Could not verify link: " + cleanedLink)
