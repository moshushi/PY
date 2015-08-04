# -*- coding: utf-8 -*-
"""
Programm repeat word, if word have 'a' - repeat 2 time, if 'z' - 3 time
"""
print "Enter the word. For end program enter 'Enter'"
loop = 1

while loop == 1:
    word = raw_input("=>")
    if word == '':
        loop = 0    
    else:
        if 'z' in word:
            word += 2 * (" " + word)
        elif 'a' in word:
            word += (" " + word)
        print word
