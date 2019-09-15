# Chapter 2 - Flow Control
Chapter 2 adds in the ability to control the execution of the program with the introduction of boolean and comparison operators, if blocks, and loops. Al finishes the chapter with the import statements which allow you to build with other's contributions.

## Accompanying Videos:
- [Lesson 4 - Flow charts, boolean values, comparison operators, boolean operators](https://www.youtube.com/watch?v=4XA9CKJJbr4)
- [Lesson 5 - if, elif, and else](https://www.youtube.com/watch?v=lWeCgEbk-Ro)
- [Lesson 6 - while Loops, break, and continue](https://www.youtube.com/watch?v=885qKiiKisI)
- [Lesson 7 - for Loops and range()](https://www.youtube.com/watch?v=HFQGxh1jY3g)
- [Lesson 8 - import Statements, sys.exit(), the pyperclip Module](https://www.youtube.com/watch?v=xJLj6fWfw6k)

## Summary Notes

**Comparison Operators**

Operator | Meaning
---------|---------
\==|Equal to
\!=|Not equal to
\<|Less than
\>|Greater than
\<=|Less than or equal to
\>=|Greater than or equal to

**Boolean Values**
- True
- False

**Boolean Operators**
- and
- or
- not

**if-elif-else**
- if statement: conditionally execute code 
- elif: executes if condition true and all previous have been false
- else: at the end; executes if all previous conditions have been false
- falsey values: 0, 0.0 and empty string '' are considered false; however better to be explicit in code

**while**
- while: a loop which executes code, when reachs end of block, back to start, re-check condition
- break: leave current cycle of loop, do not re-check condition
- condition: leave current cycle of loop, back to start, and re-check condition

**For Loop**
- for loop: block of code executed a number of times as defined in control
- [range](https://docs.python.org/3/library/functions.html#func-range): create immutable sequence of numbers; call with 1 (stop), 2 (start, stop) , or 3 (start, stop, step) arguments 

**Modules**
- Standard Library: modules that come with python
- sys.exit(): quit program
- pyperclip: 3rd-party module with copy(), paste() functions for reading/writing to clipboard

## Code

Code Name|Section|Channel|Description
---------|-------|-------|-----------
if_example.py|Flow Control Statements|Video Lesson 5|Basic if statement
if_else_example.py|Flow Control Statements|Video Lesson 5|Basic if-else statement
if_elif_example.py|Flow Control Statments|Video Lesson 5|Basic if-elif statement; without else
string_truthey_exmaple.py|Flow Control Statements|Video Lesson 5|if-else with implied "truth" from non-blank string
vampire.py|Flow Control Statements|Book|if-elif multiple elifs
vampire2.py|Flow Control Statements|Book|if-elif multiple elifs; with bug in order of elifs
littlekid.py|Flow Control Statements|Book|if-elif-else
while_example.py|While Loop Statements|Video Lesson 6|basic while loop for 5
yourName.py|While Loop Statements|Video Lesson 6|while loop until enter 'your name'
spam_while.py|While Loop Statements|Video Lesson 6|while loop with a continue
yourName2.py|While Loop Statements|Book|infinite while loop with a break when enter 'your name'
infiniteloop.py|While Loop Statements|Book|infinite loop
swordfish.py|While Loop Statements|Book|infinite loop with a break and continue
for_loop_gauss.py|For Loops and the Range() Function|Video Lesson 7|for loop to return the sum of all numbers from 1 to 100

## Other Resources
[pythontutor.com](pythontutor.com)
