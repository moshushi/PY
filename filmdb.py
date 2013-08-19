import sqlite3

conn = sqlite3.connect("filmbase.db")

cursor = conn.cursor()

#create a table
cursor.execute("""CREATE TABLE films
                (id integer, title text, release_date integer, format text, stars text)
               """)
