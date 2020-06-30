import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="raspberry",
	database="practicedatabase"
	)

mycursor = db.cursor()

try:
    mycursor.execute("CREATE TABLE Family (name VARCHAR(50) NOT NULL, age smallint UNSIGNED NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
    pass
except:
    pass

try:
    mycursor.execute("CREATE TABLE Devices (id2 int PRIMARY KEY NOT NULL AUTO_INCREMENT, userid int NOT NULL, deviceid int NOT NULL)")
    pass
except:
    pass

try:
    mycursor.execute("CREATE TABLE names (id3 int PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(30) NOT NULL)")
    pass
except:
    print("postoji")
    pass

#ime2 = input("Unesite ime: ")
#print(ime2)
#ime = input("Unesite ime: ")
#godine = int(input("Unesite godine: "))

#mycursor.execute("INSERT INTO Family (name, age) VALUES (%s,%s)", (ime, godine))
#db.commit()

#last_id = mycursor.lastrowid
#print(last_id)
#uredjaj = int(input("Unesite id uredjaja: "))

#mycursor.execute("INSERT INTO Devices (userid, deviceid) VALUES (%s,%s)", (last_id, uredjaj))
#db.commit()

#mycursor.execute("INSERT INTO names (name) VALUES(%s,)", ime2)
#db.commit()

mycursor.execute("SELECT * FROM Family")

last_id = mycursor.lastrowid
print(last_id)

for x in mycursor:
    print(x)

mycursor.execute("SELECT * FROM Devices")

for x in mycursor:
    print(x)

devid = 1234
mycursor.execute("SELECT userid FROM Devices WHERE deviceid = %s", (devid,))

devajs = mycursor.fetchone()
devajs = int(''.join(map(str, devajs))) #BITNO! Nacin pretvaranja tuplea u broj
print("grabimo...")
print (devajs)

mycursor.execute("SELECT * FROM Family WHERE id = %s", (devajs,))

korisnik = mycursor.fetchone()
print("grabimo...")
print(korisnik)

#mycursor.execute("SELECT * FROM names WHERE name = %s", (ime2))
#drugoime = mycursor.fetchone()
#print("grabimo...")
#print(drugoime)

try:
    mycursor.execute("SELECT * FROM Devices WHERE deviceid = '5293")
    pass
except:
    print("Greska")
    pass
