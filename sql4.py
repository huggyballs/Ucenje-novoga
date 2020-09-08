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
    mycursor.execute("CREATE TABLE Example (id int PRIMARY KEY NOT NULL AUTO_INCREMENT, ajdi int, dt DATETIME)")
    pass
except:
    print("nece")
    pass

now = datetime.now()
now = now.strftime('%Y-%m-%d %H:%M:%S')

mycursor.execute("INSERT INTO Example (ajdi, dt) VALUES (%s, %s)", (1, strnow))
db.commit()

mycursor.execute("SELECT * FROM Example")

for x in mycursor:
	print(x)