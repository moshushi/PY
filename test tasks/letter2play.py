# -*- coding: utf-8 -*-
"""
Program play sound with frequency of ASCII number
"""

import msvcrt, winsound

current_charaster = ''
RUNNING_TIME = 400

print 'Program play sound with frequency of ASCII number.\n For Exit program press "ESC".'
while current_charaster != '\x1b':
    current_charaster = msvcrt.getwch()
    print ord(current_charaster)
    if ord(current_charaster) > 37:
        winsound.Beep(ord(current_charaster), RUNNING_TIME)
