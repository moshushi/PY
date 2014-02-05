#read from random line

import linecache
import json

li = []
a1={}

#do = linecache.getline('s.txt', 3)
#print 'do===>', do
#kn = do.rstrip('\n')
#print 'kn===>', kn
#li = kn.split(':')
#print 'li===>', li
#print 'li[0]===>', li[0]
#a1.setdefault(str(li[0]), li[1])
#print 'a1===>', a1

#db = linecache.getline('s.txt', 3)
#fileIN = 's.txt'
fileIN = open('s.txt', 'r')
line = fileIN.readline()
db = line
print db

while line:
    line = fileIN.readline()
    db = line
    print db

kn = db.rstrip('\n')
li = kn.split(':')
a1.setdefault(str(li[0]), li[1])

print 'a1===>', a1
print a1.get('Title')
