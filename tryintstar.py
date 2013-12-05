# -*- coding: cp1251 -*-
import sqlite3

def instar():
    li=[]
    while True:
        n = raw_input('Enter n or enter Enter to quit')
#        if not n:
        if n == "":
            break
        li.append(n)
        print li
    print ('Loop end')

def CheckStarInDB():
    #n = Mell
    conn = sqlite3.connect('filmbase.db')
    c = conn.cursor()
    #c.execute ('select count(*) from stars where name = n')
    c.execute ('select count(*) from stars')
    row = c.fetchone()
        #count = row[0]
            #if not count:
               #sql insert in table
    print row
        #print count

    conn.commit()
    conn.close()
def main():
    instar()
    CheckStarInDB()

if __name__ == "__main__":
    main()
