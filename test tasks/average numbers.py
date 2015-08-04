# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
program for compute average entered numbers
"""

l = []

def input_number():
    # input number's function 
    x = raw_input("Enter number or word 'ok'\n>")
    return x

def average_list(ls):
    # compute average list's members and output results

    if len(ls) == 0:
        return  None 
    else:
    
        # we can use reduce(lambda x,y: x + y, l)/ float(len(l)),
        # but sum(l)/float(len(l)) more simple
        return sum(ls)/float(len(ls))

def assembly_list(x):
    # assembly to list only numbers
    out_list = ['ok', 'OK']

    if x in out_list:
        pass
    elif x.isdigit():
        l.append(int(x))
        assembly_list(input_number())
    else:
        assembly_list(input_number())

def outp(x):
    # function print compute result's
    if isinstance(x, float):
        print "Result is ... %s" % x
    else:
        print "You didn't enter any number"



def main():
    print "This program compute's average entered numbers"
    assembly_list(input_number())
    outp(average_list(l))


if __name__ == "__main__":
    main()
