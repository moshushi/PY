# -*- coding: cp1251 -*-
import sqlite3

def make_db():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
    conn.commit()
    conn.close()

#t = ('RHAT',)
#c.execute('SELECT * FROM stocks WHERE symbol=?', t)
#print c.fetchone()

def ins_db():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
#Larger example that inserts many records at time
    purchases = [('2006-03-08', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
                ]
    c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
    conn.commit()
    conn.close()

def sel_db():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        print row
    conn.commit()
    conn.close()

def main():
    make_db()
    ins_db()
    sel_db()

if __name__ == "__main__":
    main()
