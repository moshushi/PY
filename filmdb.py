import sqlite3

conn = sqlite3.connect("filmbase.db")

cursor = conn.cursor()

#create a table
cursor.execute("""CREATE TABLE films
                (id_film integer primary key, title text, release_year integer, format text, stars text)
               """)

cursor.execute("""CREATE TABLE stars
                (id_star integer primary key, firstname_star text, secondname_stars text)
               """)

cursor.execute("""CREATE TABLE films_stars
                (id_film integer, id_star integer, foreign key (id_film) REFERENCES fillm(id_film), foreign key (id_star) REFERENCES stars(id_star)
               """)

#insert some data
cursor.execute ("INSERT INTO films VALUES (0001, 'Blazing Saddles', 1974, 'VHS', 'Mel Brooks')")

#save data to database
conn.commit ()

#insert multiple records
films =[(0002, 'Role', 1982, 'VDS', 'Some'),
        (0003, 'Role 2', 1983, 'VDS', 'Some')]
cursor.executemany("INSERT INTO films VALUES(?,?)", films)
conn.commit
