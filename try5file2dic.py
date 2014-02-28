# coding: utf-8

#read random string from file
#read all strign from file
import linecache

li = []
d = {}

#For all lines
so = linecache.getlines('movies.txt')
n = 0
for j in so:
    if j == '\n':
            n=n+1
print so
print 'some n', n

##Get len() 'file'
#s = sum(1 for l in open('movies.txt', ‘r’)).
#print s
#for line in open ('s.txt', 'r').readline():
#    print line

#lines = open('s.txt','r').readlines()
#lines = open('s.txt','r').readlines()
#print lines
#n = 0
#for i in lines:
#        if(i == "\n" or i == '\r\n' ):
#                    n=n+1
#                    print 'len file string',n
#


# make loop while
# while string not blank
#     read strint to string
# dictionarty update to sql, clear dictionarydd
# do { if.. else if } while();


#For one line
do = linecache.getline('s.txt', 4)
print 'do====>', do

#This block for delete \n for another encode
kn = do.rstrip('\n')
#print '\n'
#li = kn.rstrip(':')

#li = do.split(':')
li = kn.split(':')

#This string if don't use upper block
#li = do.split(':')
print 'li====>', li

#Make dictonary form string
d.setdefault(li[0],li[1])
print 'd====>', d
