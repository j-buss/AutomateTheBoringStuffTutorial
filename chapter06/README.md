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
# Chapter 6 - Practice Questions
Q:1. QUESTION STUFF

