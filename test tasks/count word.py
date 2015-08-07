# -*- coding: utf-8 -*-
"""
program compute word with letter 'a', when 10 word - ending
"""

# count for phrase with 'a'
i = 0

while i <= 10:
    phrase = raw_input("Enter the phrase and press 'Enter'\n=>")
    if 'a' of 'A' in phrase:
        i += 1
    print "You printed %d phrase with letter 'a'" % i

print "Program end"
