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
    def __init__(self, id, title):
    #def __init__(self):
    #    pass
        self.id = id
        self.title = title

    def save(self):
        pass
#?add new, search?

class UI(object):
    #def __init__(self, show, add):
    def __init__(self):
        pass

    def start(self):
   #     pass
        print ("Welcome to CMDB - Command line Movie Database.")
        print ("Type 'help' to see available commands.")

    def add_movie(self):
        pass
        #f.movie()
        #f.save()

    def help(self):
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
#a.add_movie()
