# -*- coding: cp1251 -*-
import sqlite3

global tr
global globalLastRowIdF
globalLastRowIdF = {}

def createtable_formatmovie():
    conn = sqlite3.connect('filmbase.db')
    c = conn.cursor()
    c.execute('PRAGMA foreign_keys = ON')
    c.execute('''CREATE TABLE IF NOT EXISTS formatm (film_id INTEGER, formats VARCHAR(8) NOT NULL CHECK (formats IN ('VHS', 'DVD', 'Blu-Ray')), FOREIGN KEY(film_id) REFERENCES films(id))''')
    #c.execute('''CREATE TABLE IF NOT EXISTS formatsmovie (id INTEGER PRIMARY KEY, format VARCHAR(7) XXXXXXXX)''')
    conn.commit()
    conn.close()

def informat():
    global tr
    tr = raw_input("Choise VHS, DVD or Blu-Ray\n")
    while tr not in ["VHS", "DVD", "Blu-Ray"]:
        tr = raw_input("Choise VHS, DVD or Blu-Ray\n")
    print (tr)

def test_lastrowidF():
    global globalLastRowIdF
    globalLastRowIdF[0] = 2

def choise_formatmovie():
    global tr
    global globalLastRowIdF
    conn = sqlite3.connect('filmbase.db')
    c = conn.cursor()
    c.execute('INSERT OR IGNORE INTO formatm(film_id, formats) VALUES(?,?)', (globalLastRowIdF[0], tr))
    conn.commit()
    conn.close()

def main():
    informat()
    createtable_formatmovie()
    test_lastrowidF()
    choise_formatmovie()

if __name__ == "__main__":
    main()
