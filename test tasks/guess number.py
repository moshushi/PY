# -*- coding: utf-8 -*-
"""
Guess number in 10 try
"""

import random
global guess_number

i_try = 0
guess_number = 0
AMT_GUESS = 10

secret_number = random.randrange(1,101)

while True:
    guess_number = int(raw_input("Input guess number => "))
    i_try += 1
    if guess_number == secret_number:
        print "You Win!!! You'r score is %s" % (AMT_GUESS - i_try)
        break
        
    if i_try == AMT_GUESS:
        print 'You Lose!'
        break
    
    if guess_number > secret_number:
        print "too much"
    else:
        print "too few"
