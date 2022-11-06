import mysql.connector as sql, time as t

db = sql.connect(host = "localhost", user = "root", password = "225bench", database = "gym1")
cu = db.cursor()

def MEMBER():
	while True:
		print("1. View details")
		print("2. Add details")
		print("3. Delete details")
		print("4. Search details")
		print("5. Modify details")
		print("6. Exit")
		
		choice = int(input("Enter input (member): "))
		print()
		
		if choice == 1:
			cu.execute("SELECT * FROM MEMBER;")
			
			print("The members in your gym: ")
			for table in cu:
				print(table)
			print()

		if choice == 2:
			cu.execute("SELECT MAX(MEM_ID) FROM MEMBER;")
			IDN = cu.fetchone()
			IDNO = ""
			for i in IDN:
				IDNO = str(i) + IDNO
			IDNO = int(IDNO)
			IDNO = IDNO + 1
		
			MEM_ID = input("Enter ID ({}): ".format(IDNO))
			MEM_NAME = input("Enter name: ")
			MEM_NUMBER = input("Enter phone number (X5X-XXX-XXXX): ")
			MEM_AGE = input("Enter age: ")
			MEM_GENDER = input("Enter gender (M / F): ")
			MEM_LEVEL = input("Enter subscription level (BASIC / STANDARD / PREMIUM): ")
			
			cu.execute("INSERT INTO MEMBER VALUES ('"+MEM_ID+"', '"+MEM_NAME+"', '"+MEM_AGE+"', '"+MEM_GENDER+"', '"+MEM_LEVEL+"', '"+MEM_NUMBER+"');")
			db.commit()
			print()
			
		if choice == 3:
			NUM = input("Enter member name: ")
			
			cu.execute("DELETE FROM MEMBER WHERE MEM_NAME LIKE '%"+NUM+"%'")
			db.commit()
			print()
			
		if choice == 4:
			NUM = input("Enter member name: ")
			
			cu.execute("SELECT * FROM MEMBER WHERE MEM_NAME LIKE '%"+NUM+"%'")
			
			fetch = cu.fetchone()
			if fetch != None:
				print("Member name: {} found".format(NUM))
			if fetch == None:
				print("Member name: {} not found".format(NUM))
			print()
			
		if choice == 5:
			print("1. Member ID")
			print("2. Member name")
			print("3. Member age")
			print("4. Member gender")
			print("5. Member subscription level")
			print("6. Member number")
			
			choice = int(input("Enter input: "))
			print()
			
			if choice == 1:
				OLD = input("Enter name: ")
				NEW = input("Enter new ID: ")
				
				cu.execute("UPDATE MEMBER SET MEM_ID = '"+NEW+"' WHERE MEM_NAME LIKE '%"+OLD+"%'")
				db.commit()
				print()
			
			if choice == 2:
				OLD = input("Enter name: ")
				NEW = input("Enter new name: ")
				
				cu.execute("UPDATE MEMBER SET MEM_NAME = '"+NEW+"' WHERE MEM_NAME LIKE '%"+OLD+"%'")
				db.commit()
				print()
			
			if choice == 3:
				OLD = input("Enter name: ")
				NEW = input("Enter new age: ")
				
				cu.execute("UPDATE MEMBER SET MEM_AGE = '"+NEW+"' WHERE MEM_NAME LIKE '%"+OLD+"%'")
				db.commit()
				print()
			
			if choice == 4:
				OLD = input("Enter name: ")
				NEW = input("Enter new gender: ")
				
				cu.execute("UPDATE MEMBER SET MEM_GENDER = '"+NEW+"' WHERE MEM_NAME LIKE '%"+OLD+"%'")
				db.commit()
				print()
			
			if choice == 5:
				OLD = input("Enter name: ")
				NEW = input("Enter new subscription level: ")
				
				cu.execute("UPDATE MEMBER SET MEM_LEVEL = '"+NEW+"' WHERE MEM_NAME LIKE '%"+OLD+"%'")
				db.commit()
				print()
			
			if choice == 6:
				OLD = input("Enter name: ")
				NEW = input("Enter new number: ")
				
				cu.execute("UPDATE MEMBER SET MEM_NUMBER = '"+NEW+"' WHERE MEM_NAME LIKE '%"+OLD+"%'")
				db.commit()
				print()
			
		if choice == 6:
			break
