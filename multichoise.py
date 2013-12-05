# -*- coding: cp1251 -*-
import sqlite3

def make_form_db():
    conn = sqlite3.connect('filmbase.db')
    c = conn.cursor()
    #c.execute('''CREATE TABLE IF NOT EXISTS formatsmovie (id INTEGER PRIMARY KEY, format VARCHAR(7) XXXXXXXX)''')
    conn.commit()
    conn.close()

def informat():
    tr = raw_input("Choise VHS, DVD or Blu-Ray ")
    while tr not in ["VHS", "DVD", "Blu-Ray"]:
        tr = raw_input("Choise VHS, DVD or Blu-Ray")
    print (tr)

def main():
        informat()

if __name__ == "__main__":
    main()
