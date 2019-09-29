# Chapter 7 - Pattern Matching with Regular Expressions
In [Chapter 7](https://automatetheboringstuff.com/chapter7/) 

## Accompanying Videos:
- [Lesson 23 - Regular Expressions Introduction](https://youtu.be/ruRYJiV2hI0)
- [Lesson 24 - Groups](https://youtu.be/QQVDWnnieOw)

## Summary Notes

- regular expression: specify a specific text pattern to search for
- regex: abreviation for regular expression

### Regex Review

Character Class | Meaning
----------------|---------
\\d|any digit (0-9)
\\w|any "word" (digit or letter)
\\s|any space (space, tab, newline)
\\D|any non-digit (0-9)
\\W|any non-"word" (digit or letter)
\\S|any non-space (space, tab, newline)
\*|match zero or more
\?|match zero or more
\+|match one or more
{n}|match exactly n occurences
{n,}|match n or more
{,m}|matchs 0 to m
{n,m}|matches at least n and at most m
suffix - "?"|performs a nongreedy match
^ - prefix|string must begin with
suffix - "$"|string must end with
. | matches any character except newline
[abc] | matches any character between the brackets
\[^abc] | matches any character that isn't between the brackets
re.IGNORECASE | optional second argument to "re.compile"
re.VERBOSE | optional second argument to "re.compile" to allow white space in the definition
re.DOTALL | optional second argument to "re.compile" to allow the dot character to match all including newline
search()|return a matched object
sub()|use the search to substitute strings with the matched pattern

------
## Project: Phone Number and Email Address Extractor

## Practice Questions:
Q:1. What is the function that creates Regex objects?

##### re.compile()

Q:2. Why are raw strings often used when creating Regex objects?

##### regular expressions frequently use backslashes in the pattern, so this removes the need to use multiple repeated backslashes

Q:3. What does the search() method return?

##### search returns a match object

Q:4. How do you get the actual strings that match the pattern from a Match object?

##### use the match objects group() method

Q:5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1? Group 2?

##### group 1 is the area code (first 3 numbers); group 2 is the phone number (last 7 numbers); group 0 is the entire phone number (10 digit)

Q:6. Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?

##### it would be possible to escape the parenthesis with a backslash \( or include in [(]

Q:7. The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?

##### If there are groups in the regular expression then it will return lists of tuples of strings; else it will return simply a list of strings

Q:8. What does the | character signify in regular expressions?

##### It signifies the OR command. Essentially it will return the expression before or after the pipe. It will only return the first occurrence.

Q:9. What two things does the ? character signify in regular expressions?

##### the "?" character flags the previous group as optional e.g. "bat(wo)?man" would identify both batman and batwoman

##### the second meaning is the "non-greedy" fashion; whereby with multiple possible matches it selects the shorter one

Q:10. What is the difference between the + and * characters in regular expressions?

##### the '+' character signifies that regex should match one or more of the pattern; the '\*' character signifies zero or more

Q:11. What is the difference between {3} and {3,5} in regular expressions?

##### the expression {3} signifies that the previous group should be matched 3 times; whereas the {3,5} designation signifies that the previous group should be matched within the range of 3 - 5 (i.e. 3, 4, or 5 times)

Q:12. What do the \d, \w, and \s shorthand character classes signify in regular expressions?

Character Class | Meaning
----------------|---------
\\d|any digit (0-9)
\\w|any "word" (digit or letter)
\\s|any space (space, tab, newline)
\\D|any non-digit (0-9)
\\W|any non-"word" (digit or letter)
\\S|any non-space (space, tab, newline)

Q:13. What do the \D, \W, and \S shorthand character classes signify in regular expressions?

##### see the previous question

Q:14. How do you make a regular expression case-insensitive?

##### you can add the re.IGNORECASE or re.I as the second argument of the "re.compile" statement
```python
robocop = re.compile(r'robocop', re.I)
```

Q:15. What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile()?  

##### the "." character matches any character except newline; if you include the re.DOTALL into the expression it will also include the newline character

Q:16. What is the difference between these two: .* and .*?

##### first will match in a greedy way; in which it groups as much of the text as possible; the second with the '?' will match in a non-greedy way

Q:17. What is the character class syntax to match all numbers and lowercase letters?

##### [a-z0-9]

Q:18. If numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?

##### It replaces the numbers with 'X'

```python
>>> import re
>>> numRegex = re.compile(r'\d+')
>>> numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens')
'X drummers, X pipers, five rings, X hens'
```

Q:19. What does passing re.VERBOSE as the second argument to re.compile() allow you to do?

##### ignore whitespace and comments inside the regular expression string

Q:20. How would you write a regex that matches a number with commas for every three digits? It must match the following:

'42'

'1,234'

'6,368,745'

but not the following:

'12,34,567' (which has only two digits between the commas)

'1234' (which lacks commas)

```python
import re

def findThreeDigitCommas(testString):
    threeDigitCommas = re.compile(r'^\d{1,3}(,\d{3})*$')
    mo = threeDigitCommas.search(testString)
    try:
        print('''The "three Digit Comma" number: ''' + mo.group() + ''' was found in: ''' + testString)
    except:
        print('''--------''' + testString + ''' doesn't have a "three Digit Comma" number''')

def main():
    testlist = ['42', '1,234', '1234','6,368,745','12,34,567','1234']
    for n in testlist:
        findThreeDigitCommas(n)

if __name__ == "__main__":
    main()
```

Q:21. How would you write a regex that matches the full name of someone whose last name is Nakamoto? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:

'Satoshi Nakamoto'

'Alice Nakamoto'

'Robocop Nakamoto'

but not the following:

'satoshi Nakamoto' (where the first name is not capitalized)

'Mr. Nakamoto' (where the preceding word has a nonletter character)

'Nakamoto' (which has no first name)

'Satoshi nakamoto' (where Nakamoto is not capitalized)

```python
import re

def findNakamota(testString):
    personNakamota = re.compile(r'^[A-Z][a-z]+ Nakamoto$')
    mo = personNakamota.search(testString)
    try:
        print('''A proper "Nakamota" name: ''' + mo.group() + ''' was found in: ''' + testString)
    except:
        print('''--------''' + testString + ''' doesn't have a proper "Nakamota" name''')

def main():
    testlist = ['Satoshi Nakamoto', 'Alice Nakamoto', 'Robocop Nakamoto',
            'satoshi Nakamoto','Mr. Nakamoto','Nakamoto','Satoshi nakamoto']
    for n in testlist:
        findNakamota(n)

if __name__ == "__main__":
    main()
```

Q:22. How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:

'Alice eats apples.'

'Bob pets cats.'

'Carol throws baseballs.'

'Alice throws Apples.'

'BOB EATS CATS.'

but not the following:

'Robocop eats apples.'

'ALICE THROWS FOOTBALLS.'

'Carol eats 7 cats.'

```python
import re

def aliceEatsApples(testString):
    #aliceEatsApples = re.compile(r'^(alice|bob|carol) (eats|pets|throws) (apples|cats|baseballs)$', re.IGNORECASE)
    aliceEatsApples = re.compile(r'^(alice|bob|carol) (eats|pets|throws) (apples|cats|baseballs).$', re.IGNORECASE)
    mo = aliceEatsApples.search(testString)
    try:
        print('''A proper "Alice eats apples." sentence: ''' + mo.group() + ''' was found in: ''' + testString)
    except:
        print('''--------''' + testString + ''' doesn't have a proper "Alice eats apples" sentence''')

def main():
    testlist = ['Alice eats apples.','Bob pets cats.','Carol throws baseballs.','Alice throws Apples.',
            'BOB EATS CATS.','Robocop eats apples.','ALICE THROWS FOOTBALLS.','Carol eats 7 cats.',
            'Alice chucks baseballs','Bob pets cats']
    for n in testlist:
        aliceEatsApples(n)

if __name__ == "__main__":
    main()
```

## Other Resoures

### Online Regex Testers:
[regexpal](https://www.regexpal.com/)
[pythex](https://pythex.org/)
