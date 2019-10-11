#! /usr/bin/python3

import sys
import webbrowser
import re

# lkupAddress contains address string for google maps; explicitly start with "empty string"
lkupAddress = ""

if len(sys.argv) > 1:
    # Loop through command line arguments; after the program name which is sys.argv[0]
    for item in sys.argv[1:]:
        item = re.sub('[\.\,]','',item)
        print(item)
        lkupAddress += item + "+"

    # Add last "/" after removing last "+"
    lkupAddress = lkupAddress[:-1] + "/"
    print(lkupAddress)
    webbrowser.open('https://www.google.com/maps/place/' + lkupAddress)
