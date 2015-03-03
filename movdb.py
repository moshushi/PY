# -*- coding: cp1251 -*-
"""Study task movie database film application
"""
import sqlite3

global conn
global myl

myl = []


class Movie(object):
    def __init__(self, idf, title, ryear, formatm, stars):
        self.idf = idf
        self.title = title
        self.ryear = ryear
        self.formatm = formatm
        self.stars = stars

    def save(self):
        global conn
        c = conn.cursor()
        c.execute('INSERT OR IGNORE INTO movies(title, yearrelease) VALUES (?,?)', (self.title, self.ryear,))
        conn.commit()
        #last_add(self)
        for row in c.execute('SELECT id FROM movies WHERE title = ? and yearrelease = ?', (self.title, self.ryear)):
            self.idf = row[0]
        c.execute('INSERT OR IGNORE INTO formatm(movie_id, formats) VALUES(?,?)', (self.idf, self.formatm))
        conn.commit()
### Insert stars from list to database
###### Will trying make it with pop.cupple, without iteration counter
        cnt = 0
        while cnt != len(self.stars):
            c.execute('INSERT OR IGNORE INTO stars(name) VALUES (?)', (self.stars[cnt],))
            conn.commit()
# Need add to another table too!!
            c.execute('SELECT id FROM stars WHERE name = ?', (self.stars[cnt],))
            for row in c:
    #            print row[0]
                c.execute ('INSERT OR IGNORE INTO movie_star(movie_id, star_id) VALUES(?,?)', (self.idf, row[0]))
                conn.commit()

#increment
            cnt += 1
        conn.commit()
        #print "Movie saved to database, id = %s" % (self.idf)

    def delete(self):
        global conn
        d = conn.execute("DELETE FROM movies WHERE id =?", (self.idf,))
        #print (self.idf)
        conn.commit()
        print "Movie with id = %s deleted from database" % (self.idf)

    def display(self):
        global conn
##        global myl
##
##        myl = []

        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('''SELECT title, yearrelease FROM movies WHERE id=?''', (self.idf,))
        for row in cursor:
            self.title = row[0]
            self.ryear = row[1]
        cursor.execute('''SELECT formats FROM formatm WHERE movie_id=?''', (self.idf,))
        for row in cursor:
            self.formatm = row[0]
        conn.text_factory = mystr
        cursor = conn.cursor()
        cursor.execute('''SELECT stars.name FROM stars INNER JOIN movie_star ON movie_star.star_id = stars.id WHERE movie_star.movie_id=?''', (self.idf,))
        self.stars = cursor.fetchall()


    def listtitle(self):

        global conn
        #conn.row_factory = sqlite3.Row
        conn.text_factory = mystr
        cursor = conn.cursor()
        cursor.execute('SELECT title, id FROM movies ORDER by title')
        all_rows = cursor.fetchall()
        return all_rows

    def listyear(self):

        global conn
        conn.text_factory = mystr
        cursor = conn.cursor()
        cursor.execute('SELECT title, yearrelease, id FROM movies ORDER by yearrelease')
        all_rows = cursor.fetchall()
        return all_rows

    def findtitle(self):
        global conn
        conn.text_factory = mystr
        cursor = conn.cursor()
        cursor.execute('SELECT title, yearrelease, id FROM movies WHERE title LIKE ? ORDER by title', ('%{}%'.format(self.title),))
        all_rows = cursor.fetchall()
        return all_rows

    def findstar(self):
        global conn
        #conn.row_factory = sqlite3.Row
        conn.text_factory = mystr
        cursor = conn.cursor()
        #cursor.execute('''SELECT movie_id FROM movie_star INNER JOIN stars ON movie_star.star_id = stars.id WHERE stars.name = ?''', (self.stars,))
        cursor.execute('''SELECT movie_id FROM movie_star INNER JOIN stars ON movie_star.star_id = stars.id WHERE stars.name LIKE ?''', ('%{}%'.format(self.stars),))
        all_rows = cursor.fetchall()
        print all_rows



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
        elif UI.ch == 'list by title':
            UI.list_by_title(self)
        elif UI.ch == 'list by year':
            UI.list_by_year(self)
        elif UI.ch == 'find by title':
            UI.find_by_title(self)
        elif UI.ch == 'find by star':
            UI.find_by_star(self)
        else:
            UI.start(self)

    def add_movie(self):
        pass
        f = Movie('None', 'None', 'None', 'None', 'None')
        #f = Movie(str(zen))
        #f = Movie()
        f.title = raw_input("Enter movie title: ")
        f.ryear = int(raw_input("Enter release year: "))
        f.formatm = choice_format()
        #li = []
        f.stars = stars_input()
        f.save()
        #f.last_add()
        print "Movie saved to database, id = %s" % (f.idf)
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
    find by title   - find movies by title
    find by star    - find movies by star
    quit            - quit this program
        """)
        UI.user_input(self)

    def quit(self):
        #conn.commit()
        conn.close()
        pass

    def del_movie(self):
        f = Movie('None', 'None', 'None', 'None', 'None')
        f.idf = raw_input("Enter delete movie id: ")
        f.delete()
        UI.user_input(self)

    def display_movie(self):
        f = Movie('None', 'None', 'None', 'None', 'None')
        #f = Movie('None', 'None', 'None')
        f.idf = raw_input("Enter display movie id: ")
        f.display()
        if f.title == 'None':
            print "Film with id = %s not exists in database" % (f.idf)
        else:
            print "\n Film with id = %s \n Title: %s \n Year release: %s\n" % (f.idf, f.title, f.ryear)
            print " with stars:"

            for i in f.stars:
                print i[0]
            print "\nformat: %s" % (f.formatm)
       ###     for i in f.stars:
       ###         print 11*''+i
        UI.user_input(self)

    def list_by_title(self):
        f = Movie('None', 'None', 'None', 'None', 'None')
        ows = f.listtitle()
        print 'List movies ordered by title with their id:'
        for i in ows:
            print i[0], '  id:', i[1]
        #list2print(ows)
        UI.user_input(self)

    def list_by_year(self):
        f = Movie('None', 'None', 'None', 'None', 'None')
        ows = f.listyear()
        print 'List movies ordered by year with their id:'
#        for i in ows:
#            print i[0], ' Year release: ', i[1],'  id:', i[2]
        list2print(ows)
        UI.user_input(self)

    def find_by_title(self):
        f = Movie('None', 'None', 'None', 'None', 'None')
        f.title = raw_input("Enter movie title: ")
        ows = f.findtitle()
        list2print(ows)
        UI.user_input(self)

    def find_by_star(self):
        f = Movie('None', 'None', 'None', 'None', 'None')
        f.stars= raw_input("Enter movie star: ")
       # ows = f.findstar()
       # list2print(ows)
       # UI.user_input(self)
        f.findstar() 


def list2print(input):
    for i in input:
        print i[0], ' Year release: ', i[1],'  id:', i[2]


def mystr(input):
    return unicode(input,'u8').encode('cp866')


def stars_input():
    global myl

    sint = None
    while sint != '':
        sint = raw_input("Star (or empty string to end):")
        myl.append(sint)
    myl.pop(-1)
    return myl

def choice_format():
    print ("""
 1> VHS
 2> DVD
 3> Blu-Ray
           """)
    fc = raw_input("Choose format: ")
    if fc == '1':
           fc = 'VHS'
    elif fc == '2':
           fc = 'DVD'
    elif fc == '3':
           fc = 'Blu-Ray'
    else:
        choice_format()
    return fc

def conn_or_create_db():
#    conn = sqlite3.connect('filmbase.db')
    global conn

    c = conn.cursor()
    c.execute('PRAGMA foreign_keys = ON')
    #c.execute('''CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY, title VARCHAR(30), yearrelease INTEGER)''')
##### Will change to executescript
    c.execute('''CREATE TABLE IF NOT EXISTS movies (id INTEGER, title VARCHAR(30), yearrelease INTEGER, PRIMARY KEY (id))''')
    conn.commit()
    c.execute('''CREATE TABLE IF NOT EXISTS stars (id INTEGER, name VARCHAR(60) UNIQUE, PRIMARY KEY(id))''')
    conn.commit()
    c.execute('''CREATE TABLE IF NOT EXISTS movie_star (movie_id INTEGER, star_id INTEGER, FOREIGN KEY(movie_id) REFERENCES movies(id), FOREIGN KEY(star_id) REFERENCES stars(id), PRIMARY KEY (movie_id, star_id)) ''')
    conn.commit()
    c.execute('''CREATE TABLE IF NOT EXISTS formatm (movie_id INTEGER, formats VARCHAR(8) NOT NULL CHECK (formats IN ('VHS', 'DVD', 'Blu-Ray')), FOREIGN KEY(movie_id) REFERENCES movies(id), PRIMARY KEY(movie_id, formats))''')
# Creates or opens a file called filmabase.db

conn = sqlite3.connect('filmbase.db')
conn_or_create_db()
a = UI()
a.start()
