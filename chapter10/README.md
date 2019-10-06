# Chapter 10 - Debugging
In [Chapter 10](https://automatetheboringstuff.com/chapter10/) 

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

Q:2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).

Q:3. Write an assert statement that always triggers an AssertionError.

Q:4. What are the two lines that your program must have in order to be able to call logging.debug()?

Q:5. What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?

Q:6. What are the five logging levels?

Q:7. What line of code can you add to disable all logging messages in your program?

Q:8. Why is using logging messages better than using print() to display the same message?

Q:9. What are the differences between the Step, Over, and Out buttons in the Debug Control window?

Q:10. After you click Go in the Debug Control window, when will the debugger stop?

Q:11. What is a breakpoint?

Q:12. How do you set a breakpoint on a line of code in IDLE?

## Practice Project

### Debugging Coin Toss
