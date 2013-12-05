# -*- coding: cp1251 -*-
import sqlite3

def insert_name():
    global globalStars
    global globalLastRowIdS
    conn = sqlite3.connect('filmbase.db')
    c = conn.cursor()
    #тут делаю двумя способами вызов
    c.execute('INSERT OR IGNORE INTO stars(name) VALUES(?)', [globalStars])
    #why don't work?
    #globalLastRowIdS = c.execute('SELECT id FROM stars WHERE name = ?', (globalStars,))
    c.execute('SELECT id FROM stars WHERE name = ?', (globalStars,))
    globalLastRowIdS = c.fetchone()
    conn.commit()
    conn.close()

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
    global globalStars
    n = 'Mell'
    conn = sqlite3.connect('filmbase.db')
    c = conn.cursor()
    c.execute ('select count(*) from stars where name = ?', (n,))
    #c.execute ('select count(*) from stars')
    row = c.fetchone()
    print row[0]
    if row[0] != 1:
        globalStars = n
        insert_name()

    conn.commit()
    conn.close()
def main():
    instar()
    CheckStarInDB()

if __name__ == "__main__":
    main()
