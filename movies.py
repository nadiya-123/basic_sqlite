from multiprocessing import connection
import sqlite3
connection = sqlite3.connect('movies.db')
cursor = connection.cursor()
comm = """CREATE TABLE IF NOT EXISTS MOVIE(MOVIE_NAME TEXT NOT NULL,
ACTOR TEXT NOT NULL,
ACTRESS TEXT NOT NULL,
RELEASE_DATE INT NOT NULL,
DIRECTOR TEXT NOT NULL)"""

cursor.execute(comm)
cursor.execute("INSERT INTO MOVIE VALUES ('KRISH', 'HRITHIK_ROSHAN', 'PREITY_ZINTA', '23-06-2006', 'RAKESH_ROSHAN')")
cursor.execute("INSERT INTO MOVIE VALUES ('BODYGUARD', 'SALMAN_KHAN', 'KAREENA_KAPOOR', '31-08-2011', 'SIDDIQUE')")

cursor.execute("SELECT * FROM MOVIE")

results= cursor.fetchall()
print(results)
print("\n")
print("to get only one particular row")
print(results[0])
print("\n")

# update 
cursor.execute("UPDATE MOVIE SET ACTRESS='PRIYANKA_CHOPRA' WHERE MOVIE_NAME='KRISH'")
cursor.execute("SELECT * FROM MOVIE")
results= cursor.fetchall()
print(results)