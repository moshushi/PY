# -*- coding: utf-8 -*-
"""
Programm count letter and non-letter in input text.
"""

from __future__ import print_function
import msvcrt, string

current_charaster = ''
count_letter = 0
count_non_letter = 0



while current_charaster != 'q':
    current_charaster = msvcrt.getwch()
    print (current_charaster, sep = '', end = '')
    if current_charaster in string.ascii_letters:
        count_letter += 1
    else:
        count_non_letter += 1

pr_letter = 100 * count_letter / (count_letter + count_non_letter)
pr_nletter = 100 * count_non_letter / (count_letter + count_non_letter)

print()
print ('the percentage of letters is ', pr_letter)
print ('the percentage of non-letters is ', pr_nletter)
print ('\nDraw bar chart\n')

print (pr_letter * '#' + ' -- letters')
print (pr_nletter * '#' + ' -- not letters')
