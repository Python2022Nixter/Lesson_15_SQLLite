
import sqlite3 as sql
import package_sql_lite.util as util
import pathlib as pathlib

FILE = 'test.db'
DB = pathlib.Path(__file__).parent.joinpath(FILE)
util.create_db(DB)


name = 'Nixter'
res = util.count_name_in_db(name, DB)

print(f"Number of rows with name '{name}': {res}")

print(f"Number of unique names in db: {util.count_unique_names_in_db(DB)}")
print(f"Unique names in db: {util.unique_names_in_db(DB)}")
print(f"Score of name '{name}': {util.count_score_of_name(name,DB)}")

util.insert_into_db_random(3, DB)
