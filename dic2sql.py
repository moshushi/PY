# -*- coding: cp1251 -*-
import sqlite3

globalD={}

def make_row_dictionary():
    global globalD
    globalD = {'title' : 'Blazing Saddles', 'yearrelease' : 1974}

def ins_db_var1():
    global globalD
    conn = sqlite3.connect('filmbase.db')
    c = conn.cursor()
    c.execute('INSERT INTO films (title, yearrelease) VALUES (?,?)', [globalD["title"], globalD["yearrelease"]])
    conn.commit()
    conn.close()

def ins_db_var2():
    global globalD
    conn = sqlite3.connect('filmbase.db')
    c = conn.cursor()
    purchases = [('Casablanca', 1942),
                 ('Charade', 1953),
                 ('Cool Hand Luke', 1967),
                ]
    c.executemany('INSERT INTO films (title, yearrelease) VALUES (?,?)', purchases)
    conn.commit()
    conn.close()

def sel_db():
    conn = sqlite3.connect('filmbase.db')
    g = conn.cursor()
    for row in g.execute('SELECT * FROM films'):
        print row
    conn.commit()
    conn.close()


def del_db():
    conn = sqlite3.connect('filmbase.db')
    g = conn.cursor()

    sql = """
    DELETE FROM films
    """
    g.execute(sql)
    conn.commit()
    conn.close()

def main():
    #make_row_dictionary()
    #ins_db_var1()
    #ins_db_var2()
    del_db()
    sel_db()

if __name__ == "__main__":
    main()

