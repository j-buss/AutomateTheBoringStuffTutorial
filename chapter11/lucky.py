#! /usr/bin/python3
# lucky.py - Opens several Google search results

import requests
import sys
import webbrowser
import bs4

print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.

# Open a browser tab for each result.
