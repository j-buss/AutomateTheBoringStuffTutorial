# Chapter 6 - DESCRIPTION
In [Chapter 6](https://automatetheboringstuff.com/chapter6/) we learn about manipulating strings.

## Accompanying Videos:
- [Lesson 19 - Raw Strings and Multiline Strings](https://youtu.be/0gybjpkN-UY)
- [Lesson 20 - String Methods and the pyperclip Module](https://youtu.be/rODBsj5DfQ0)

## Summary Notes

- string values: defined by either single ' or double quote "
- escape character: backslash (\\) when used in a string it will allow the next character to be "normal" rather than special
- raw string: completely ignores all escape characters and prints any backslash that appears in the string; ex: `print(r'raw \string')`
- multiline string: three single or three double quotes designate all the formatting as part of the string, (e.g. new lines, tabs); many times used for multiline comments
- membership: use _in_ and _not in_ to determine if a string contains another string
- string methods: upper(), lower(), islower(), isupper()
- isX string methods: isalpha(), isalnum(), isdecimal(), isspace(), istitle()
- membership beginning or end: string.startswith(SEARCHSTRING), string.endswith(SEARCHSTRING)
- string.join(LIST): join all the items in the list, with the _string_ as the "glue" between the items
- string.split(optional splitstring): will take the _string_ and split it on each occurrence of the _splitstring_
- padding a string: string.rjust(num, pad_string), ljust(), center()
- remove whitespace: strip(), rstrip() and lstrip()
- pyperclip: external library which has copy and paste functions to access the computers clipboard

------
## Project: Password Locker
```python
#! python3
# pw.py - An insecure password locker program.
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
```

## Project: Adding Bullets to Wiki Markup
```python
#! /usr/bin/python3
import pyperclip

text = pyperclip.paste()
lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i] 

text = '\n'.join(lines)
pyperclip.copy(text)
```

## Chapter 6 - Practice Questions
Q:1. What are escape characters?

##### lets you use characters that are otherwise impossible to put into a string.It consists of a backslash followed by another character

Q:2. What do the \n and \t escape characters represent?

##### \\n = newline; \\t = tab

Q:3. How can you put a \ backslash character in a string?

##### put a backslash in front of it; \\\\

Q:4. The string value "Howl's Moving Castle" is a valid string. Why isn’t it a problem that the single quote character in the word Howl's isn’t escaped?

##### the single quote is included within double quotes; therefore the single quote is not interpreted as a string terminator

Q:5. If you don’t want to put \n in your string, how can you write a string with newlines in it?

##### you can designate the string as "raw" by including a "r" prefix

Q:6. What do the following expressions evaluate to?

'Hello world!'[1]
##### "e"

'Hello world!'[0:5]
##### "Hello"

'Hello world!'[:5]
##### "Hello"

'Hello world!'[3:]
##### "lo world!"

Q:7. What do the following expressions evaluate to?

'Hello'.upper()
##### "HELLO"

'Hello'.upper().isupper()
##### True

'Hello'.upper().lower()
##### "hello"

Q:8. What do the following expressions evaluate to?

'Remember, remember, the fifth of November.'.split()

##### ['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']

'-'.join('There can be only one.'.split())

##### 'There-can-be-only-one.'

Q:9. What string methods can you use to right-justify, left-justify, and center a string?

##### rjust(), ljust() and center() 
```python
>>> 'example'.rjust(20, '*')
'*************example'
```

Q:10. How can you trim whitespace characters from the beginning or end of a string?

##### strip(), rstrip(), lstrip()
```python
>>> '     extra space     '.rstrip()
'     extra space'
```

## Practice Project

### Table Printer
```python
tableData = [['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs','cats','moose','goose']]

def printTable(listoflists):
    numberoflists = len(listoflists)
    numberofitems = len(listoflists[0]) # assuming that all inner lists are the same size
    maxoflists = []
    for innerlist in listoflists:
        maxlen = len(max(innerlist, key=len))
        maxoflists.append(maxlen)
    for i in range(numberofitems): # of items
        for j in range(numberoflists): # of lists
            print(listoflists[j][i].rjust(maxoflists[j]),' ',end='',sep='')
        print()

def main():
    printTable(tableData)

if __name__ == "__main__":
    main()
```

## Extras

I did receive some error messages when trying to access the pyperclip library on my chromebook.

It appears that there is a package that needs to be loaded: ![XSel](https://packages.debian.org/stretch/xsel). Which is a command line program for getting and setting the contents of the X selection. Here is a link which describes a similar situation of loading in the XSel package to access the X selection.

![Pyperclip could not find a copy/paste mechanism for your system.](https://catinsunshine.blogspot.com/2017/04/solved-pyperclip-could-not-find.html)
