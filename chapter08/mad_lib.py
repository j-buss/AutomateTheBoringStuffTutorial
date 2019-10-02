#! /usr/bin/python3

# mad_libs.py FILENAME, where FILENAME is a text file that contains a story with placeholders for 
#     grammatical types; example: VERB, ADJECTIVE, etc.
import sys

# TODO: Read the filename for the base story from the commandline
try:
    filename = sys.argv[1]
    storyFile = open(filename)
    storyText = storyFile.read()
except:
    print('Unable to open file')

# TODO: Default list of Grammar items
grammar_type_count = {'VERB':,'ADJECTIVE':,'NOUN':,'ADVERB':}

# TODO: Search the story file for the values: ADJECTIVE, NOUN, ADVERB, VERB


# TODO: Prompt the user to imput values for the 

# TODO: Print the story
print(storyFile.read())
