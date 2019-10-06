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
