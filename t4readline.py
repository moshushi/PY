# coding: utf-8

#lines = open('movies.txt','r').readline():
#    print lines

#f = open('movies.txt', 'r')
#s = f.readlines()
#print 's===>', s
#
#allRows = []
#with open ('movies.txt', 'r') as f:
#    for row in f:
#        allRows.append(row)
#print allRows

with open('movies.txt', 'r') as f:
    myList = list(f)
print myList
