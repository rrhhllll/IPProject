import mysql.connector as sql, time as t

db = sql.connect(host = "localhost", user = "root", password = "225bench", database = "gym1")
cu = db.cursor()

def EQUIPMENT():
	while True:
		print("1. View details")
		print("2. Add details")
		print("3. Delete details")
		print("4. Search details")
		print("5. Modify details")
		print("6. Exit")
		
		choice = int(input("Enter input (equipment): "))
		print()
		
		if choice == 1:
			cu.execute("SELECT * FROM EQUIPMENT;")
			
			print("The equipments in your gym: ")
			for table in cu:
				print(table)
			print()
		
		if choice == 2:
			cu.execute("SELECT MAX(EQU_ID) FROM EQUIPMENT;")
			IDN = cu.fetchone()
			IDNO = ""
			for i in IDN:
				IDNO = str(i) + IDNO
			IDNO = int(IDNO)
			IDNO = IDNO + 1
		
			EQU_ID = input("Enter ID ({}): ".format(IDNO))
			EQU_NAME = input("Enter name: ")
			EQU_COMPANY = input("Enter company: ")
			EQU_KIND = input("Enter kind: ")
			
			cu.execute("INSERT INTO EQUIPMENT VALUES ('"+EQU_ID+"', '"+EQU_NAME+"', '"+EQU_COMPANY+"', '"+EQU_KIND+"');")
			db.commit()
			print()
			
		if choice == 3:
			NUM = input("Enter equipment name: ")
			
			cu.execute("DELETE FROM EQUIPMENT WHERE EQU_NAME LIKE '%"+NUM+"%'")
			db.commit()
			print()
			
		if choice == 4:
			NUM = input("Enter equipment name: ")
			
			cu.execute("SELECT * FROM EQUIPMENT WHERE EQU_NAME LIKE '%"+NUM+"%'")
			
			fetch = cu.fetchone()
			if fetch != None:
				print("Equipment name: {} found".format(NUM))
			if fetch == None:
				print("Equipment name: {} not found".format(NUM))
			print()
			
		if choice == 5:
			print("1. Equipment ID")
			print("2. Equipment name")
			print("3. Equipment company")
			print("4. Equipment kind")
			
			choice = int(input("Enter input: "))
			print()
			
			if choice == 1:
				OLD = input("Enter old ID: ")
				NEW = input("Enter new ID: ")
				
				cu.execute("UPDATE EQUIPMENT SET EQU_ID = '"+NEW+"' WHERE EQU_NAME LIKE '%"+OLD+"%'")
				db.commit()
				print()
			
			if choice == 2:
				OLD = input("Enter old name: ")
				NEW = input("Enter new name: ")
				
				cu.execute("UPDATE EQUIPMENT SET EQU_NAME = '"+NEW+"' WHERE EQU_NAME LIKE '%"+OLD+"%'")
				db.commit()
				print()
			
			if choice == 3:
				OLD = input("Enter old company: ")
				NEW = input("Enter new company: ")
				
				cu.execute("UPDATE EQUIPMENT SET EQU_COMPANY = '"+NEW+"' WHERE EQU_NAME LIKE '%"+OLD+"%'")
				db.commit()
				print()
			
			if choice == 4:
				OLD = input("Enter old kind: ")
				NEW = input("Enter new kind: ")
				
				cu.execute("UPDATE EQUIPMENT SET EQU_KIND = '"+NEW+"' WHERE EQU_NAME LIKE '%"+OLD+"%'")
				db.commit()
				print()
			
		if choice == 6:
			break