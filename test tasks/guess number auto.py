# -*- coding: utf-8 -*-
"""
Guess number in 10 try
"""

import random, math
global guess_number

i_try = 0
guess_number = 0
AMT_GUESS = 10

guess_start = 0
guess_finish = 100

secret_number = random.randrange(1,101)

while True:
    guess_number = int(math.ceil((guess_finish - guess_start)/2)) + guess_start
    print 'computer choose number ', guess_number

    i_try += 1
    if guess_number == secret_number:
        print "You Win!!! You'r score is %s" % (AMT_GUESS - i_try)
        break
        
    if i_try == AMT_GUESS:
        print 'You Lose!'
        print 'The number was ', guess_number
        break
    
    if guess_number > secret_number:
        print "too much"
        guess_finish = guess_number
    else:
        print "too few"
        guess_start = guess_number
