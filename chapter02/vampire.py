import os
print('Running program: ' + __file__)
print('Please enter your name')
name = input()
print('Please enter your age')
age = int(input())
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('You are not Alice, kiddo')
elif age > 2000:
    print('Unlike you, Alice is not an undead, importal vampire')
elif age > 100:
    print('You are not Alice, grannie.')
