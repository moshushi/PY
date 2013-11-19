# -*- coding: cp1251 -*-
globavar = 0

def in_row():
    global globalvar
    globalvar = raw_input("Enter something: ")
def out_row():
    print ("you entered ", globalvar)
def main():
    in_row()
    out_row()

if __name__ ==  "__main__":
    main()
