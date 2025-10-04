import sqlite3

connection = sqlite3.connect("itstep_DB.sl3",5)
cursor = connection.cursor()
cursor.execute("SELECT rowid, name FROM firs_table;")

connection.commit()
res = cursor.fetchall()
print(res)
connection.close()