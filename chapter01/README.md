# Chapter 1 - Python Basics
In 
[Chapter 1](https://automatetheboringstuff.com/chapter1/)
 Al focuses on a few fundamental items that need to be addressed in any programming language. Namely data types and variables. In addition he walks through creating your first program.

## Accompanying Videos:
- [Lesson 2 - Python Programming (Automate the Boring Stuff with Python](https://www.youtube.com/watch?v=7qHMXu99d88)
- [Lesson 3 - Python Programming (Automate the Boring Stuff with Python](https://www.youtube.com/watch?v=buMTH6ICnqk)

## Summary Notes
- Expressions: values and operators; eveluate to single value
- Data Types: int, float, string
- Variables: temporary store of data for processing
- Comments in python are designated with a #; anything to the right of a hash is ignored
- execution of the program goes line by line (like reading a book)

## Practice Questions

Q1. Which of the following are operators, and which are values?
###### operator
- *
###### value
- 'hello'
###### value
- -88.8
###### operator
- -
###### operator
- /
###### operator
- +
###### value
- 5

Q:2. Which of the following is a variable, and which is a string?

###### Variable
spam 
###### string
'spam'

Q:3. Name three data types.

###### string, float, integer

Q4. What is an expression made up of? What do all expressions do?

###### expressions consist of values and operators

###### all expressions simplify to a single value

Q5. This chapter introduced assignment statements, like spam = 10. What is the difference between an expression and a statement?

###### an expression is "evaluating" a value; in a statement we are assigning a value

Q6. What does the variable bacon contain after the following code runs?

```python
bacon = 20
bacon + 1
```

###### bacon still contains 20


Q7. What should the following two expressions evaluate to?

```python
'spam' + 'spamspam'
'spam' * 3
```

###### both expressions evaluate to the same: 'spamspamspam'
Q8. Why is eggs a valid variable name while 100 is invalid?

###### a variable name cannot start with a number

Q9. What three functions can be used to get the integer, floating-point number, or string version of a value?

###### int(), float(), and str()

Q10. Why does this expression cause an error? How can you fix it?

```python
'I have eaten ' + 99 + ' burritos.'
```
###### Here is the answer, simply use the str() to convert the int to a string
```python
'I have eaten ' + str(99) + ' burritos.'
```

Extra credit: Search online for the Python documentation for the len() function. It will be on a web page titled “Built-in Functions.” Skim the list of other functions Python has, look up what the round() function does, and experiment with it in the interactive shell.

###### round(NUMBER, NUMBEROFDIGITS) rounds the NUMBER to the NUMBEROFDIGITS
