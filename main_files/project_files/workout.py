import mysql.connector as sql, time as t

db = sql.connect(host = "localhost", user = "root", password = "225bench", database = "gym1")
cu = db.cursor()

def WORKOUT():
	cu.execute("SELECT * FROM EQUIPMENT;")
	
	print("The equipments in your gym: ")
	for table in cu:
		print(table)
	print()
