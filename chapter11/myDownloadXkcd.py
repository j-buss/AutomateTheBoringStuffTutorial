#! /usr/bin/python3
# Following the motivation of the "Automate the Boring Stuff" book by Al Sweigart. 
# This is my own code to download all the web comics from Xkcd http://xkcd.com.  
# I didn't consult Al's version until mine was working

import logging
from bs4 import BeautifulSoup
import requests
import sys
import os
import shutil

logging.basicConfig(filename='myDownloadXkcdLog.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

def prepDirectory(directoryPath):
    directoryAbsPath = os.path.abspath(directoryPath)
    try:
        shutil.rmtree(directoryAbsPath)
    except:
        pass
    os.mkdir(directoryAbsPath)

def returnXkcdImageURL(soupObject):
    """For an Xkcd page; return the link to the image"""
    comicURL = "http:" + soupObject.find("div", {"id":"comic"}).find("img")['src']
    logging.debug("ComicURL: " + comicURL)
    return comicURL

def downloadImage(folder, imageURL, headers):
    """Download and image given the specific URL"""
    req = requests.get(imageURL, headers)
    req.raise_for_status()
    fileName = os.path.split(imageURL)[1]
    directoryAbsPath = os.path.abspath(folder)
    fileName = os.path.join(directoryAbsPath, fileName)
    logging.debug("Full path: " + imageURL)
    logging.debug("Filename: " + fileName)
    with open(fileName, 'wb') as f:
        for chunk in req.iter_content(100000):
            f.write(chunk)
            logging.debug("Downloaded image: " + fileName)

def returnPrevURL(soupObject, baseURL):
    """Return the link to the previous Xkcd comic page"""
    previousLink = soupObject.find("div", {"id":"middleContainer"}).find("a",{"rel":"prev"})['href']
    fullPreviousLink = baseURL + previousLink
    logging.debug("Found previous link: " + fullPreviousLink)
    return fullPreviousLink, previousLink

def returnSoup(pageURL, headers):
    req = requests.get(pageURL, headers)
    req.raise_for_status()
    soup = BeautifulSoup(req.text, "html.parser")
    return soup

def dailyXkcd(folder, url, headers):
    """Perform the step to find the image url, download it, and return link to previous page"""
    tempSoup = returnSoup(url, headers)
    try:
        imageURL = returnXkcdImageURL(tempSoup)
        downloadImage(folder, imageURL, headers)
    except:
        logging.warning("Couldn't get Image from: " + url)
        pass
    fullPrevURL, prevURL = returnPrevURL(tempSoup, xkcdBaseURL)
    return fullPrevURL, prevURL

if __name__ == "__main__":
    xkcdBaseURL = "https://xkcd.com"
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
    imageDirectory = 'TESTDIR_forXkcdImages'
    prepDirectory(imageDirectory)
    
    # Get Xkcd information for current webpage
    fullPrevURL, prevURL = dailyXkcd(imageDirectory, xkcdBaseURL,headers)

    count = 0
    while prevURL:
        fullPrevURL, prevURL = dailyXkcd(imageDirectory, fullPrevURL, headers)
        prevURL = prevURL.strip("/")
        count += 1
        logging.debug(prevURL)
        if count % 100 == 0:
            print("Image count download: " + str(count))
            print("Latest prevURL: " + str(prevURL))
        if prevURL == str(1):
            break
