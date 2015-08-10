# -*- coding: utf-8 -*-
"""
Programm piano
"""
# a - do, s - do-dies
# asdfghjkl;'

import winsound, math, msvcrt
current_charaster = ''
RUNNING_TIME = 200

#music dictionary

piano_dic = {'a': 261.25, 's': 277.18, 'd': 293.66, 'f': 311.13, \
        'g': 329.63, 'h': 349.23, 'j': 369.99, 'k': 392.00, 'l': 415.30,\
        ';': 440.00, "'": 466.16, '\\':493.88} 

while current_charaster != 'q':
    current_charaster = msvcrt.getwch()
    for i in piano_dic.keys():
        if i == current_charaster:
            winsound.Beep(int(math.ceil(piano_dic[i])), RUNNING_TIME)

