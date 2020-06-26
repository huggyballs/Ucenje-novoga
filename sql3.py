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

#ime = input("Unesite ime: ")
#godine = int(input("Unesite godine: "))

#mycursor.execute("INSERT INTO Family (name, age) VALUES (%s,%s)", (ime, godine))
#db.commit()

#last_id = mycursor.lastrowid
#uredjaj = int(input("Unesite id uredjaja: "))

#mycursor.execute("INSERT INTO Devices (userid, deviceid) VALUES (%s,%s)", (last_id, uredjaj))
#db.commit()

mycursor.execute("SELECT * FROM Family")

for x in mycursor:
    print(x)

mycursor.execute("SELECT * FROM Devices")

for x in mycursor:
    print(x)

mycursor.execute("SELECT userid FROM Devices WHERE deviceid = '1234'")

devajs = mycursor.fetchone()
devajs2 = int(''.join(map(str, devajs))) #BITNO! Nacin pretvaranja tuplea u broj
print("grabimo...")
print (devajs2)

mycursor.execute("SELECT * FROM Family WHERE id = %s", (devajs2,))

korisnik = mycursor.fetchone()
print("grabimo...")
print(korisnik)