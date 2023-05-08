import sqlite3

##connect to database
connect = sqlite3.connect("loginData.db")
cursor = connect.cursor()

cursor.execute('''CREATE TABLE doctors (id INTEGER PRIMARY KEY, name TEXT, password TEXT)''')
cursor.execute("INSERT INTO doctors (name, password) VALUES (?, ?)", ('Dr. Smith', 'password321'))
connect.commit()
connect.close()
