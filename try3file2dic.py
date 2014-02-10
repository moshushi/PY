# coding: utf-8

#read random string from file
import linecache

li = []

#For all lines
#do = linecache.getlines('s.txt')

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
