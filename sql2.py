import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
	host="localhost",
	user="marko",
	passwd="marko",
	database="testdatabese"
	)

mycursor = db.cursor()

try:
	mycursor.execute("CREATE TABLE Users2 (id int PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(50) NOT NULL)")
	mycursor.execute("CREATE TABLE Devices (id2 int PRIMARY KEY NOT NULL AUTO_INCREMENT, userid int NOT NULL, deviceid VARCHAR(25))")
	pass
except:
	print("Ne valja!")
	pass

print("Unesi ime: ")
ime = input()

mycursor.execute("INSERT INTO Users (name) VALUES (%s)", (ime))
db.commit()

last_id = mycursor.lastrowid
print("Unesi id uredjaja: ")
ur = input()

mycursor.execute("INSERT INTO Devices (userid, deviceid) VALUES (%s, %s)", (last_id, ur))
db.commit()

mycursor.execute("SELECT * FROM Users")

for x in mycursor:
	print(x)

mycursor.execute("SELECT * FROM Devices")

for x in mycursor:
	print(x)