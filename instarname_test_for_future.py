# -*- coding: cp1251 -*-
import sqlite3

globalStars={}
global globalRowId

def make_db():
    conn = sqlite3.connect('filmbase.db')
    c = conn.cursor()
    c.execute('PRAGMA foreign_keys = ON')
    c.execute('''CREATE TABLE IF NOT EXISTS films (id INTEGER PRIMARY KEY, title VARCHAR(30), yearrelease INTEGER)''')
    conn.commit()
    c.execute('''CREATE TABLE IF NOT EXISTS stars (id INTEGER PRIMARY KEY, firstname VARCHAR(30), secondname VARCHAR(30))''')
    conn.commit()
    c.execute('''CREATE TABLE IF NOT EXISTS film_star (film_id INTEGER, star_id INTEGER, FOREIGN KEY(film_id) REFERENCES films(id), FOREIGN KEY(star_id) REFERENCES stars(id)) ''')
    conn.commit()
    conn.close()

def test_name_star_dictionary():
    global globalStars
    globalStars = {'firstname' : 'Mel', 'secondname' : 'Brooks'}
    #Mel Brooks

def print_globalStars():
    print globalStars

#def insert_name():
#exist = cursor.fetchone()
#if exist is None:
#  #not exists
#else:
#  #exists
#    global globalStars
#    conn = sqlite3.connect('filmbase.db')
#    c = conn.cursor()
#    c.execute('INSERT OR IGNORE INTO stars(firstname, secondname) VALUES(?,?)',['globalStars["firstname"], globalStars["secondname"]])
#    last_row_id = c.execute('SELECT id FROM stars WHERE firstname = ?, secondname = ?', ['globalStars["firstname"], globalStars["secondname"]])
#    conn.commit()
#    conn.close()
def main():
#    make_db()
    test_name_star_dictionary()
    print_globalStars()

if __name__ == "__main__":
    main()
