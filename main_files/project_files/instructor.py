import mysql.connector as sql, time as t

db = sql.connect(host = "localhost", user = "root", password = "225bench", database = "gym1")
cu = db.cursor()

def INSTRUCTOR():
	while True:
		print("1. View details")
		print("2. Add details")
		print("3. Delete details")
		print("4. Search details")
		print("5. Modify details")
		print("6. Exit")
		
		choice = int(input("Enter input (instructor): "))
		print()
		
		if choice == 1:
			cu.execute("SELECT * FROM INSTRUCTOR;")
			print("The instructors in your gym: ")
			for table in cu:
				print(table)
			print()
		if choice == 2:
			cu.execute("SELECT MAX(INS_ID) FROM INSTRUCTOR;")
			IDN = cu.fetchone()
			IDNO = ""
			for i in IDN:
				IDNO = str(i) + IDNO
			IDNO = int(IDNO)
			IDNO = IDNO + 1
		
			INS_ID = input("Enter ID ({}): ".format(IDNO))
			INS_NAME = input("Enter name: ")
			INS_NUMBER = input("Enter phone number (5XXXXXXXX): ")
			
			cu.execute("INSERT INTO INSTRUCTOR VALUES ('"+INS_ID+"', '"+INS_NAME+"', '"+INS_NUMBER+"');")
			db.commit()
			print()
			
		if choice == 3:
			NUM = input("Enter instructor name: ")
			
			cu.execute("DELETE FROM INSTRUCTOR WHERE INS_NAME LIKE '%"+NUM+"%'")
			db.commit()
			print()
			
		if choice == 4:
			NUM = input("Enter instructor name: ")
			
			cu.execute("SELECT * FROM INSTRUCTOR WHERE INS_NAME LIKE '%"+NUM+"%'")
			
			fetch = cu.fetchone()
			if fetch != None:
				print("Instructor name: {} found".format(NUM))
			if fetch == None:
				print("Instructor name: {} not found".format(NUM))
			print()
			
		if choice == 5:
			print("1. Instructor ID")
			print("2. Instructor name")
			print("3. Instructor number")
			
			choice = int(input("Enter input: "))
			print()
			
			if choice == 1:
				OLD = input("Enter name: ")
				NEW = input("Enter new ID: ")
				
				cu.execute("UPDATE INSTRUCTOR SET INS_ID = '"+NEW+"' WHERE INS_NAME LIKE '%"+OLD+"%'")
				db.commit()
				print()
			
			if choice == 2:
				OLD = input("Enter name: ")
				NEW = input("Enter new name: ")
				
				cu.execute("UPDATE INSTRUCTOR SET INS_NAME = '"+NEW+"' WHERE INS_NAME LIKE '%"+OLD+"%'")
				db.commit()
				print()
			
			if choice == 3:
				OLD = input("Enter name: ")
				NEW = input("Enter new number: ")
				
				cu.execute("UPDATE INSTRUCTOR SET INS_NUMBER = '"+NEW+"' WHERE INS_NAME LIKE '%"+OLD+"%'")
				db.commit()
				print()
			
		if choice == 6:
			break
