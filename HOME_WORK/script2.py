import sqlite3 as sql


with sql.connect('test.db') as con:
    cur = con.cursor()

    #cur.execute("DROP TABLE IF EXISTS test")
    cur.execute("""Create table if not exists test(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL,
        old INTEGER default 0,
        score INTEGER
        )
    """)
    # cur.execute("DROP TABLE test")



