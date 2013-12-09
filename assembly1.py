# -*- coding: cp1251 -*-
import sqlite3

def make_db():
    conn = sqlite3.connect('filmbase.db')
    c = conn.cursor()
    c.execute('PRAGMA foreign_keys = ON')
    c.execute('''CREATE TABLE IF NOT EXISTS films (id INTEGER PRIMARY KEY, title VARCHAR(30), yearrelease INTEGER)''')
    conn.commit()
    c.execute('''CREATE TABLE IF NOT EXISTS stars (id INTEGER PRIMARY KEY, name VARCHAR(60) UNIQUE)''')
    conn.commit()
    c.execute('''CREATE TABLE IF NOT EXISTS film_star (film_id INTEGER, star_id INTEGER, FOREIGN KEY(film_id) REFERENCES films(id), FOREIGN KEY(star_id) REFERENCES stars(id)) ''')
    conn.commit()
    c.execute('''CREATE TABLE IF NOT EXISTS formatm (film_id INTEGER, formats VARCHAR(8) NOT NULL CHECK (formats IN ('VHS', 'DVD', 'Blu-Ray')), FOREIGN KEY(film_id) REFERENCES films(id))''')
    conn.commit()
    conn.close()

def informat():
    tr = raw_input("Choise VHS, DVD or Blu-Ray\n")
    while tr not in ["VHS", "DVD", "Blu-Ray"]:
        tr = raw_input("Choise VHS, DVD or Blu-Ray\n")
    return tr

def test_print():
    print informat()

def main():
    #make_db()
    #informat()
    test_print()

if __name__ == "__main__":
    main()
