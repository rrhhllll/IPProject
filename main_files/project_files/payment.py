import mysql.connector as sql, time as t

db = sql.connect(host = "localhost", user = "root", password = "225bench", database = "gym1")
cu = db.cursor()

def PAYMENT():
	while True:
		print("1. View details")
		print("2. Pay fees")
		print("3. Exit")
		
		choice = int(input("Enter input (payment): "))
		print()
		
		if choice == 1:
			cu.execute("SELECT * FROM PAYMENT;")
			print("The payment details: ")
			for table in cu:
				print(table)
			print()

		if choice == 2:
			NUM = input("Enter ID: ")
			cu.execute("SELECT PAY_AMOUNT FROM PAYMENT WHERE MEM_ID = '"+NUM+"'")
			fetch = cu.fetchone()
			fetchre = fetch[0]
			print("You have to pay: {} AED".format(fetchre))
			
			C_NAME = input("Enter name on card: ")
			C_NUMBER = input("Enter number on card (XXXX XXXX XXXX XXXX): ")
			C_EXPDATE = input("Enter expiration date on card: ")
			C_CVV = input("Enter security code on card: ")
			
			C_MII1 = C_NUMBER[:1]
			C_MII2 = C_NUMBER[:2]
			C_MII3 = C_NUMBER[:3]
			print()
			print("Summary: ")
			if C_MII1 == "3":
				print("Card issuer: American Express")
			if C_MII1 == "4":
				print("Card issuer: VISA")
			if C_MII1 == "5":
				print("Card issuer: MasterCard")
			print("Name on card: {}".format(C_NAME))
			print("Card number: {}".format(C_NUMBER))
			print("Card expiration date: {}".format(C_EXPDATE))
			print("Card security code: {}".format(C_CVV))
			print()
			print("Processing transaction")
			t.sleep(2)
			print("Transaction successful")

		if choice == 3:
			break