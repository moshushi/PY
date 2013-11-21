# -*- coding: cp1251 -*-
import sqlite3

#many-many
#    c.execute('''CREATE TABLE IF NOT EXISTS film_star (film_id INTEGER, star_id INTEGER, FOREIGN KEY (film_id) REFERENCES films(id), FOREIGN KEY (star_id) REFERENCES stars(id)) ''')

def ins_fstar_var1():
    #global globalD
    conn = sqlite3.connect('filmbase.db')
    c = conn.cursor()
    c.execute('INSERT INTO film_star (film_id, star_id) VALUES (?,?)', [globalD["film_id"], globalD["star_id"]])
    conn.commit()
    conn.close()

def sel_fstar():
    conn = sqlite3.connect('filmbase.db')
    g = conn.cursor()
    for row in g.execute('SELECT * FROM film_star'):
        print row
    conn.commit()
    conn.close()


def del_fstar():
    conn = sqlite3.connect('filmbase.db')
    g = conn.cursor()

    sql = """
    DELETE FROM film_star
    """
    g.execute(sql)
    conn.commit()
    conn.close()


def main():
    ins_fstar_var1()
    del_fstar()
    sel_fstar()

if __name__ == "__main__":
    main()

