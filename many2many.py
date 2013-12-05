# -*- coding: cp1251 -*-
import sqlite3

global globalStars
global globalLastRowIdS
global globalLastRowIdF
global globalD
globalD = {}

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
    #тут делаю двумя способами вызов
    c.execute('INSERT OR IGNORE INTO stars(name) VALUES(?)', [globalStars])
    #why don't work?
    #globalLastRowIdS = c.execute('SELECT id FROM stars WHERE name = ?', (globalStars,))
    c.execute('SELECT id FROM stars WHERE name = ?', (globalStars,))
    globalLastRowIdS = c.fetchone()
    conn.commit()
    conn.close()

def test_print_name_and_rowid():
    print globalStars
    #print globalLastRowIdS
    print globalLastRowIdS[0]


#def make_row_dictionary():
#    global globalD
#    globalD = {'title' : 'Blazing Saddles', 'year' : 1974}
    #print globalD
#def out_row_dictionary():
#    print globalD
def add_row_dictionary_simple():
    global globalD
    n = raw_input("Enter title: ")
    m = raw_input("Enter year release film: ")
    globalD['title'] = n
    globalD['yearrelease'] = m

def ins_db_var1():
    global globalD
    global globalLastRowIdF

    conn = sqlite3.connect('filmbase.db')
    c = conn.cursor()
    c.execute('INSERT INTO films (title, yearrelease) VALUES (?,?)', [globalD["title"], globalD["yearrelease"]])
#    globalLastRowIdF = c.execute('SELECT id FROM films WHERE name = ?', (globalStars,))
    #globalLastRowIdF = c.lastrowid
    #c.execute('SELECT id FROM films WHERE (title, yearrelease) VALUES (?,?)', [globalD["title"], globalD["yearrelease"]])
    #c.execute('SELECT id FROM films WHERE title=?, yearrelease =?', [globalD["title"], globalD["yearrelease"]])
    c.execute('SELECT id FROM films WHERE title=? AND yearrelease =?', [globalD["title"], globalD["yearrelease"]])
    globalLastRowIdF = c.fetchone()
    print globalLastRowIdF
    conn.commit()
    conn.close()

def ins_film_star():
    global globalLastRowIdS
    global globalLastRowIdF

    conn = sqlite3.connect('filmbase.db')
    c = conn.cursor()
    #c.execute('INSERT OR IGNORE INTO film_star(film_id, star_id) VALUES(?,?)', (globalLastRowIdF, globalLastRowIdS,))
    #c.execute('INSERT OR IGNORE INTO film_star(film_id, star_id) VALUES(?,?)', ('globalLastRowIdF', 'globalLastRowIdS',))

    c.execute('INSERT OR IGNORE INTO film_star(film_id, star_id) VALUES(?,?)', (globalLastRowIdF[0], globalLastRowIdS[0],))
    print globalLastRowIdF[0]
    print globalLastRowIdS[0]

    conn.commit()
    conn.close()

def main():
    make_db()
    test_name_star()
    insert_name()
    test_print_name_and_rowid()
    add_row_dictionary_simple()
    ins_db_var1()
    ins_film_star()

if __name__ == "__main__":
    main()
