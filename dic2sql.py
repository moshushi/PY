# -*- coding: cp1251 -*-
import sqlite3

globalD={}

def make_row_dictionary():
    global globalD
    globalD = {'title' : 'Blazing Saddles', 'year' : 1974}

def ins_db():
    global globalD
    conn = sqlite3.connect('filmbase.db')
    c = conn.cursor()
    c.executemany('INSERT INTO films (title, yearrelease) VALUES (?,?) globalD')
    conn.commit()
    conn.close()

def main():
    make_row_dictionary()
    ins_db()
    sel_db()

if __name__ == "__main__":
    main()

