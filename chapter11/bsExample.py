#! /usr/bin/python3

import logging
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

exampleFile = open("example.html")
fileString = exampleFile.read()
exampleFile.close()
logging.debug("The following is the file string: \n" + fileString)

exampleSoup = BeautifulSoup(fileString, "html.parser")
elems = exampleSoup.select('#author')
try:
    print("Element: " + str(elems[0]))
    print("Attributes: " + str(elems[0].attrs))
    #print("Attributes: " + elems[0].attrs)
    print("Author: " + elems[0].getText())
except:
    print("Error getting author name")
