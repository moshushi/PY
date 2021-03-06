# -*- coding: utf-8 -*-
"""
Programm play chizhyk pyzhyk on piano
"""
# a - do, s - do-dies
# asdfghjkl;'

import winsound, math, msvcrt, time
current_charaster = ''
RUNNING_TIME = 200

#music dictionary

piano_dic = {'a': 261.25, 's': 277.18, 'd': 293.66, 'f': 311.13, \
        'g': 329.63, 'h': 349.23, 'j': 369.99, 'k': 392.00, 'l': 415.30,\
        ';': 440.00, "'": 466.16, '\\':493.88} 

# ми-до-ми-до-фа-ми-ре-соль-соль-соль-ля-си-до-до-до
music_tuple = ('g','a','g','a','h','g','d','j','pause','j','pause','j',';',\
        '\\','a','a','a')

for note in music_tuple:
    if note != 'pause':
        for note in piano_dic.keys():
            winsound.Beep(int(math.ceil(piano_dic[note])), RUNNING_TIME)
    else:
        time.sleep(0.5)
