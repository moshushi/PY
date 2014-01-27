# -*- coding: cp1251 -*-
import sqlite3

#Make filmbase.db
def make_db():
    conn = sqlite3.connect('filmbase.db')
    c = conn.cursor()
    c.execute('PRAGMA foreign_keys = ON')
    c.execute('''CREATE TABLE IF NOT EXISTS films (id INTEGER PRIMARY KEY, title VARCHAR(30), yearrelease INTEGER)''')
    conn.commit()
    c.execute('''CREATE TABLE IF NOT EXISTS stars (id INTEGER PRIMARY KEY, name VARCHAR(60) UNIQUE)''')
    conn.commit()
    c.execute('''CREATE TABLE IF NOT EXISTS film_star (film_id INTEGER, star_id INTEGER, FOREIGN KEY(film_id) REFERENCES films(id), FOREIGN KEY(star_id) REFERENCES stars(id)) ''')
    conn.commit()
    c.execute('''CREATE TABLE IF NOT EXISTS formatm (film_id INTEGER, formats VARCHAR(8) NOT NULL CHECK (formats IN ('VHS', 'DVD', 'Blu-Ray')), FOREIGN KEY(film_id) REFERENCES films(id))''')
    conn.commit()
    conn.close()

#Hand input
def infnamerelease():
    n = raw_input("Enter title:\n")
    m = raw_input("\nEnter year release film:\n")
    return (n, m)

def informat():
    tr = raw_input("\nChoise VHS, DVD or Blu-Ray\n")
    while tr not in ["VHS", "DVD", "Blu-Ray"]:
        tr = raw_input("\nChoise VHS, DVD or Blu-Ray\n")
    return tr

def instar():
    li=[]
    while True:
        n = raw_input('\nEnter n or enter Enter to end input Stars\n')
        if n == "":
            break
        li.append(n)
    return li

#insert information in db
#for item in my_list:
#        insert_to_db(item)

def insqlnameonly():
    my_list=instar()
    conn = sqlite3.connect('filmbase.db')
    c = conn.cursor()
    for item in my_list:
        #c.execute('INSERT OR IGNORE INTO stars(name) VALUES(?)', (item,))
        c.execute('INSERT OR IGNORE INTO stars(name) VALUES(?)', [item])
        conn.commit()
    conn.close()

def insqlname():
    li2=[]
    my_list=instar()
    conn = sqlite3.connect('filmbase.db')
    c = conn.cursor()
    for item in my_list:
        c.execute('SELECT id FROM stars WHERE name = ?', (item,))
        row = c.fetchone()
        if row==None:
            c.execute('INSERT OR IGNORE INTO stars(name) VALUES(?)', (item,))
            conn.commit()
            c.execute('SELECT id FROM stars WHERE name = ?', (item,))
            row = c.fetchone()
        n = row[0]
        li2.append(n)
    conn.close()
    return li2

def insqlfilm():
    fn=infnamerelease()
    tr = informat()
    conn = sqlite3.connect('filmbase.db')
    c = conn.cursor()
    c.execute('INSERT INTO films (title, yearrelease) VALUES (?,?)', fn)
    conn.commit()
    #c.execute('SELECT id FROM films WHERE title=? AND yearrelease =?', (fn[0], fn[1],))
    c.execute('SELECT id FROM films WHERE title=? AND yearrelease =?', fn)
    row = c.fetchone()
    n = row[0]
    c.execute('INSERT OR IGNORE INTO formatm(film_id, formats) VALUES(?,?)', (n, tr))
    conn.commit()
    conn.close()
    return n

#def ins_film_star():
def add_film():
    a=insqlfilm()
    b_list=insqlname()

    conn = sqlite3.connect('filmbase.db')
    c = conn.cursor()
    for item in b_list:
        c.execute('INSERT OR IGNORE INTO film_star(film_id, star_id) VALUES(?,?)', (a, item,))
        conn.commit()
    conn.close()

def sel_film_id():
    id = raw_input("\nEnter film id :\n")
    conn = sqlite3.connect('filmbase.db')
    c = conn.cursor()
    c.execute('SELECT title, yearrelease FROM films WHERE id=?', (id,))
    fm = c.fetchone()
    #c.execute('SELECT title, yearrelease FROM film_star WHERE id=?', id)
    conn.close()
    return fm

def print_sel_film_id():
    print sel_film_id()

def del_film_id():
    id = raw_input("\nEnter film id :\n")
    conn = sqlite3.connect('filmbase.db')
    c = conn.cursor()
    c.execute('DELETE FROM films WHERE id=?', (id,))
    conn.commit()
    conn.close()

def sel_film_all():
    conn = sqlite3.connect('filmbase.db')
    c = conn.cursor()
    c.execute ('SELECT * FROM films')
    fs = c.fetchmany()
    print fs
    conn.close()


#test section
def test_sel_db():
    conn = sqlite3.connect('filmbase.db')
    c = conn.cursor()
    #c.execute('SELECT * FROM stars')
    #x = c.fetchall()
    #c.execute('SELECT * FROM films where film_id=?', t)
    #y = c.fetchall()
    #c.execute('SELECT * FROM film_star')
    #z = c.fetchall()
    conn.close()
    #return y,x
    #return z
    return y

def test_print():
    #### ins_film_star() - general input to database
    #print add_film()
    #print test_sel_db()
    #print sel_film_id()
    sel_film_all()
    #del_film_id()

def main():
    #make_db()
    #CheckStarInDB()
    test_print()

if __name__ == "__main__":
    main()
