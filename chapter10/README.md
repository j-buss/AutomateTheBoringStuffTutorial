# Chapter 10 - Debugging
In [Chapter 10](https://automatetheboringstuff.com/chapter10/) we examine the ways to diagnose issues with our code. How can we validate, test or solve errors in our code. This is accomplished with Exception handling, logging and using the debug tools appropriately.

## Summary Notes

Item|Description
----|-----------
Exception|stop running code in this function and move the program to the `except` statement
traceback|a report containing the function calls made in your code
traceback Module|a library with functions for reading the call stack and traceback
assertion|sanity check; if the assertion fails then the AssertionError exception is raised and code should fail
logging module|library which contains functions to facilitate logging

## Logging Levels
Level|Logging Function|Description
----|----|----
DEBUG|logging.debug()|lowest level; small details; usually used when diagnosing problems
INFO|logging.info()|record information on general events
WARNING|logging.warning()|indicate potential problem; doesn't prevent program from working
ERROR|logging.error()|record an error that caused the program to fail to do something
CRITICAL|logging.critical()|highest level; used to indicate fatal error that has caused or about to cause the program to stop running

### Exception as error:

```python
def testException(intInput):
    if intInput == 1:
        raise Exception('''Don't use the number: ''' + str(intInput))
    print('''Number passed to function: ''' + str(intInput))

for i in range(5):
    try:
        testException(i)
    except Exception as err:
        print('An exception happend: ' + str(err))
```

------
# Chapter 10 - Practice Questions
Q:1. Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.

##### assert spam < 10, 'Spam is greater than 10'

Q:2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).

##### assert eggs.lower() != bacon.lower(), 'Eggs and Bacon are the same...not good'

Q:3. Write an assert statement that always triggers an AssertionError.

##### assert False, 'This assertion is false'

Q:4. What are the two lines that your program must have in order to be able to call logging.debug()?

```python
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
```

Q:5. What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?

```python
import logging
logging.basicConfig(filename='myProgramLog.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname) s - %(message)s')
```

Q:6. What are the five logging levels?

Level|Logging Function|Description
----|----|----
DEBUG|logging.debug()|lowest level; small details; usually used when diagnosing problems
INFO|logging.info()|record information on general events
WARNING|logging.warning()|indicate potential problem; doesn't prevent program from working
ERROR|logging.error()|record an error that caused the program to fail to do something
CRITICAL|logging.critical()|highest level; used to indicate fatal error that has caused or about to cause the program to stop running

Q:7. What line of code can you add to disable all logging messages in your program?

##### logging.disable(logging.DEBUG)

Q:8. Why is using logging messages better than using print() to display the same message?

##### Logging is easier to remove

Q:9. What are the differences between the Step, Over, and Out buttons in the Debug Control window?

Item|Description
----|-----------
Step|Execute the next line of code; then pause
Over|Execute the next line of code; however if the next line was a function - execute at full speed; then pause for next line
Out|Execute to the end of the function; then wait (basically transforming the remaining _Step_ lines into an _Over_

Q:10. After you click Go in the Debug Control window, when will the debugger stop?

##### Cause the program to execute normally until it reaches a breakpoint or terminates

Q:11. What is a breakpoint?

##### A "stop" added to a line of code; forces execution to stop at that point

Q:12. How do you set a breakpoint on a line of code in IDLE?

##### Click in the left gutter

## Practice Project

### Debugging Coin Toss

Here is the code from the book:

```python
import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if toss == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
```

Here is my response to the code:

```python

#! /usr/bin/python3

import random
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program')

guess = ''
coinStates = ['heads','tails']

while guess not in coinStates:
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug('Guess is: ' + guess)

toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug('Toss is: ' + str(toss) + ' Value of: ' + coinStates[toss])

if coinStates[toss] == guess:
    logging.debug('toss ' + coinStates[toss] + ' == guess ' + guess + '; first if-else statement')
    print('You got it!')
else:
    logging.debug('toss <> guess; first if-else statement')
    print('Nope! Guess again!')
    guess = input()
    if coinStates[toss] == guess:
        logging.debug('toss ' + coinStates[toss] + ' == guess ' + guess + '; first if-else statement')
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

```
