# -*- coding: cp1251 -*-
import sqlite3
#connect database
conn = sqlite3.connect("filmbase.db")
#
#open cursor
cursor = con.cursor()
#create tables
cursor.execute('CREATE TABLE IF NOT EXISTS formats (id INTEGER PRIMARY KEY AUTOINCREMENT NO NULL, format VARCHAR(7))')
con.commit
cursor.execute('CREATE TABLE IF NOT EXISTS films (id INTEGER PRIMARY KEY AUTOINCREMENT NO NULL, title VARCHAR(30), yearrelease INTEGER)')
con.commit
cursor.execute('CREATE TABLE IF NOT EXISTS stars (id INTEGER PRIMARY KEY AUTOINCREMENT NO NULL, firstname VARCHAR(30), secondname VARCHAR(30))')
con.commit
cursor.execute('CREATE TABLE IF NOT EXISTS film_star (films_id INTEGER NOT NULL, stars_id INTEGER NOT NULL, PRIMARY KEY (film_id, star_id), CONSTRAINT film_id_fk FOREIGN KEY (film_id) REFERENCES film(id), CONSTRAINT film_id_fk FOREIGN KEY (film_id) REFERENCES film(id))')
con.commit
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
#conn.commit
