#! /usr/bin/python3
# Commandline argument is the search term; Go to Imgur and download first 10 images

import logging
from bs4 import BeautifulSoup
import requests
import webbrowser
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

def returnSoup(pageURL, headers):
    req = requests.get(pageURL, headers)
    req.raise_for_status()
    soup = BeautifulSoup(req.text, "html.parser")
    return soup

def saveSoup(soupObject, fileName):
    with open(fileName, 'w') as f:
        f.write(soupObject.prettify())

def fileToSoup(fileName):
    with open(fileName, 'r') as f:
        strFile = f.read()
    logging.debug("First 500 bytes of file: " + fileName + "\n\n--------------------\n\n" + strFile[:500])
    return BeautifulSoup(strFile, "html.parser")

def returnImgurGalleryLinks(soupObject):
    elems = soupObject.find_all("a",{"class":"image-list-link"})
    galleryLink = []
    logging.debug("Number of elements found: " + str(len(elems)))
   
    for i, link in enumerate(elems):
        tempLink = elems[i]['href']
        tempLink = 'https://imgur.com' + tempLink
        galleryLink.append(tempLink)
    
    return galleryLink

def saveImageFromGallery(urlList, headers, folder):
    for i in urlList: 
        returnSoup(i, headers)

def getImageFromGalleryPage(soupObject):
    elems = soupObject.find("div":{"class":"image post-image"})


def returnGoogleLinks(soupObject):
    elems = soupObject.find_all("div",{"class":"kCrYT"})

    logging.debug("Number of elements found: " + str(len(elems)))
    for i, link in enumerate(elems):
        try:
            subElems = elems[i].find_all("a", href=True)

            logging.debug("---------\nNumber of links found: " + str(len(subElems)))
            if len(subElems) > 0:
                for link in subElems:
                    rawLink = link['href']
                    startLink = link['href'].find('q=') + 2
                    endLink = link['href'].find('&sa=')
                    formattedLink = link['href'][startLink:endLink]
                    if formattedLink[:4] == "http":
                        print("Found link: " + formattedLink)
                        webbrowser.open(formattedLink)

            logging.debug("---------\n")
        except:
            continue

if __name__ == "__main__":
    # Get Search Keyword from commandline
    if len(sys.argv) < 2:
        print("Please enter a command line search term")

    searchTerm = ' '.join(sys.argv[1:])
    logging.debug("[Non-trivial] Commandline arg is: " + searchTerm)

    # Setup requests parameters
    baseURL = "https://imgur.com/search/score/all?q="
    url = baseURL + searchTerm
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
   
    fName = "temporary_imgur_results.txt"
    #temporarySoup = returnSoup(url, headers)
    #saveSoup(temporarySoup,fName) 
    temporarySoup = fileToSoup(fName)
    # returnGoogleLinks(returnSoup(url, headers))
    galleryList = returnImgurGalleryLinks(temporarySoup)
    for i in galleryList:

