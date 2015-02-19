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
    def __init__(self, title):
   # def __init__(self, id, title):
    #    self.id = id
        self.title = title

    def save(self, title):
        c.execute('INSERT OR IGNORE INTO films(title) VALUES (?)', (title))

#    def add_new(self, title):

#?add new, search?

class UI(object):
    #def __init__(self, show, add):
    def __init__(self):
        pass

    ch = ''

    def start(self):
        print ("Welcome to CMDB - Command line Movie Database.")
        print ("Type 'help' to see available commands.")
        UI.user_input(self)

    def user_input(self):
        UI.ch = raw_input("=>")
        UI.choice(self)

    def choice(self):
        if UI.ch == 'help':
            UI.help(self)
        elif UI.ch == '':
            UI.user_input(self)
        elif UI.ch == 'quit':
            UI.quit(self)
        else:
            UI.start(self)

    def add_movie(self):
        pass
        f = Movie()
        f.title = raw_input("Enter movie title:")
        #f.movie()
        #f.save()

    def help(self):
        print ("help")

    def quit(self):
        #conn.commit()
        #conn.close()
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
