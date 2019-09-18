# Chapter 3 - Functions
In [Chapter 3](https://automatetheboringstuff.com/chapter3/) Al introduces us to functions. Functions are these really cool "black boxes" of logic. Simply send some input and get some output. From a code simplicity perspective these bits of code are great. They help you keep your common code together and by encapsulating the logic it helps abstract away some of the details.

## Accompanying Videos:
- [Lesson 9 - def Statements, arguments, and the None value](https://www.youtube.com/watch?v=WB4hJJkfhLU)
- [Lesson 10 - Global Scope and Local Scope](https://www.youtube.com/watch?v=M-CoVBK_bLE)
- [Lesson 11 - Error Handling](https://www.youtube.com/watch?v=qS0UkqaYmfU)
- [Lesson 12 - Writing a Guess the Number Game](https://www.youtube.com/watch?v=48WXHT0dfEY)

## Summary Notes

- functions: essentially mini-programs created with _def_ statment, arguments, and return
- None: absence of a value; added to functions if they don't have explicit return
- argument: value passed in fucntion call
- parameter: variable inside the function
- keyword argument: argument added to a function call, but requires a keyword to identify the argumuent, generally optional
- scope: is an area of source code or "container" for variables
- global scope: is outside of all functions; cannot use any local variables from functions
- local scope: is inside a function; if there is an assignment in a function it is local
- try / except block: if an error happens in "try" block; the code in "except" block will execute; hopefully handling the error or displaying appropriate messages

------

# Chapter 3 - Practice Questions
Q:1. Why are functions advantageous to have in your programs?

###### They allow you to reuse code. It can be maintained in one spot.

Q:2. When does the code in a function execute: when the function is defined or when the function is called?

###### When it is called

Q:3. What statement creates a function?

###### a statement like "def functionname():"

Q:4. What is the difference between a function and a function call?

###### A function defines the code; a function call executes the code defined in the function

Q:5. How many global scopes are there in a Python program? How many local scopes?

###### There is 1 global scope. Local scopes are defined for each function. There would be as many local scopes as functions defined.

Q:6. What happens to variables in a local scope when the function call returns?

###### They are essentially deleted

Q:7. What is a return value? Can a return value be part of an expression?

###### a return value is the output or the result from a function; yes it can be part of a function

Q:8. If a function does not have a return statement, what is the return value of a call to that function?

###### If there is not an explicit return value the function returns the special value: None

Q:9. How can you force a variable in a function to refer to the global variable?

###### It is possible to add the "global" keyword prior to the variable reference

Q:10. What is the data type of None?

###### A special data type that only has the value None.

Q:11. What does the import areallyourpetsnamederic statement do?

###### It makes the code in "areallyourpetsnamederic" file available for execution within the calling code, essentially making the ability to reuse previously defined code

Q:12. If you had a function named bacon() in a module named spam, how would you call it after importing spam?

```python
import spam
spam.bacon()
```

Q:13. How can you prevent a program from crashing when it gets an error?

###### Add code to handle potential errors by implementing a "try/except" block.  

Q:14. What goes in the try clause? What goes in the except clause?

###### The "try" clause should contain the code which may have an error; The "except" clause is the code that should execute given the captured error

## Practice Projects
For practice, write programs to do the following tasks.

The Collatz Sequence

Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1.

Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1. (Amazingly enough, this sequence actually works for any integer—sooner or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why. Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”)

Remember to convert the return value from input() to an integer with the int() function; otherwise, it will be a string value.

Hint: An integer number is even if number % 2 == 0, and it’s odd if number % 2 == 1.

The output of this program could look something like this:


Enter number:

3

10

5

16

8

4

2

1

Input Validation

Add try and except statements to the previous project to detect whether the user types in a noninteger string. Normally, the int() function will raise a ValueError error if it is passed a noninteger string, as in int('puppy'). In the except clause, print a message to the user saying they must enter an integer.

######Collatz Function with Input Validation [included below, but also found in the collatz.py file]

```python
def collatz(number):
    integer = int(number)
    if integer % 2 == 0:
        return integer // 2
    else:
        return 3 * integer + 1

def collatz_sequence():
    while True:
        print('Please enter a positive integer:')
        try:
            result = int(input())
            if result <= 0:
                continue
            while result != 1:
                result = collatz(result)
                print(result)
            break
        except ValueError:
            pass

def main():
    collatz_sequence()

if __name__ == "__main__":
    main()
```


Input Validation
Add try and except statements to the previous project to detect whether the user types in a noninteger string. Normally, the int() function will raise a ValueError error if it is passed a noninteger string, as in int('puppy'). In the except clause, print a message to the user saying they must enter an integer.
