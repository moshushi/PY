# -*- coding: cp1251 -*-
import sqlite3
"""Study task movie database film application
"""


#class Movie(object):
#    def __init__(self, id, title, ryear, format, stars)
#
#def funct():
#    pass

class Movie(object):
    #def __init__(self, id, title):
    def __init__(self):
        pass

class UI(object):
    #def __init__(self, show, add):
    def __init__(self):
        pass

    def start(self):
        pass


def conn_or_create_db():
    conn = sqlite3.connect('filmbase.db')

    c = conn.cursor()
    c.execute('PRAGMA foreign_keys = ON')
    c.execute('''CREATE TABLE IF NOT EXISTS films (id INTEGER PRIMARY KEY, title VARCHAR(30), yearrelease INTEGER)''')
    conn.commit()

conn_or_create_db()
a = UI()
a.start()

