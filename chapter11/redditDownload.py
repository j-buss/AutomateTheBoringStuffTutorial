#! /usr/bin/python3

# This notebook is to accompany the Automate The Boring Stuff chapter 11.  
# This code is my build of the "Practice Project" Image Site Downloader. 
# Specifically it downloads the first 8 images from a reddit subreddit

import logging
from bs4 import BeautifulSoup
import requests
import sys
import os
import shutil
from urllib.parse import urlparse

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)
def prepDirectory(directoryPath):
    directoryAbsPath = os.path.abspath(directoryPath)
    try:
        shutil.rmtree(directoryAbsPath)
    except:
        pass
    os.mkdir(directoryAbsPath)

def returnSoup(pageURL):
    req = requests.get(pageURL)
    req.raise_for_status()
    soup = BeautifulSoup(req.text, "html.parser")
    return soup

def downloadImage(folder, imageURL):
    # Clean up the imageURL
    a = urlparse(imageURL)
    parsedURL = a.path 
    fileName = os.path.basename(a.path)
    downloadURL = "https://i.redd.it/" + fileName
    logging.debug("----------------------")
    logging.debug("Raw URL: " + imageURL)
    logging.debug("URL Parsed: " + parsedURL)
    logging.debug("Filename: " + fileName)
    logging.debug("DownloadURL: " + downloadURL)
    
    # Download the content
    req = requests.get(downloadURL)
    req.raise_for_status()
    directoryAbsPath = os.path.abspath(folder)
    fileName = os.path.join(directoryAbsPath, fileName)
    with open(fileName, 'wb') as f:
        for chunk in req.iter_content(100000):
            f.write(chunk)
    logging.debug("Downloaded image: " + fileName)
    logging.debug("\n")

if __name__ == "__main__":
    
    baseURL = "http://www.reddit.com/r/itookapicture/"
    imageDirectory = 'TESTDIR_forRedditImages'
    prepDirectory(imageDirectory)
    tempSoup = returnSoup(baseURL)
    elems = tempSoup.find_all("img", {"alt":"Post image"})

    for i in elems:
        rawImageURL = i['src']
        logging.debug(rawImageURL)
    try:
        downloadImage(imageDirectory, rawImageURL)
    except:
        logging.warning("Couldn't get Image from: " + imageURL)
        pass
