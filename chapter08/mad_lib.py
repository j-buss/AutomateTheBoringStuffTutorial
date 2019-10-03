#! /usr/bin/python3

# mad_libs.py FILENAME, where FILENAME is a text file that contains a story with placeholders for 
#     grammatical types; example: VERB, ADJECTIVE, etc.
import sys
import re

def file_input():
    filename = input('Please enter a filename for the story: ') 
    print(filename)
    try:
        storyFile = open(filename)
        storyText = storyFile.read()
        storyFile.close()
    except:
        print('unable to open file')
        sys.exit(1)

    return storyText, filename

def mad_libs_replace(text, substring):
    # Search the story file for the values: ADJECTIVE, NOUN, ADVERB, VERB
    count = text.count(substring)
    for i in range(count):
        replace_string = input("Please enter a " + substring + ": ")
        text = text.replace(substring, replace_string, 1)
    return text


def main():
    story, filename = file_input()
    grammar_types = ['VERB','NOUN','ADJECTIVE','ADVERB']
    for item in grammar_types:
        story = mad_libs_replace(story, item)
    
    print(story)
    filename_regex = re.compile(r'''
            (\w+)       # Filename
            (\.\w{3})      # File Type
            ''' ,re.VERBOSE)
    mo = filename_regex.search(filename)
    new_filename = mo.group(1) + '_output' + mo.group(2)
    newfile = open(new_filename, 'w')
    newfile.write(story)
    newfile.close

if __name__ == "__main__":
    main()
