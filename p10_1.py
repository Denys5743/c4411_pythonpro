import sqlite3
from asyncio import timeout

connection = sqlite3.connect("itstep_DB.sl3",5)
cursor = connection.cursor()
print(connection)
print(cursor)
connection.close()