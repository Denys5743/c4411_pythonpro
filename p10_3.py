import sqlite3

connection = sqlite3.connect("itstep_DB.sl3",5)
cursor = connection.cursor()
cursor.execute("INSER INTO firs_table (name) VALUES ('Nick');")
cursor.execute("INSER INTO firs_table (name) VALUES ('Andriy');")
connection.commit()
connection.close()
