#! /usr/bin/python3
# Commandline argument is the search term; Google search the term; Open top N links in new tabs

import logging
from bs4 import BeautifulSoup
import requests
import webbrowser
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

# Get Search Keyword from commandline
if len(sys.argv) < 2:
    print("Please enter a command line search term")

searchTerm = ' '.join(sys.argv[1:])
logging.debug("[Non-trivial] Commandline arg is: " + searchTerm)

# Retrieve search results
res = requests.get("http://google.com/search?q=" + searchTerm)
res.raise_for_status()
resultString = res.text

# Open Broaswer Tab for each result
logging.debug("Request returned the following [first 1000 bytes]: " + resultString[:1000])  
soup = BeautifulSoup(resultString, "html.parser")
#elems = soup.find_all('a', href=True)
elems = soup.select('.r a')

# <div id="main">
# <div id="cnt">
# <div class="mw">
# <div class=rcnt">
# <div class="col">
# <div id="center_col">
# <div id="search">
# <div class="rc">
# <div class="r">
# <a href="...">

logging.debug("Number of elements found: " + str(len(elems)))
for i, link in enumerate(elems):
    logging.debug("Link found: " + str(elems[i]))
