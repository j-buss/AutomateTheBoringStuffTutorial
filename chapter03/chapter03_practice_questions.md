# Chapter 3 - Practice Questions
Q:1. Why are functions advantageous to have in your programs?

They allow you to reuse code. It can be maintained in one spot.

Q:2. When does the code in a function execute: when the function is defined or when the function is called?

When it is called

Q:3. What statement creates a function?

a statement like "def functionname():"

Q:4. What is the difference between a function and a function call?

A function defines the code; a function call executes the code defined in the function

Q:5. How many global scopes are there in a Python program? How many local scopes?

There is 1 global scope. Local scopes are defined for each function. There would be as many local scopes as functions defined.

Q:6. What happens to variables in a local scope when the function call returns?

They are essentially deleted

Q:7. What is a return value? Can a return value be part of an expression?



Q:8. If a function does not have a return statement, what is the return value of a call to that function?

If there is not an explicit return value the function returns the special value: None

Q:9. How can you force a variable in a function to refer to the global variable?

It is possible to add the "global" keyword prior to the variable reference

Q:10. What is the data type of None?

A special data type that only has the value None.

Q:11. What does the import areallyourpetsnamederic statement do?

It makes the code in "areallyourpetsnamederic" file available for execution within the calling code, essentially making the ability to reuse previously defined code

Q:12. If you had a function named bacon() in a module named spam, how would you call it after importing spam?

import spam
spam.bacon()

Q:13. How can you prevent a program from crashing when it gets an error?

Add code to handle potential errors by implementing a "try/except" block.  

Q:14. What goes in the try clause? What goes in the except clause?

Practice Projects
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
