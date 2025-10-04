import sqlite3

connection = sqlite3.connect("itstep_DB.sl3",5)
cursor = connection.cursor()
cursor.execute("CREATE TABLE first_table(name TEXT);")
connection.commit()
connection.close()
