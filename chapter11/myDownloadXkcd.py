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

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
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
    # directoryAbsPath = os.path.abspath(folder)
    # filename = os.path.join(directoryAbsPath, filename)
    logging.debug("Full path: " + filename)
    with open(fileName, 'wb') as f:
        for chunk in req.iter_content(100000):
            f.write(chunk)
            logging.debug("Downloaded image: " + fileName)

def returnPrevURL(soupObject, baseURL):
    """Return the link to the previous Xkcd comic page"""
    previousLink = soupObject.find("div", {"id":"middleContainer"}).find("a",{"rel":"prev"})['href']
    previousLink = baseURL + previousLink
    logging.debug("Found previous link: " + previousLink)
    return previousLink

def returnSoup(pageURL, headers):
    req = requests.get(pageURL, headers)
    req.raise_for_status()
    soup = BeautifulSoup(req.text, "html.parser")
    return soup

def dailyXkcd(folder, url, headers):
    """Perform the step to find the image url, download it, and return link to previous page"""
    tempSoup = returnSoup(url, headers)
    imageURL = returnXkcdImageURL(tempSoup)
    try:
        downloadImage(folder, imageURL, headers)
    except:
        logging.warning("Couldn't get Image from: " + imageURL)
        pass
    prevURL = returnPrevURL(tempSoup, xkcdBaseURL)
    return prevURL

if __name__ == "__main__":
    xkcdBaseURL = "https://xkcd.com"
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
    imageDirectory = 'TESTDIR_forXkcdImages'
    prepDirectory(imageDirectory)
    
    # Get Xkcd information for current webpage
    #prevURL = dailyXkcd(imageDirectory, xkcdBaseURL,headers)
    tempSoup = returnSoup('https://xkcd.com/2211/', headers)
    imageURL = returnXkcdImageURL(tempSoup)
    print(imageURL)
    downloadImage(imageDirectory, imageURL, headers)

    #count = 0
    #while count < 2:
    #    prevURL = dailyXkcd(imageDirectory, prevURL, headers)
    #    count += 1
