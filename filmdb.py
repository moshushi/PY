# -*- coding: cp1251 -*-
import sqlite3
#connect database
conn = sqlite3.connect("filmbase.db")
#
#open cursor
c = conn.cursor()
#enable support foreign keys
c.execute('PRAGMA foreign_keys = ON')
#
#create tables Section
c.execute('''CREATE TABLE IF NOT EXISTS formats (id INTEGER PRIMARY KEY AUTOINCREMENT, format VARCHAR(7))''')
conn.commit()
c.execute('''CREATE TABLE IF NOT EXISTS films (id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR(30), yearrelease INTEGER)''')
conn.commit()
c.execute('''CREATE TABLE IF NOT EXISTS stars (id INTEGER PRIMARY KEY AUTOINCREMENT, firstname VARCHAR(30), secondname VARCHAR(30))''')
conn.commit()
#c.execute('''CREATE TABLE film_star (films_id INTEGER NOT NULL, stars_id INTEGER NOT NULL, PRIMARY KEY (film_id, star_id), CONSTRAINT film_id_fk FOREIGN KEY (film_id) REFERENCES film(id), CONSTRAINT film_id_fk FOREIGN KEY (film_id) REFERENCES film(id))''')
#conn.commit()
#
#insert some data
#cursor.execute ("INSERT INTO films VALUES (0001, 'Blazing Saddles', 1974, 'VHS', 'Mel Brooks')")
#
#save data to database
#conn.commit ()
#
#insert multiple records
#films =[(0002, 'Role', 1982, 'VDS', 'Some'),
#        (0003, 'Role 2', 1983, 'VDS', 'Some')]
#cursor.executemany("INSERT INTO films VALUES(?,?)", films)
conn.close()
