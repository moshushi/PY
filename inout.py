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
    global globalD
    n = raw_input("Enter title: ")
    m = raw_input("Enter year release film: ")
    globalD['title'] = n
    globalD['yearrelease'] = m

def main():
    #in_row()
    #out_row()
    #make_row_dictionary()
    add_row_dictionary_simple()
    out_row_dictionary()

if __name__ ==  "__main__":
    main()
