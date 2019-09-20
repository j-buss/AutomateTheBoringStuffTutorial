# Chapter 4 - Lists
In [Chapter 4](https://automatetheboringstuff.com/chapter4/) Al explores 2 key data structures that are used within python that being a list and a tuple. 

## Accompanying Videos:
- [Lesson 9 - def Statements, arguments, and the None value](https://www.youtube.com/watch?v=WB4hJJkfhLU)
- [Lesson 10 - Global Scope and Local Scope](https://www.youtube.com/watch?v=M-CoVBK_bLE)
- [Lesson 11 - Error Handling](https://www.youtube.com/watch?v=qS0UkqaYmfU)
- [Lesson 12 - Writing a Guess the Number Game](https://www.youtube.com/watch?v=48WXHT0dfEY)

## Summary Notes

- list: a container type of data structure that can store multiple data; additionally the data need not be of the same type

------
# Chapter X - Practice Questions
Q:1. What is []?

###### that is an empty list

Q:2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)

```python
spam[2] = 'hello'
print(spam)
spam = [2, 4, 'hello', 8, 10]
```

For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].

Q:3. What does spam[int(int('3' * 2) // 11)] evaluate to?

###### spam[int(int('3' * 2) // 11)]
###### spam[int(int('33') // 11)]
###### spam[int(33 // 11)]
###### spam[int(3)]
###### 'd'

Q:4. What does spam[-1] evaluate to?

###### 'd'

Q:5. What does spam[:2] evaluate to?

###### ['a','b']

For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].

Q:6. What does bacon.index('cat') evaluate to?

###### 1

Q:7. What does bacon.append(99) make the list value in bacon look like?

##### [3.14, 'cat', 11, 'cat', True, 99]

Q:8. What does bacon.remove('cat') make the list value in bacon look like?

##### [3.14, 11, 'cat', True, 99]

Q:9. What are the operators for list concatenation and list replication?

###### They are the same as for strings; + for concatenation and * for replication

Q:10. What is the difference between the append() and insert() list methods?

###### append(ITEM) will place a new _ITEM_ at the end of the list; insert(ITEM, LOCATION) will put a new _ITEM_ at a certain _LOCATION_

Q:11. What are two ways to remove values from a list?

###### list_name.remove(ITEM) or list_name.pop(INDEX)
```python
>>> ham = [10, 20, 'goodbye']
>>> ham.remove(20)
>>> print(ham)
[10, 'goodbye']
>>> ham.pop(1)
'goodbye'
>>> print(ham)
[10]
```

Q:12. Name a few ways that list values are similar to string values.

###### Letters in a string can be accessed with list notation. For example to get the first two letters of a string use STRING_NAME[:2]
###### Strings and lists are able to use concatenation and multiplication operators


Q:13. What is the difference between lists and tuples?

###### Lists are mutable, meaning that the values of them and the characteristics of them (length, etc.) can be changes; but tuples are immutable, once defined they cannot be changed

Q:14. How do you type the tuple value that has just the integer value 42 in it?

###### tuple_exmple = ((42,))

Q:15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?

###### Use the function with the data type name to convert the item
###### tuple(list_example) or list(tuple_example)

Q:16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?



Q:17. What is the difference between copy.copy() and copy.deepcopy()?

Comma Code

Say you have a list value liek this:

spam = ['apples','bananas','tofu','cats']

Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it.

```python
def list_to_string(input_list):
    
```
