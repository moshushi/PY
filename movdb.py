# -*- coding: cp1251 -*-
"""Study task movie database film application
"""
import sqlite3

global conn

#class Movie(object):
#    def __init__(self, id, title, ryear, format, stars)

class Movie(object):
    def __init__(self, idf, title, ryear):
        self.idf = idf
        self.title = title
        self.ryear = ryear

    def save(self):
        global conn
        c = conn.cursor()
        c.execute('INSERT OR IGNORE INTO movies(title, yearrelease) VALUES (?,?)', (self.title, self.ryear,))
        conn.commit()

    def last_add(self):
        global conn
        c = conn.cursor()
        for row in c.execute('SELECT id FROM movies WHERE title = ? and yearrelease = ?', (self.title, self.ryear)):
            self.idf = row[0]
            print "Movie saved to database, id = %s" % (self.idf)

    def delete(self):
        global conn
        d = conn.execute("DELETE FROM movies WHERE id =?", (self.idf,))
        #print (self.idf)
        conn.commit()
        print "Movie with id = %s deleted from database" % (self.idf)

    def display(self):
        global conn
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('''SELECT title, yearrelease FROM movies WHERE id=?''', (self.idf,))
        for row in cursor:
            self.title = row[0]
            self.ryear = row[1]
        #    print self.title
        #    print self.ryear


class UI(object):

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
        elif UI.ch == 'delete':
            UI.del_movie(self)
        elif UI.ch == 'display':
            UI.display_movie(self)
        else:
            UI.start(self)

    def add_movie(self):
        pass
        f = Movie('None', 'None', 'None')
        f.title = raw_input("Enter movie title: ")
        f.ryear = int(raw_input("Enter release year: "))
        f.save()
        f.last_add()
        UI.user_input(self)

    def help(self):
        print ("""
Available commands:

    help            - view this help
    add             - add new movie
    import          - import movies from text file
    delete          - delete movie by id
    display         - display movie by id
    list by title   - list all movies, ordered by title
    list by year    - list all movies, ordered by year
    find by title   - list all movies, ordered by title
    find by star    - list all movies, ordered by year
    find by title   - find movies by title
    find by star    - find movies by star
    quit            - quit this program
        """)
        UI.user_input(self)

    def quit(self):
        #conn.commit()
        #conn.close()
        pass

    def del_movie(self):
        f = Movie('None', 'None', 'None')
        f.idf = raw_input("Enter delete movie id: ")
        f.delete()
        UI.user_input(self)

    def display_movie(self):
        f = Movie('None', 'None', 'None')
        f.idf = raw_input("Enter display movie id: ")
        f.display()
        if f.title == 'None':
            print "Film with id = %s not exists in database" % (f.idf)
        else:
            print "\n Film with id = %s \n Title: %s \n Year release: %s \n" % (f.idf, f.title, f.ryear)
        UI.user_input(self)


def conn_or_create_db():
#    conn = sqlite3.connect('filmbase.db')
    global conn

    c = conn.cursor()
    c.execute('PRAGMA foreign_keys = ON')
    #c.execute('''CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY, title VARCHAR(30), yearrelease INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS movies (id INTEGER, title VARCHAR(30), yearrelease INTEGER, PRIMARY KEY (id))''')
    conn.commit()

# Creates or opens a file called filmabase.db
conn = sqlite3.connect('filmbase.db')
conn_or_create_db()
a = UI()
a.start()
