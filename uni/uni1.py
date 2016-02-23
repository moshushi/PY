# -*- coding: utf-8 -*-
"""
Check settings in developer environment
"""

import sys
import locale

print sys.getdefaultencoding()
print sys.getfilesystemencoding()

print "----"

print locale.getpreferredencoding()
print locale.getlocale()
print locale.getdefaultlocale()

print "----"
print sys.stdout.encoding
print "----"
