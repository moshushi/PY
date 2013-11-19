# -*- coding: cp1251 -*-
globavar = 0
globalD = {}
globalS = {}

def in_row():
    global globalvar
    globalvar = raw_input("Enter something: ")
def out_row():
    print ("you entered ", globalvar)
def make_row_dictionary():
    global globalD
    globalD = {'title' : 'Blazing Saddles', 'year' : 1974}
    #print globalD
def out_row_dictionary():
    print globalD
def add_row_dictionary_simple():
    global globalS
    print ("inter title")
    n = raw_input()
#    print ("inter year realese film")
#    m = raw_input()
    globalS['title'] = n
#    globalS['yearrelease'] = m
    print globalS

def main():
    #in_row()
    #out_row()
    #make_row_dictionary()
    add_row_dictionary_simple()
#    out_row_dictionary()

if __name__ ==  "__main__":
    main()
