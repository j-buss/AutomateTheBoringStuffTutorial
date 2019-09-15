# Extra credit question: investigate abs() function with using random scenarios and check the result

import random

def coinflip():
    return random.choice([-1,1])

def multiplier():
    return 10 ** random.randint(0,6)

for num in range(10):
    numbertoabsolute = random.random() * multiplier() * coinflip()
    print('abs(' + str(numbertoabsolute) + ')\t = \t',end='')
    print(str(abs(numbertoabsolute)),end='\n\n')
