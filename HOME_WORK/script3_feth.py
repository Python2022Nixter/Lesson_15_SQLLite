import sqlite3 as sql
import pathlib as pathlib

FILE = 'test.db'
DB = pathlib.Path(__file__).parent.joinpath(FILE)

with sql.connect('test.db') as con:
    cur = con.cursor()

    cur.execute("SELECT * FROM test")
    result = cur.fetchall()
    cur.execute("SELECT * FROM test")
    result1 = cur.fetchone()
    cur.execute("SELECT * FROM test")
    result2 = cur.fetchmany(3)
    for row in result:
        print(row)
    
    
    print()
    print(result1)
    print()
    for row in result2:
        print(row)