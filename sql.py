import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
	host="localhost",
	user="marko",
	passwd="marko",
	database="testdatabese"
	)

mycursor = db.cursor()

#ovo se ne izvodi ovo je samo moje skupljanje korisnih komandi

db.commit()
mycursor.execute("DESCRIBE Person") #komanda za opis stupova i redova

mycursor.execute("SELECT * FROM Person") #komanda za biranje svih iz tablice

mycursor.execute("CREATE TABLE Test (name VARCHAR(50) NOT NULL, created datetime NOT NULL, gender ENUM('M', 'F') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")

mycursor.execute("SELECT * FROM Test WHERE gender = 'M'") #vadjenje po nekom kriteriju
mycursor.execute("SELECT * FROM Test WHERE gender = 'M' ORDER BY id DESC") #Mijenjanje redoslijeda
mycursor.execute("SELECT name FROM Test WHERE gender = 'M'") #vadjenje samo iz stupaca

mycursor.execute("ALTER TABLE Test ADD COLUMN food VARCHAR(50) NOT NULL") #izmjena tablice - dodavanje stupca
mycursor.execute("ALTER TABLE Test DROP food") #brisanje stupca
mycursor.execute("ALTER TABLE Test CHANGE name first_name VARCHAR(50)") #mijenjanje stupca


for x in mycursor: #hod kroz tablicu
	print(x)