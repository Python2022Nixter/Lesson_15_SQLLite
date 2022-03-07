import os
import pathlib
import sqlite3

DB_FILE = "python_test_db1.db"
PATH_TO_FILE = pathlib.Path(__file__).parent.joinpath(DB_FILE)

con = None
con = sqlite3.connect(PATH_TO_FILE) 

sql_query = """
CREATE TABLE if NOT  EXISTS "test"(
	"id"  INTEGER NOT NULL,
	"name"  TEXT,
	"email"  INTEGER,
	PRIMARY KEY  ("id"  AUTOINCREMENT) 
);
INSERT INTO test(name, email) VALUES("Oleg", 20);
INSERT INTO test(name, email) VALUES("Max", 16);
"""

sql_insert = """
INSERT INTO test(name, email) VALUES("Nixter", 44);
"""
cursor = con.cursor()
con.execute(sql_insert)

for i in range(10):
    sql_query += F"""
    INSERT INTO test(name, email) VALUES("Jhon{i}", 12{i});
"""
con.executescript(sql_query)
con.execute(sql_insert)


print(cursor)
con.commit()
con.close()