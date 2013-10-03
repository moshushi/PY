# -*- coding: cp1251 -*-
import sqlite3

#function to make database for films
def make_db():
#connect database
    conn = sqlite3.connect('filmbase.db')

#open cursor
    c = conn.cursor()
#enable support foreign keys
    c.execute('PRAGMA foreign_keys = ON')

#create tables Section
    c.execute('''CREATE TABLE IF NOT EXISTS formats (id INTEGER PRIMARY KEY AUTOINCREMENT, format VARCHAR(7))''')
    conn.commit()
    c.execute('''CREATE TABLE IF NOT EXISTS films (id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR(30), yearrelease INTEGER)''')
    conn.commit()
    c.execute('''CREATE TABLE IF NOT EXISTS stars (id INTEGER PRIMARY KEY AUTOINCREMENT, firstname VARCHAR(30), secondname VARCHAR(30))''')
    conn.commit()
#many-many
    c.execute('''CREATE TABLE IF NOT EXISTS film_star (film_id INTEGER, star_id INTEGER, FOREIGN KEY (film_id) REFERENCES films(id), FOREIGN KEY (star_id) REFERENCES stars(id)) ''')
    conn.commit()
    conn.close()
#
#insert 1 some data
def inst_db():
    conn = sqlite3.connect("filmbase.db")
    b = conn.cursor()
    b.execute ("INSERT INTO films (id, title, yearrelease) VALUES (NULL, 'Blazing Saddles', 1974)")
    conn.commit()
    conn.close()
#c.execute ("INSERT INTO films VALUES (NULL, 'Blazing Saddles', 1974, 'VHS', 'Mel Brooks')")
#
#save data to database
#conn.commit ()
#
#insert multiple records
#films =[(0002, 'Role', 1982, 'VDS', 'Some'),
# (0003, 'Role 2', 1983, 'VDS', 'Some')]
#cursor.executemany("INSERT INTO films VALUES(?,?)", films)
    conn.close()
def main():
    make_db()
    inst_db()

if __name__ == "__main__":
    main()
