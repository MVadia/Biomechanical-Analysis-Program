import sqlite3

connect = sqlite3.connect("loginData.db")
cursor = connect.cursor()

cursor.execute("DELETE FROM patient_login")
cursor.execute("DELETE FROM patientDetails")
cursor.execute("DELETE FROM patientDetails_fromDoctor")


connect.commit()
connect.close()