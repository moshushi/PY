# -*- coding: cp1251 -*-
"""Study task movie database film application
"""
import sqlite3

global conn

#class Movie(object):
#    def __init__(self, id, title, ryear, format, stars)
#
#def funct():
#    pass

class Movie(object):
    def __init__(self, idf, title, ryear):
        self.idf = idf
        self.title = title
        self.ryear = ryear

    #def save(self, title):
    def save(self):
        global conn
        c = conn.cursor()
        c.execute('INSERT OR IGNORE INTO films(title, yearrelease) VALUES (?,?)', (self.title, self.ryear,))
        conn.commit()
#    def add_new(self, title):

    def last_add(self):
        global conn
        c = conn.cursor()
        for row in c.execute('SELECT id FROM films WHERE title = ? and yearrelease = ?', (self.title, self.ryear)):
            self.idf = row[0]
            print "Movie saved to database, id = %s" % (self.idf)

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
        elif UI.ch == 'add':
            UI.add_movie(self)
        else:
            UI.start(self)

    def add_movie(self):
        pass
        f = Movie('None', 'None', 'None')
        f.title = raw_input("Enter movie title: ")
        f.ryear = int(raw_input("Enter release year: "))
        #f.movie()
        #print f.title
        f.save()
        f.last_add()
        UI.user_input(self)

    def help(self):
        print ("help")
        UI.user_input(self)

    def quit(self):
        #conn.commit()
        #conn.close()
        pass

def conn_or_create_db():
#    conn = sqlite3.connect('filmbase.db')
    global conn

    c = conn.cursor()
    c.execute('PRAGMA foreign_keys = ON')
    c.execute('''CREATE TABLE IF NOT EXISTS films (id INTEGER PRIMARY KEY, title VARCHAR(30), yearrelease INTEGER)''')
    conn.commit()


conn = sqlite3.connect('filmbase.db')
conn_or_create_db()
a = UI()
a.start()
#a.add_movie()
