# Chapter 7 - Pattern Matching with Regular Expressions
In [Chapter 7](https://automatetheboringstuff.com/chapter7/) 

## Accompanying Videos:
- [Lesson 23 - Regular Expressions Introduction](https://youtu.be/ruRYJiV2hI0)
- [Lesson 24 - Groups](https://youtu.be/QQVDWnnieOw)

## Summary Notes

- regular expression: specify a specific text pattern to search for
- regex: abreviation for regular expression
- 

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



Q:10. What is the difference between the + and * characters in regular expressions?

Q:11. What is the difference between {3} and {3,5} in regular expressions?

Q:12. What do the \d, \w, and \s shorthand character classes signify in regular expressions?

Q:13. What do the \D, \W, and \S shorthand character classes signify in regular expressions?

Q:14. How do you make a regular expression case-insensitive?

Q:15. What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile()?  

Q:16. What is the difference between these two: .* and .*?

Q:17. What is the character class syntax to match all numbers and lowercase letters?

Q:18. If numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?

Q:19. What does passing re.VERBOSE as the second argument to re.compile() allow you to do?

Q:20. How would you write a regex that matches a number with commas for every three digits? It must match the following:

'42'

'1,234'

'6,368,745'

but not the following:

'12,34,567' (which has only two digits between the commas)

'1234' (which lacks commas)

Q:21. How would you write a regex that matches the full name of someone whose last name is Nakamoto? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:

'Satoshi Nakamoto'

'Alice Nakamoto'

'Robocop Nakamoto'

but not the following:

'satoshi Nakamoto' (where the first name is not capitalized)

'Mr. Nakamoto' (where the preceding word has a nonletter character)

'Nakamoto' (which has no first name)

'Satoshi nakamoto' (where Nakamoto is not capitalized)

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
