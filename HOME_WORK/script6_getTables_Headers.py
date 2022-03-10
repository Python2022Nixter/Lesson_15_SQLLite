import sqlite3 as sql
import pathlib
import package_sql_lite.util as util

NAME_DB = 'test.db'
DB = pathlib.Path(__file__).parent.joinpath(NAME_DB)
TABLE_1, TABLE_2 = util.get_tables(DB)

print(f"Tables in db: {util.get_tables(DB)}")
print(f"Headers of table '{TABLE_1}': {util.get_headers(TABLE_1, DB)}")
print(f"Headers of table '{TABLE_2}': {util.get_headers(TABLE_2, DB)}")

print(f"Unique names in db: {util.unique_names_in_db(DB, TABLE_1)}")
print(f"Unique names in db: {util.unique_names_in_db(DB, TABLE_2)}")