# Extra credit question: investigate round() function with using random scenarios and check the result

import random

def numofdigits():
    return random.randint(-6, 6)

def coinflip():
    return random.choice([-1,1])

def multiplier():
    return 10 ** random.randint(0,6)

for num in range(25):
    numbertoround = random.random() * multiplier() * coinflip()
    placestoround = numofdigits()
    print('round(' + str(numbertoround) + ',' + str(placestoround) + ')\t = \t',end='')
    print(str(round(numbertoround, placestoround)),end='\n\n')
