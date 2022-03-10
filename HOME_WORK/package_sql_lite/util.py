from random import random
import sqlite3 as sql
import random

DB = 'test.db'


def create_db(db=DB):
    with sql.connect(db) as con:
        cur = con.cursor()
        try:
            cur.execute("""CREATE TABLE "test" (
	                        "id"	INTEGER,
	                        "name"	TEXT NOT NULL,
	                        "old"	INTEGER DEFAULT 0,
	                        "score"	INTEGER,
	                            PRIMARY KEY("id")
                                );
                            """)
            pass
        except sql.OperationalError:
            print("Table already exists")
            pass


def insert_into_db_random(number: int, db=DB):

    names = ['Nixter', 'Max', 'John', 'Daiil', 'Vanya', 'Fred']
    olds = [20, 30, 40, 50, 60, 70]
    scores = [40, 50, 60, 70, 80, 90]

    with sql.connect(db) as con:
        cur = con.cursor()

        for i in range(number):
            name = random.choice(names)
            old = random.choice(olds)
            score = random.choice(scores)
            cur.execute("""INSERT INTO test (name, old, score)
                        VALUES (?, ?, ?)""", (name, old, score))


def count_name_in_db(name: str, db=DB):
    with sql.connect(db) as con:
        cur = con.cursor()
        res = cur.execute(
            """SELECT COUNT(*) FROM test WHERE name LIKE '%{}%'""".format(name))
        count = None
        try:
            count = res.fetchone()[0]
        except:
            pass
        return count


def count_unique_names_in_db(db=DB):
    with sql.connect(db) as con:
        cur = con.cursor()
        res = cur.execute("""SELECT COUNT(DISTINCT name) FROM test""")
        count = None
        try:
            count = res.fetchone()[0]
            pass
        except:
            print("Error")
            pass
        return count


def unique_names_in_db(db=DB):
    with sql.connect(db) as con:
        cur = con.cursor()
        res = cur.execute("""SELECT DISTINCT name FROM test""")
        names = res.fetchall()
        names = set(names)
        return names


def count_score_of_name(name: str, db=DB):
    with sql.connect(db) as con:
        cur = con.cursor()
        res = cur.execute(f"""SELECT sum(score) as score FROM test 
        WHERE name = '{name}' 
        """)
        number = res.fetchall()[0][0]
        return number


def get_headers(tb:str, db=DB):
    with sql.connect(db) as con:
        cur = con.cursor()
        data = cur.execute(f"""PRAGMA table_info({tb})""").fetchall()
        headers = [x[1] for x in data]
        return headers


def get_tables(db=DB):
    with sql.connect(db) as con:
        cur = con.cursor()
        data = cur.execute("""SELECT name FROM sqlite_master WHERE type='table'""").fetchall()
        tables = [x[0] for x in data]
        return tables