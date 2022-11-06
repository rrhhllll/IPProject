import mysql.connector as sql, time as t, datetime

db = sql.connect(host = "localhost", user = "root", password = "225bench", database = "gym1")
cu = db.cursor()

def SIGN_UP():
	USE_ID = input("Enter user ID: ")
	USE_USERNAME = input("Enter username: ")
	USE_PASSWORD = input("Enter password: ")
	
	cu.execute("INSERT INTO USER VALUES ('"+USE_ID+"', '"+USE_USERNAME+"', '"+USE_PASSWORD+"');")
	db.commit()
	
	print("Enter additional information, in majuscules")
	t.sleep(0.5)
	print()
	
	cu.execute("SELECT MAX(MEM_ID) FROM MEMBER;")
	IDN = cu.fetchone()
	IDNO = ""
	for i in IDN:
		IDNO = str(i) + IDNO
	IDNO = int(IDNO)
	IDNO = IDNO + 1
	
	MEM_ID = input("Enter ID ({}): ".format(IDNO))
	MEM_NAME = input("Enter name: ")
	MEM_NUMBER = input("Enter phone number (05X-XXX-XXXX): ")
	MEM_AGE = input("Enter age: ")
	MEM_GENDER = input("Enter gender (M / F): ")
	MEM_LEVEL = input("Enter subscription level (BASIC / STANDARD / PREMIUM): ")
	
	cu.execute("INSERT INTO MEMBER VALUES ('"+MEM_ID+"', '"+MEM_NAME+"', '"+MEM_AGE+"', '"+MEM_GENDER+"', '"+MEM_LEVEL+"', '"+MEM_NUMBER+"');")
	db.commit()
	print()
	
	print("Additional information entered")
	print("Redirecting to home page")
	t.sleep(0.5)
	print()