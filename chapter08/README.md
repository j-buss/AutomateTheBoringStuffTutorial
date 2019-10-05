# Chapter 8 - Reading and Writing Files
In [Chapter 8](https://automatetheboringstuff.com/chapter8/) we work with files: Reading, Writing and overall navigation of the folder structure.

## Summary Notes

Item|Description
----|-----------
os.path.join('usr','bin')|function to create path for folder/file based on os conventions ('\\' vs. '/')
os.path.sep|returns the path separator for the system based on OS convention
os.getcwd()|return the current working directory
os.chdir(_path_)|change the directory to _path_
os.makedirs(_path_)|make directory
os.path.abspath(_path_)|return string of absolute path of _path_
os.path.isabs(_path_)|return True if argument is an absolute path, False if argument is relative
os.path.relpath(_path_, _start_)|return string of relative path from _start_ to _path_
os.path.basename(_path_)|return the basename of the _path_ argument
os.path.dirname(_path_)|return the directory name of the _path_ argument
os.path.split(_path_)|return a tupe of directory name and basename of the _path_ argumenti
os.path.getsize(_path_)|return size in bytes
os.path.listdir(_path_)|return list of filename strings
os.path.exists(_path_)|return True if file or folder exists 
os.path.isfile(_path_)|return True if exists and is a file
os.path.isdir(_path_)|return True if exists and is a directory
open(_path_,_mode_)|open the file passed as _path_ argument in the _mode_ (default is r=read mode, w=write plaintext, a=append) and returns a File Object
read(_path_)|return a string value of the content of the file passed as argument
readlines(_path_)|return a list of string values from the file, one string for each line of text
write(_path_)|write to the file object passed as read the file passed as argument
close(_path_)|close the file object passed as argument
shelve library|a simple persistent storage option for Python objects when a relational db is overkill; the shelf is accessed by keys, just as with a dictionary 
shelve.open(_file_)|open a shelve object
pprint.pformat(_obj_)|return pretty print contents of text as string; could store in file to load as module

------
# Chapter 8 - Practice Questions
Q:1. What is a relative path relative to?

##### A relative path is relative to the current working directory

Q:2. What does an absolute path start with?

##### An absolute path starts with the drive (e.g. "C:", "D:" on windows and "/" on linux)

Q:3. What do the os.getcwd() and os.chdir() functions do?

##### the os.getcwd() function will return a string with the absolute path of the current working directory; the os.chdir(_path_) function will change the current working directory to the _path_ variable that is passed as an argument

Q:4. What are the . and .. folders?

##### the dot (.) and the dot-dot (..) folders are not real folders but special names that can be used in the path for (.) "this directory" and (..) "parent directory"

Q:5. In C:\bacon\eggs\spam.txt, which part is the dir name, and which part is the base name?

##### the basename is the file or "spam.txt" and the dir name is everything before that; namely "C:\bacon\eggs"

Q:6. What are the three “mode” arguments that can be passed to the open() function?

##### read mode (r), write mode (w) and append mode (a)

Q:7. What happens if an existing file is opened in write mode?

##### it will overwrite the file and start it from scratch

Q:8. What is the difference between the read() and readlines() methods?

##### the read() method will load all of the content into one string; but readlines() will load each line of the file into a list object

Q:9. What data structure does a shelf value resemble?

##### a relational database

------
## Project: Generating Random Quiz Files

```python
#! /usr/bin/python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in random order, along with the answer key

import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
           'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
           'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
           'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
           'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
           'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
           'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
           'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
           'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
           'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
           'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
           'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
           'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
           'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
           'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
           'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':
           'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files
for quizNum in range(35):
    # Create the quiz and answer key files.
    quizFile = open('randomQuizGenerator/capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('randomQuizGenerator/capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    # Loop through all 50 states, making a question for each.
    for questionNum in range(50):

        # Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Write the question and answer options to the quiz file.
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # Write the answer key to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
```

## Project: Multiclipboard

```python
#! /usr/bin/python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
```

## Practice Projects: Extending the Multiclipboard
```python
#! /usr/bin/python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb_2')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
```

## Practice Projects: Mad Libs
```python
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
```

## Practice Projects: Regex Search

Write a program that opens all .txt. files in a folder and searche for any line that matches a user-supplied regular expression. The results should be printed to the screen.

```python
import re
import os

def main():
    folderpath = input('Enter the folder path: ')
    search_string = input('Enter the string to search for: ')
    
    # ensure path is absolute
    folderpath = os.path.abspath(folderpath)

    for filename in os.listdir(folderpath):
        if filename[-4:] == '.txt':
            absolute_filename = os.path.join(folderpath, filename)
            with open(absolute_filename, "r") as f:
                found_lines = []
                fileHasLine = False
                for line in f:
                    if search_string in line:
                        fileHasLine = True
                        found_lines.append(line)
                if fileHasLine == True:
                    print(absolute_filename)
                    for x in range(len(found_lines)):
                        print(found_lines[x])

if __name__ == "__main__":
    main()
```

