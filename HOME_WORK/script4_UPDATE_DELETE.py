import sqlite3 as sql
import pathlib as pathlib

FILE = 'test.db'
DB = pathlib.Path(__file__).parent.joinpath(FILE)

with sql.connect(DB) as con:
    cur = con.cursor()

    cur.execute("""UPDATE test SET score = score+55 WHERE name LIKE 'Nixter'
        
    """)