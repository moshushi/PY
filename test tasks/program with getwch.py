# -*- coding: utf-8 -*-
"""
Programm repeat symbol and quit, when press q 
"""

import msvcrt

current_charaster = ''

while current_charaster != u'q':
    current_charaster = msvcrt.getwch()
    print current_charaster
