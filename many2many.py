# -*- coding: cp1251 -*-
import sqlite3

global globalStars
global globalLastRowIdS

def make_db():
    conn = sqlite3.connect('filmbase.db')
    c = conn.cursor()
    c.execute('PRAGMA foreign_keys = ON')
    c.execute('''CREATE TABLE IF NOT EXISTS films (id INTEGER PRIMARY KEY, title VARCHAR(30), yearrelease INTEGER)''')
    conn.commit()
    c.execute('''CREATE TABLE IF NOT EXISTS stars (id INTEGER PRIMARY KEY, name VARCHAR(60))''')
    conn.commit()
    c.execute('''CREATE TABLE IF NOT EXISTS film_star (film_id INTEGER, star_id INTEGER, FOREIGN KEY(film_id) REFERENCES films(id), FOREIGN KEY(star_id) REFERENCES stars(id)) ''')
    conn.commit()
    conn.close()

def test_name_star():
    global globalStars
    globalStars = 'Mel Brooks'
    #Mel Brooks

def insert_name():
    global globalStars
    global globalLastRowIdS
    conn = sqlite3.connect('filmbase.db')
    c = conn.cursor()
    c.execute('INSERT OR IGNORE INTO stars(name) VALUES(?)', [globalStars])
    globalLastRowIdS = c.execute('SELECT id FROM stars WHERE name = ?', (globalStars,))
    conn.commit()
    conn.close()

def test_print_name_and_rowid():
    print globalStars
    print globalLastRowIdS

def main():
    make_db()
    test_name_star()
    insert_name()
    test_print_name_and_rowid()

if __name__ == "__main__":
    main()
