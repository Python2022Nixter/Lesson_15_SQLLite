import os
import pathlib
import sqlite3

DB_FILE = "python_test_db2.db"
PATH_TO_FILE = pathlib.Path(__file__).parent.joinpath(DB_FILE)

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

for i in range(10):
    sql_query += F"""
    INSERT INTO test(name, email) VALUES("Jhon{i}", 12{i});
"""

con = None
res = None
try:
    con = sqlite3.connect(PATH_TO_FILE)
    # todo

    pass
except sqlite3.Error as e:
    print(e)
    pass
else:
    cursor = con.cursor()
    cursor.executescript(sql_query)
finally:
    res = con.execute("SELECT * FROM test")
    print(res.fetchall())
    cursor.close()

print("Done")


con.commit()
con.close()
