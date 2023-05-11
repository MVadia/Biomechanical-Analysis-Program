import sqlite3

##connect to database
connect = sqlite3.connect("loginData.db")
cursor = connect.cursor()

cursor.execute('''CREATE TABLE patient_login (id INTEGER PRIMARY KEY, name TEXT, password TEXT)''')
cursor.execute("INSERT INTO patient_login (name, password) VALUES (?, ?)", ('John Smith', 'password321'))
connect.commit()
connect.close()


