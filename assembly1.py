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
    tr = raw_input("Choise VHS, DVD or Blu-Ray\n")
    while tr not in ["VHS", "DVD", "Blu-Ray"]:
        tr = raw_input("Choise VHS, DVD or Blu-Ray\n")
    return tr

def instar():
    li=[]
    while True:
        n = raw_input('\nEnter n or enter Enter to end input Stars\n')
        if n == "":
            break
        li.append(n)
    return li

def insqlname():
    my_list=instar()
    conn = sqlite3.connect('filmbase.db')
    c = conn.cursor()
    for item in my_list:
        #c.execute('INSERT OR IGNORE INTO stars(name) VALUES(?)', (item,))
        c.execute('INSERT OR IGNORE INTO stars(name) VALUES(?)', [item])
        conn.commit()
        c.execute('SELECT id FROM stars WHERE name = ?', (item,))
        x = c.fetchone()
    return x
    #    li2[]
    #    li2.append(x)
    #return li2
    conn.close()

#for item in my_list:
#        insert_to_db(item)
def CheckStarInDB():
    global globalStars
    n = 'Mell'
    conn = sqlite3.connect('filmbase.db')
    c = conn.cursor()
    c.execute ('SELECT COUNT(*) FROM stars WHERE name = ?', (n,))
    #c.execute ('select count(*) from stars')
    row = c.fetchone()
    print row[0]
    if row[0] != 1:
        globalStars = n
        insqlname()

    conn.commit()
    conn.close()

def test_sel_db():
    conn = sqlite3.connect('filmbase.db')
    c = conn.cursor()
    c.execute('SELECT * FROM stars')
    x = c.fetchall()
    return x

def test_print():
    #print informat()
    #print infnamerelease()
    #print instar()
    #print insqlname()
    CheckStarInDB()
    print test_sel_db()
    #print insqlname()

def main():
    #make_db()
    test_print()

if __name__ == "__main__":
    main()
