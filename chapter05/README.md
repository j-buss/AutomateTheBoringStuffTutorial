# Chapter 5 - Dictionaries and Structuring Data
In [Chapter 5](https://automatetheboringstuff.com/chapter5/) 

## Accompanying Videos:
- [Lesson 9 - def Statements, arguments, and the None value](https://www.youtube.com/watch?v=WB4hJJkfhLU)
- [Lesson 10 - Global Scope and Local Scope](https://www.youtube.com/watch?v=M-CoVBK_bLE)
- [Lesson 11 - Error Handling](https://www.youtube.com/watch?v=qS0UkqaYmfU)
- [Lesson 12 - Writing a Guess the Number Game](https://www.youtube.com/watch?v=48WXHT0dfEY)

## Summary Notes

- blab: blab blab blab

------
# Chapter 5 - Practice Questions
Q:1. What does the code for an empty dictionary look like?

```python
example_dict = {}
```

Q:2. What does a dictionary value with a key 'foo' and a value 42 look like?

```python
>>> dict_test = {}
>>> dict_test['foo'] = 42
>>> dict_test
{'foo':42}
```

Q:3. What is the main difference between a dictionary and a list?

###### a list generally stores individual items which are ordered; a dictionary stores unordered items which are referred to/accessed by a key

Q:4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

##### an error will result: 'KeyError'
![Dictionary KeyError](../images/dictionary_KeyError.png)

Q:5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

##### there is no difference.  first is checking to see if 'cat' is one of the values of the spam dictionary

![Dictionary Check Key and Values](../images/dictionary_check_keys_values.png)

Q:6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?

##### the first expression checks for 'cat' in the keys of spam; where as the 2nd expression checks for 'cat' in the values

Q:7. What is a shortcut for the following code?
```python
if 'color' not in spam:
    spam['color'] = 'black'

# Here is how to do it in one line...
spam.setdefault('color', 'black')
```

Q:8. What module and function can be used to “pretty print” dictionary values?

##### use the pprint library

```python
import pprint

pprint.pprint(spam)
```
### Practice Projects
For practice, write programs to do the following tasks.

### Fantasy Game Inventory
You are creating a fantasy video game. The data structure to model the player’s inventory will be a dictionary where the keys are string values describing the item in the inventory and the value is an integer value detailing how many of that item the player has. For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the player has 1 rope, 6 torches, 42 gold coins, and so on.

Write a function named displayInventory() that would take any possible “inventory” and display it like the following:


Inventory:
- 12 arrow
- 42 gold coin
- 1 rope
- 6 torch
- 1 dagger
- Total number of items: 62
Hint: You can use a for loop to loop through all the keys in a dictionary.


# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL IN THE CODE HERE
    print("Total number of items: " + str(item_total))

displayInventory(stuff)

### List to Dictionary Function for Fantasy Game Inventory
Imagine that a vanquished dragon’s loot is represented as a list of strings like this:


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

Write a function named addToInventory(inventory, addedItems), where the inventory parameter is a dictionary representing the player’s inventory (like in the previous project) and the addedItems parameter is a list like dragonLoot. The addToInventory() function should return a dictionary that represents the updated inventory. Note that the addedItems list can contain multiples of the same item. Your code could look something like this:


def addToInventory(inventory, addedItems):
    # your code goes here

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
The previous program (with your displayInventory() function from the previous project) would output the following:


Inventory:
- 45 gold coin
- 1 rope
- 1 ruby
- 1 dagger

- Total number of items: 48
