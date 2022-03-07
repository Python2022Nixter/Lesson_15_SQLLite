import sqlite3 as sql
import pathlib
import package_sql_lite.util as util

NAME_DB = 'test.db'
TABLE_1 = 'test'
TABLE_2 = 'idiots2022'
DB = pathlib.Path(__file__).parent.joinpath(NAME_DB)

print(f"Heders of table {TABLE_1}: {util.get_headers(TABLE_1, DB)}")
print(f"Heders of table {TABLE_2}: {util.get_headers(TABLE_2, DB)}")

# with sql.connect(DB) as con:
#     cur = con.cursor()
#     headers = cur.execute("""PRAGMA table_info(idiots2022)""").fetchall()
#     res = [x[1] for x in headers]
#     print(res)