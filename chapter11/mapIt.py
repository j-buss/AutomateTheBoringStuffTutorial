#! /usr/bin/python3

import sys
import webbrowser
import re
import logging
import pyperclip

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

# lkupAddress contains address string for google maps; explicitly start with "empty string"
lkupAddress = ""

if len(sys.argv) > 1:
    logging.debug('Command line arguments given')
    # Loop through command line arguments; after the program name which is sys.argv[0]
    for i, argument in enumerate(sys.argv[1:],1):
        argument = re.sub('[\.\,]','',argument)
        logging.debug('Command line argument number: ' + str(i) + ' value: ' + argument)
        lkupAddress += argument + "+"

    # Add last "/" after removing last "+"
    lkupAddress = lkupAddress[:-1] + "/"
else:
    logging.debug('No command line arguments given. Using clipboard.')
    lkupAddress = pyperclip.paste()

logging.debug('Using the following address for lookup: ' + lkupAddress)
webbrowser.open('https://www.google.com/maps/place/' + lkupAddress)
