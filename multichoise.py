# -*- coding: cp1251 -*-
import sqlite3

global tr

def createtable_formatmovie():
    conn = sqlite3.connect('filmbase.db')
    c = conn.cursor()
    c.execute('PRAGMA foreign_keys = ON')
    c.execute('''CREATE TABLE IF NOT EXISTS formatm (film_id INTEGER, formats VARCHAR(8) NOT NULL CHECK (formats IN ('VHS', 'DVD', 'Blu-Ray')), FOREIGN KEY(film_id) REFERENCES films(id))''')
    #c.execute('''CREATE TABLE IF NOT EXISTS formatsmovie (id INTEGER PRIMARY KEY, format VARCHAR(7) XXXXXXXX)''')
    conn.commit()
    conn.close()

#def choise_formatmovie():

def informat():
    tr = raw_input("Choise VHS, DVD or Blu-Ray\n")
    while tr not in ["VHS", "DVD", "Blu-Ray"]:
        tr = raw_input("Choise VHS, DVD or Blu-Ray\n")
    print (tr)

def main():
    informat()
    createtable_formatmovie()

if __name__ == "__main__":
    main()
